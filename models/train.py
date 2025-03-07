import json
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')

# Load dataset
with open("data/data.json", "r") as file:
    data = json.load(file)

# Extract patterns and corresponding labels
patterns = []
labels = []
classes = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern.lower())  # Convert to lowercase
        labels.append(intent["tag"])
    classes.append(intent["tag"])

# Text vectorization
vectorizer = CountVectorizer(tokenizer=word_tokenize)
X = vectorizer.fit_transform(patterns).toarray()

# Encode labels
encoder = LabelEncoder()
y = encoder.fit_transform(labels)

# Train classifier
classifier = MultinomialNB()
classifier.fit(X, y)

# Save model and encoders
with open("models/intent_model.pkl", "wb") as f:
    pickle.dump(classifier, f)

with open("models/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("models/label_encoder.pkl", "wb") as f:
    pickle.dump(encoder, f)

print("Model training complete. Files saved in ../models/")
