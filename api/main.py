from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

# Load trained models
with open("../models/intent_model.pkl", "rb") as f:
    intent_vectorizer, intent_model = pickle.load(f)

with open("../models/sentiment_model.pkl", "rb") as f:
    sentiment_vectorizer, sentiment_model = pickle.load(f)

# Process user input
class RequestData(BaseModel):
    message: str

@app.post("/analyze")
def analyze_text(data: RequestData):
    # Predict intent
    X_intent = intent_vectorizer.transform([data.message])
    intent = intent_model.predict(X_intent)[0]

    # Predict sentiment
    X_sentiment = sentiment_vectorizer.transform([data.message])
    sentiment = sentiment_model.predict(X_sentiment)[0]

    return {"intent": intent, "sentiment": sentiment}

@app.get("/")
def root():
    return {"message": "NLU API is running!"}
