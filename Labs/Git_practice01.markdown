# Git Fundamentals: Professional Workflow Practice

**Objective:** This lab will guide you through initializing a Git repository and making your first commits using a professional, real-world workflow. You will create project boilerplate, write code, and practice crafting meaningful commit messages.

## Prerequisites

- Git installed on your machine.
- A terminal (Command Prompt, PowerShell, or Bash).

## Task 1: Project Initialization

1. Open your terminal.
2. Create a new project directory and navigate into it:
   ```bash
   mkdir python-data-analysis
   cd python-data-analysis
   ```
3. Initialize a new Git repository:
   ```bash
   git init
   ```

## Task 2: Laying the Project Foundation

Professional projects start with documentation and configuration.

1. **Create the README:** This file is the front page of your project.
   ```bash
   echo "# Python Data Analysis Project" > README.md
   ```
2. **Edit the README:** Open `README.md` in your text editor and add the following description:
   ```
   ## Project Description
   A script for analyzing and visualizing sales data from the Q1 2024 report.
   ```
3. **Create a requirements file:** This lists the project's external dependencies.
   ```bash
   echo "pandas==1.5.3" > requirements.txt
   ```
4. **Create a `.gitignore` file:** This prevents tracking of unnecessary or sensitive files.
   ```bash
   touch .gitignore
   ```
   Open `.gitignore` and add these lines:
   ```
   # Python
   __pycache__/
   *.pyc
   venv/
   env/

   # Data
   *.csv
   *.json
   ```

## Task 3: The Initial Commit

1. Check the status of your repository:
   ```bash
   git status
   ```
2. Stage the foundational files you created:
   ```bash
   git add README.md requirements.txt .gitignore
   ```
3. Commit these changes with a clear message:
   ```bash
   git commit -m "Initialize project with README, requirements, and gitignore"
   ```

## Task 4: Develop a Feature with a Proper Commit

Simulate adding the main functionality.

1. **Create the main script:**
   ```bash
   touch data_analysis.py
   ```
2. **Edit `data_analysis.py`:** Add the following code:
   ```python
   # Import necessary libraries
   import pandas as pd

   def lod_data(filepath):
       """Load sales data from a CSV file."""
       # Function stub - to be implemented
       pass

   if __name__ == "__main__":
       print("Data Analysis Script Initialized")
   ```
3. **Update project dependencies:** Add a visualization library to `requirements.txt`. The file should now contain:
   ```
   pandas==1.5.3
   matplotlib==3.7.0
   ```
4. **Make a professional commit:**
   - Stage the changes for the new feature:
     ```bash
     git add data_analysis.py requirements.txt
     ```
   - Open the editor to write a detailed commit message:
     ```bash
     git commit
     ```
   - **Write this message in the editor:**
     ```
     Add initial structure for data analysis script

     Create the main script data_analysis.py with a stub function for
     loading CSV data. Also add matplotlib to the project requirements
     for future data visualization tasks. This lays the groundwork for
     the core functionality of the application.
     ```
   - **Save and close the editor** (see table below for commands).

## Task 5: Review Your Work

View the history of your project to see the story you've built.

```bash
git log
```

For a condensed overview:

```bash
git log --oneline
```

## Bonus Challenge: The Hotfix

You've identified a typo in the function name that must be fixed.

1. **Open `data_analysis.py`** and change the function name from `lod_data` to `load_data`.
2. Stage the fixed file:
   ```bash
   git add data_analysis.py
   ```
3. Amend the previous commit to include this fix, keeping history clean:
   ```bash
   git commit --amend
   ```
   *(This will reopen the editor. You can update the commit message if needed, or just save and close to keep the original message.)*
4. Verify the fix is part of the previous commit by running `git log --oneline` again. You will see the commit hash has changed, confirming the history was rewritten.

## Commands to Save and Close the Editor

| Editor | Action | Command |
|--------|--------|---------|
| **Nano** (Common default) | Save | `Ctrl + O` (then press `Enter` to confirm filename) |
| | Exit | `Ctrl + X` |
| **Vim** / **Vi** | Enter Insert Mode (to type) | Press `i` |
| | Exit Insert Mode | Press `Esc` |
| | Save and Exit | Type `:wq` then press `Enter` |
| **VSCode** (if set as editor) | Save | `Ctrl + S` |
| | Close the window | `Ctrl + W` |

**Congratulations! You have successfully practiced a professional Git workflow.**