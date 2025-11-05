# Manual Image Annotation

**Stage**: Main Project - Annotation  
**Difficulty Level**: Medium

---

## Objective

You will manually annotate a subset of the extracted video frames using an annotation tool. These annotations will form the basis for model training. The team will also decide the labeling format and ensure all annotations are properly saved and committed to GitHub.

---

## Instructions

### 1. Choose Annotation Tool

Pick one of the following tools:
- **LabelImg**: local tool, easy to use, outputs YOLO format
- **Roboflow**: online platform, supports both YOLO and COCO export


### 2. Define Label Schema

- For now, annotate **only one class**: `dust`
- Class name should be lowercase and consistent across all annotations

### 3. Annotatation

- Ensure bounding boxes are:
  - Tight around the dust
  - Accurate and consistent

### 4. Choose Annotation Format

- Decide on **YOLO** or **COCO** format as a team
  - LabelImg outputs YOLO by default
  - Roboflow supports exporting in both
- Stick to one format for the whole team

### 5. Organize and Save

Save annotations in the following structure:
```
annotations/
└── raw/
    ├── video01/
    │   ├── frame_0001.txt
    │   └── frame_0002.txt
    └── video02/
```

### 6. Update `project_plan.md`

Include the following:
- Annotation tool used
- Format selected
- Class list (e.g., dust)
- Sample image with annotation (optional screenshot)

### 7. Push to GitHub

- Commit the following:
  - Annotated text files (YOLO/COCO format)
  - Screenshot of annotation tool in use (optional)
  - Updated `project_plan.md`

---

## Deliverables 

Each team must complete:

- Annotation
- Chosen and applied consistent annotation format (YOLO or COCO)
- Files saved in `annotations/raw/videoXX/`
- `project_plan.md` updated with:
  - Format
  - Tool used
  - Class list
- Pushed everything to GitHub
- (Optional) Screenshot of annotation tool in use

---

## Grading

You’ll be graded on:

- Annotation quality (precision, consistency)
- Folder and file organization
- Correct use of format and tool
- Clear documentation in `project_plan.md`
- GitHub commit history and structure

---

## Tips

- Use `Tab` in LabelImg to switch between boxes
- Ensure all annotations are for visible dust only
- Roboflow allows team collaboration if needed
- If unsure about bounding box guidelines, ask me "the instructor"

