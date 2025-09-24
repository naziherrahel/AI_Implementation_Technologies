
# Practice 1_2 : Extracting Video Frames with OpenCV

## Objective
Use OpenCV to extract frames from a video file at 1-second intervals and display the first frame.

## Pre-requisites
- Install OpenCV: `pip install opencv-python`
- A test video (`sample_video.mp4`) should be placed in this directory

## Usage
```bash
python extract_frames.py --video sample_video.mp4 --out frames --interval 1
```

## Your Tasks
- [ ] Allow extraction by frame count instead of seconds
- [ ] Add timestamp watermark to each frame
- [ ] Allow skipping the first N seconds before extraction
- [ ] Use argparse to allow grayscale extraction (`--gray` flag)
- [ ] Write extracted frame paths to a CSV file

## Submission
- Show at least 3 extracted frames
- Screenshot: `cv2.imshow()` preview window
- CSV with paths or image previews

---