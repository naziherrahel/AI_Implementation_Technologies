# Frame Extraction from Dust Videos

**Stage**: Main Project - Preprocessing\
**Difficulty Level**: Medium

---

## Objective

You will implement the first real step of the dust detection pipeline by writing scripts to extract frames from the provided aluminum dust videos. This task includes frame rate selection, saving extracted images in a structured format, and committing results to your GitHub repo.

---

## Instructions

### 1. Goal

From your team’s assigned video(s), extract image frames at an appropriate interval. The extracted images will later be annotated.

### 2. Analyze the Video

- Use OpenCV (or a similar library) to load the video.
- Calculate total frame count, duration, and FPS.
- Based on your planning from your previous session, select an appropriate **frame extraction rate** (e.g., every 5th frame, or 1 frame every X seconds).

### 3. Save Extracted Frames

- Create a subfolder per video inside `images/raw/`

  Example:
  ```
  images/
  ├── raw/
  │   └── video01/
  │       ├── frame_0001.jpg
  │       └── frame_0002.jpg
  ```
- Make sure image filenames are sequential and easily traceable.

### 4. Visualize Frame Intervals (Optional but Encouraged)

- Extract and display a grid of frames using different intervals (e.g., every 5th vs every 15th frame).
- You can use `matplotlib` to plot them side-by-side or save them in a debug folder:

  ```
  images/debug/frame_interval_comparison/
  ```
- This helps evaluate whether the chosen interval captures enough relevant movement or objects.

### 5. Log Your Work

- Save a short summary in `extract_info.txt` next to the extracted frames:

  Example content:
  ```
  Video: video01.mp4
  FPS: 30
  Total frames: 2700
  Extraction interval: every 5 frames
  Total extracted: 540
  Start time: 00:00:00
  End time: 00:01:30
  Note: Low motion in first 20 seconds
  ```

### 6. Commit to GitHub

- Push your `scripts/split_video.py` (fully working now)
- Push extracted frames (or at least a few for inspection — avoid overloading the repo) 
- Commit log files and updated folder structure

---

## Recommended Folder Updates

```
├── images
│   ├── raw
│   │   ├── video01
│   │   └── video02
│   └── debug
│       └── frame_interval_comparison
├── scripts
│   └── split_video.py
├── annotations
├── results
├── logs
```

---

## Deliverables (by end of session)

Each team must complete the following:

- Updated and working `split_video.py` script
- Extracted frames for at least one video saved to `images/raw/`
- `extract_info.txt` with basic stats: frame count, interval used, FPS, notes
- Pushed to GitHub: script + sample frames + logs
- Update `project_plan.md` with actual extraction rate used
- (Optional) Visual grid comparing two extraction rates (for bonus)

---

## Tips

- You can reuse OpenCV’s `VideoCapture.read()` and `cv2.imwrite()`
- Use `os.makedirs()` to create folders programmatically
- Limit GitHub image uploads (use `.gitignore` if needed)
- If processing multiple videos, use a loop and keep code modular

---

## Grading

You’ll be graded on:

- Script functionality and clarity
- Folder and code organization
- Logical frame sampling strategy
- Documentation/logs quality in GitHub
- Bonus for visualization of different frame intervals

---

