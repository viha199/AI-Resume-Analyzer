# AI Resume Analyzer

## Overview

AI Resume Analyzer is a Machine Learning and NLP-based web application that analyzes resumes and provides insights such as ATS score, predicted job role, job description match score, detected skills, and improvement suggestions.

The project combines traditional Machine Learning techniques with modern Natural Language Processing (NLP) models to evaluate resumes against a target job profile.

---

## Features

### Resume Upload

* Upload resumes in PDF format.
* Automatically extract text from uploaded resumes.

### ATS Score Calculation

* Identifies relevant technical skills from the resume.
* Calculates an ATS (Applicant Tracking System) score based on the presence of desired skills.

### Resume Classification (Machine Learning)

* Uses a trained Random Forest Classifier.
* Predicts the most suitable job role based on resume content.
* Examples:

  * Data Science
  * Java Developer
  * Frontend Developer
  * DevOps Engineer

### Job Description Matching (NLP)

* Compares the resume with a target job description.
* Uses Sentence Transformers to generate semantic embeddings.
* Calculates a Job Match Score using Cosine Similarity.

### Skill Detection

* Detects technical skills such as:

  * Python
  * SQL
  * Azure
  * AWS
  * Docker
  * FastAPI
  * Git
  * Machine Learning
  * Deep Learning
  * React

### Improvement Suggestions

* Recommends missing skills to improve resume quality and job compatibility.

---

## Technology Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* FastAPI
* Python

### Machine Learning

* Scikit-Learn
* Random Forest Classifier
* TF-IDF Vectorizer

### NLP

* Sentence Transformers
* all-MiniLM-L6-v2
* Cosine Similarity

### PDF Processing

* pdfplumber

---

## Project Architecture

```text
Resume PDF
     |
     v
PDF Text Extraction
     |
     v
+-------------------------+
| Skill Extraction        |
| ATS Score Calculation   |
+-------------------------+
     |
     v
TF-IDF Vectorization
     |
     v
Random Forest Classifier
     |
     v
Predicted Job Role

Resume Text
     |
     v
Sentence Transformer
     |
     v
Embedding Generation
     |
     v
Cosine Similarity
     |
     v
Job Match Score
```

---

## Machine Learning Workflow

### Training Phase

1. Resume dataset is loaded.
2. Resume text is converted into numerical vectors using TF-IDF.
3. A Random Forest Classifier is trained on labeled resume categories.
4. The trained model and vectorizer are saved as:

```text
resume_classifier.pkl
tfidf.pkl
```

### Prediction Phase

1. User uploads a resume.
2. Resume text is extracted.
3. TF-IDF converts text into numerical features.
4. Random Forest predicts the job role.
5. Sentence Transformer calculates semantic similarity with the target job description.
6. ATS score and recommendations are generated.

---

## Dataset

https://www.kaggle.com/datasets/muqaddasejaz/resume-cv-skills-extraction-dataset?utm_source=chatgpt.com

Expected columns:

```text
Category
Resume
```

Example categories:

* Data Science
* Java Developer
* HR
* Testing
* DevOps Engineer
* Frontend Developer
* Backend Developer

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/AI-Resume-Analyzer.git

cd AI-Resume-Analyzer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install fastapi
pip install uvicorn
pip install pdfplumber
pip install python-multipart
pip install pandas
pip install scikit-learn
pip install sentence-transformers
pip install joblib
```

---

## Train the Model

Place the dataset inside:

```text
dataset/
    resume_dataset.csv
```

Run:

```bash
python train_model.py
```

This generates:

```text
resume_classifier.pkl
tfidf.pkl
```

---

## Run Backend

```bash
uvicorn app:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

## Run Frontend

Navigate to frontend folder:

```bash
python -m http.server 5500
```

Open:

```text
http://localhost:5500
```

---

## Sample Output

### ATS Score

```text
45.45%
```

### Predicted Role

```text
Data Science
```

### Job Match Score

```text
37.23%
```

### Skills Found

```text
Python
SQL
Machine Learning
Azure
AWS
```

### Suggestions

```text
Add Docker
Add FastAPI
Add Git
```

---

## Future Enhancements

* Support DOCX resumes.
* Resume ranking against multiple job descriptions.
* Skill gap analysis dashboard.
* Resume summary generation using Generative AI.
* Interview question recommendation based on resume.
* Candidate shortlisting system.
* Cloud deployment using Azure or AWS.

---

## Learning Outcomes

This project helped in understanding:

* FastAPI backend development
* Resume text extraction
* TF-IDF feature engineering
* Random Forest Classification
* Natural Language Processing
* Sentence Transformers
* Cosine Similarity
* Machine Learning model deployment
* Frontend-backend integration

---

## Author

Viha Dave

Technical Trainer | Machine Learning Enthusiast | Cloud & AI Educator
