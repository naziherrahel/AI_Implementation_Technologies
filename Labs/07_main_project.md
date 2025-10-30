# Group Formation & Project Planning

**Duration**: 1.5 hours\
**Stage**: Start of Main Project\
**Week**: 5 (First Session)\
**Difficulty Level**: Medium → High (Team coordination, tool selection, real-world planning)

---

## Objective

In this practice, you will officially begin the main project by forming your teams, choosing appropriate tools, and creating a structured project plan. You will:

- Form a team of 2–3 students
- Create and organize your team GitHub repository
- Choose your annotation tool should be mentioned in your plan (LabelImg or Roboflow)
- Create an initial project plan with task assignments
- Set up your team folder structure and push to GitHub
- Review the full pipeline stages (annotation, training, inference, logging, storage)

---

## Instructions

### 1. Team Formation

- Form a group of **2–3 members max**.
- Choose a **team name** (will be used in folder naming).
- Share your team name and member list with me.

### 2. GitHub Setup

Each team must:

- Create a GitHub repo titled: `detection-{team-name}`
- Add all members as collaborators
- Push an initial folder structure (see below)

### 3. Project Planning

In your team, discuss and finalize:

- **Who will do what** (e.g., splitting, annotation, training, reporting, database setup, deployment ...)
- **Which tool** to use for annotation (LabelImg or Roboflow)
- **Which annotation format** you will follow (YOLO is recommended)
- Deadlines for each step (you have 5 weeks, use your calendar wisely!)

Prepare a `project_plan.md` file with:

- Task list & deadlines
- Assigned roles
- Chosen tools & reasons
- Planned outputs for each phase (e.g., annotated images, trained model, inference results, database, Docker)

---

## Folder Structure

Start your GitHub repo with this template:

```
├── README.md
├── project_plan.md
├── data
│   └── videos
├── notebooks
├── scripts
│   └── split_video.py
├── annotations
├── images
├── results
├── database
├── docker
└── utils
```

---

## Deliverables (by end of session)

Each team must submit or complete the following by the end of this practice session:

- Team formation completed and shared with me (team name + members)
- GitHub repository created (`detection-{team-name}`), shared with team & instructor
- Initial folder structure pushed to GitHub (based on provided template)
- `project_plan.md` committed to GitHub

---

## Tips

- **Be realistic**: Don't plan to annotate 1000 images in one day
- You can switch roles later, but initial planning is important
- Don’t delay GitHub setup: it's a habit for good engineering
- Use screenshots and visual aids in your plan if helpful
- Plan now for later steps like database storage or container packaging

---

## Grading

This is a **milestone checkpoint**. Your participation, planning, and code organization will impact your **final project grade**.

