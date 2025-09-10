# Lab: Collaborative Machine Learning Project with Git

## Objective

This lab is designed to teach you how to collaboratively build and execute a machine learning pipeline while adhering to Git best practices. You will work in pairs, taking on distinct roles, to preprocess data, train a machine learning model, and evaluate it. The lab emphasizes teamwork, division of responsibilities, and proper use of Git for version control and collaboration.

## Learning Outcomes

By the end of this lab, you will:

1. Understand how to collaboratively use Git and GitHub for project development.
2. Develop a machine learning pipeline that includes data preprocessing, model training, and model evaluation.
3. Learn to manage feature branches, commit descriptive changes, and create pull requests for collaborative workflows.
4. Gain experience in dividing tasks and responsibilities effectively.

## Roles and Responsibilities

You will work in pairs, with each of you assigned a specific role:

- **Student A: Data Preprocessing**
  - Responsible for preparing the dataset for modeling.
  - Writes the script `preprocessing.py`.
  - Ensures that large files (e.g., `cleaned_data.csv`) are excluded from the repository by using `.gitignore`.

- **Student B: Model Training and Evaluation**
  - Responsible for training the machine learning model (`training.py`) and evaluating its performance (`evaluation.py`).
  - Pushes model files and evaluation results, excluding unnecessary large files from the repository.

## Git Workflow Overview

- **Create and Clone the Repository**: Student A will create a new repository on their GitHub account and initialize it with the basic structure (see Expected Repository Structure below). Then, clone it locally. Add Student B as a collaborator via GitHub settings > Collaborators.
- **Feature Branches**: Always create a separate branch for each feature or task. Do not work directly on the main branch.
- **Descriptive Commits**: Commit changes frequently with clear and descriptive messages.
- **Pull Requests (PRs)**: Use PRs to propose changes from your feature branch to the main branch.
- **.gitignore Usage**: Ensure that large files (e.g., datasets, models) are excluded from the repository.

## Expected Repository Structure

After initialization by Student A, the repository should look like this:

```
.
├── .gitignore
├── README.md
├── requirements.txt
├── preprocessing.py
├── training.py
└── evaluation.py
```

- **.gitignore**: Add entries like `*.csv`, `*.pkl`, `*.png` to exclude large or generated files.
- **README.md**: A basic file describing the project.
- **requirements.txt**: List dependencies like `pandas`, `scikit-learn`, `joblib`, `seaborn`, `matplotlib`.
- Python scripts can start as empty files or with basic skeletons.

## Lab Instructions

### 1. Repository Setup

1. **Create the Repository**
   - Student A: Create a new repository (e.g., "Collaborative-ML-Project").
   - Initialize it with `README.md`, `.gitignore` (Python template), and add empty files for `preprocessing.py`, `training.py`, and `evaluation.py`.
   - Share the repository link with Student B and add them as a collaborator.

2. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

3. **Pull Latest Changes**
   ```bash
   git pull origin main
   ```

### 2. Create Feature Branches

Student A:
```bash
git checkout -b feature/data-preprocessing
```

Student B:
```bash
git checkout -b feature/model-training-evaluation
```

### 3. Write and Test the Code

#### Student A: Data Preprocessing (`preprocessing.py`)

```python
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

def load_data():
    iris = load_iris()
    data = pd.DataFrame(iris.data, columns=iris.feature_names)
    data['target'] = iris.target
    return data

def preprocess_data(data):
    data['sepal_petal_ratio'] = data['sepal length (cm)'] / data['petal length (cm)']
    scaler = StandardScaler()
    features = data.drop(columns=['target', 'sepal_petal_ratio'])
    data[features.columns] = scaler.fit_transform(features)
    data['target'] = data['target'].astype(int)
    return data

if __name__ == "__main__":
    data = load_data()
    data = preprocess_data(data)
    data.to_csv("cleaned_data.csv", index=False)
    print("Preprocessed data saved as 'cleaned_data.csv'.")
```

Test:
```bash
python preprocessing.py
```

Commit:
```bash
git add preprocessing.py
git commit -m "Added data preprocessing script"
git push origin feature/data-preprocessing
```

#### Student B: Model Training (`training.py`)

```python
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from preprocessing import load_data, preprocess_data

def train_model(data):
    X = data.drop("target", axis=1)
    y = data["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=150, max_depth=10, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, "iris_model.pkl")
    print("Model saved as 'iris_model.pkl'.")
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Accuracy: {accuracy:.2f}")
    return model

if __name__ == "__main__":
    data = load_data()
    data = preprocess_data(data)
    model = train_model(data)
```

Test:
```bash
python training.py
```

Commit:
```bash
git add training.py
git commit -m "Added model training script"
git push origin feature/model-training-evaluation
```

#### Student B: Model Evaluation (`evaluation.py`)

```python
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
import pandas as pd
import joblib
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import time

def evaluate_model(model, data):
    X = data.drop("target", axis=1)
    y = data["target"]
    predictions = model.predict(X)
    acc = accuracy_score(y, predictions)
    f1 = f1_score(y, predictions, average='weighted')
    cm = confusion_matrix(y, predictions)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, cmap='Blues', fmt='d')
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    filename = f'confusion_matrix_{int(time.time())}.png'
    plt.savefig(filename)
    plt.close()
    return acc, f1

if __name__ == "__main__":
    data = pd.read_csv("cleaned_data.csv")
    model = joblib.load("iris_model.pkl")
    acc, f1 = evaluate_model(model, data)
    print(f"Accuracy: {acc:.2f}")
    print(f"F1-Score: {f1:.2f}")
```

Test:
```bash
python evaluation.py
```

Commit:
```bash
git add evaluation.py
git commit -m "Added model evaluation script"
git push origin feature/model-training-evaluation
```

### 4. Create and Review Pull Requests

- Open PRs from your feature branches to `main`.
- Review each other's code, test locally, and provide feedback.
- Merge only after testing.

### 5. Run the Full Pipeline

```bash
python preprocessing.py
python training.py
python evaluation.py
```

## Submission Instructions

- Ensure all changes are merged into `main`.
- Submit the GitHub repository link.

## Evaluation Criteria

1. Proper use of Git workflow (feature branches, PRs, commits).
2. Functionality and correctness of scripts.
3. Effective teamwork and division of responsibilities.

