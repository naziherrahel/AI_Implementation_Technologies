import cv2
import os
import torch
from ultralytics import YOLO
from fastapi import FastAPI
from datetime import datetime
import psycopg2
import uuid
from fastapi.staticfiles import StaticFiles

# --- App Setup ---
app = FastAPI()

# Serve detected frames at /frames URL
app.mount("/frames", StaticFiles(directory="detected_frames"), name="frames")
model = YOLO("yolov8n.pt")  # pretrained model (COCO)
SAVE_DIR = "detected_frames"
os.makedirs(SAVE_DIR, exist_ok=True)

# --- Database Setup ---
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "admin")
DB_NAME = os.getenv("DB_NAME", "detection_db")

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS detections (
    id UUID PRIMARY KEY,
    class_name TEXT,
    confidence FLOAT,
    timestamp TIMESTAMP,
    image_path TEXT
);
""")
conn.commit()


# --- Helper: Select Input Source ---
def get_video_source():
    """Try webcam first, fallback to sample video."""
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        cap.release()
        print("Webcam detected — using live camera feed")
        return 0
    else:
        print("Webcam not found — using sample_video.mp4")
        if not os.path.exists("sample_video.mp4"):
            raise FileNotFoundError(
                "No webcam or sample_video.mp4 found. Add a sample video to the project folder."
            )
        return "sample_video.mp4"


# --- Detection Endpoint ---
@app.get("/detect")
def detect():
    source = get_video_source()
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        return {"error": "Camera or video not accessible"}

    ret, frame = cap.read()
    cap.release()

    if not ret:
        return {"error": "Failed to capture frame"}

    # Run YOLO
    results = model(frame)[0]
    timestamp = datetime.now()
    filename = f"{timestamp.strftime('%Y%m%d_%H%M%S')}.jpg"
    save_path = os.path.join(SAVE_DIR, filename)

    # Draw detections + log to DB
    for box in results.boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        class_name = model.names[cls_id]

        if class_name != "person":
            continue  # Only log "person"

        xyxy = box.xyxy[0].cpu().numpy().astype(int)
        x1, y1, x2, y2 = xyxy
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f"{class_name} ({conf:.2f})"
        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Log detection
        cursor.execute("""
        INSERT INTO detections (id, class_name, confidence, timestamp, image_path)
        VALUES (%s, %s, %s, %s, %s)
        """, (str(uuid.uuid4()), class_name, conf, timestamp, save_path))
        conn.commit()

    cv2.imwrite(save_path, frame)
    return {"message": f"Frame saved and detection logged: {save_path}"}
