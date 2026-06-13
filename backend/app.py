from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

import os
import pdfplumber
import joblib

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# -----------------------------
# CORS
# -----------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# -----------------------------
# Load ML Models
# -----------------------------

model = joblib.load("resume_classifier.pkl")
vectorizer = joblib.load("tfidf.pkl")

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# -----------------------------
# Target Job Description
# -----------------------------

JOB_DESCRIPTION = """
Looking for a Machine Learning Engineer with
Python,
SQL,
Azure,
Docker,
FastAPI,
Git,
Machine Learning,
Deep Learning,
Data Analysis,
API Development.
"""

# -----------------------------
# Skills List
# -----------------------------

SKILLS = [
    "python",
    "java",
    "sql",
    "machine learning",
    "deep learning",
    "azure",
    "aws",
    "docker",
    "react",
    "fastapi",
    "git"
]

# -----------------------------
# API
# -----------------------------

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    try:

        # Create uploads folder
        os.makedirs("uploads", exist_ok=True)

        filepath = f"uploads/{file.filename}"

        # Save uploaded PDF
        with open(filepath, "wb") as f:
            f.write(await file.read())

        # -------------------------
        # Extract Resume Text
        # -------------------------

        text = ""

        with pdfplumber.open(filepath) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        # Handle empty PDF text
        if not text.strip():

            return {
                "error": "Unable to extract text from PDF. Please upload a text-based PDF."
            }

        text_lower = text.lower()

        # -------------------------
        # Skill Extraction
        # -------------------------

        found_skills = []

        for skill in SKILLS:

            if skill in text_lower:
                found_skills.append(skill)

        # -------------------------
        # ATS Score
        # -------------------------

        ats_score = round(
            (len(found_skills) / len(SKILLS)) * 100,
            2
        )

        # -------------------------
        # Suggestions
        # -------------------------

        suggestions = []

        for skill in SKILLS:

            if skill not in found_skills:

                suggestions.append(
                    f"Add {skill}"
                )

        # -------------------------
        # Resume Classification
        # -------------------------

        resume_vector = vectorizer.transform(
            [text]
        )

        predicted_role = model.predict(
            resume_vector
        )[0]

        # -------------------------
        # Job Description Matching
        # -------------------------

        resume_embedding = embedding_model.encode(
            [text]
        )

        jd_embedding = embedding_model.encode(
            [JOB_DESCRIPTION]
        )

        similarity = cosine_similarity(
            resume_embedding,
            jd_embedding
        )[0][0]

        job_match = float(
            round(
                similarity * 100,
                2
            )
        )

        # -------------------------
        # Response
        # -------------------------

        return {

            "ats_score": float(ats_score),

            "job_match": float(job_match),

            "predicted_role": str(predicted_role),

            "skills": found_skills,

            "suggestions": suggestions

        }

    except Exception as e:

        print("ERROR:", e)

        return {
            "error": str(e)
        }


# -----------------------------
# Health Check
# -----------------------------

@app.get("/")
def home():

    return {
        "message": "AI Resume Analyzer API Running"
    }