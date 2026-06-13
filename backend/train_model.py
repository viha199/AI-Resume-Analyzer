import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv(
    "../dataset/resume_dataset.csv"
)

X = df["Resume"]
y = df["Category"]

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=5000
)

X_vectorized = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

accuracy = model.score(
    X_test,
    y_test
)

print(
    f"Accuracy: {accuracy:.2f}"
)

joblib.dump(
    model,
    "resume_classifier.pkl"
)

joblib.dump(
    vectorizer,
    "tfidf.pkl"
)