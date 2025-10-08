# Import SQLAlchemy modules to define the database schema.
# SQLAlchemy allows us to define tables and columns in a Pythonic way.
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, Float, DateTime, MetaData

# Create a MetaData object to hold table definitions.
# This acts as a container for all tables we define, like 'new_detections'.
metadata = MetaData()

# Define the 'new_detections' table for storing dust detection data.
# This table aligns with our dust detection system, storing data from processed video frames.
new_detections = Table(
    "new_detections",
    metadata,
    # ID is an auto-incrementing primary key to uniquely identify each detection.
    Column("id", Integer, primary_key=True),
    # Filename stores the name of the image file (e.g., 'frame_000.jpg') from our frame extraction lab.
    Column("filename", String, nullable=False),
    # Bbox is a JSON column storing bounding box coordinates [x, y, w, h] for detected dust.
    # JSON is flexible for storing structured data like arrays.
    Column("bbox", sqlalchemy.JSON, nullable=False),
    # Confidence is a float (0.0 to 1.0) indicating the model's certainty of the detection.
    Column("confidence", Float, nullable=False),
    # Timestamp records when the detection occurred, using a timezone-aware column for consistency.
    # This avoids issues with naive vs. aware datetimes, as we saw in earlier labs.
    Column("timestamp", DateTime(timezone=True), nullable=False)
)

