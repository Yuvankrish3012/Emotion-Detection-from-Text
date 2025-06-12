import streamlit as st
import pickle
import re

# Full paths for loading saved files
model_path = r"D:\ML PROJECTS\Emotion Detection from Text\emotion_model.pkl"
vectorizer_path = r"D:\ML PROJECTS\Emotion Detection from Text\emotion_vectorizer.pkl"
label_encoder_path = r"D:\ML PROJECTS\Emotion Detection from Text\emotion_label_encoder.pkl"

# Load model and transformers
model = pickle.load(open(model_path, "rb"))
tfidf = pickle.load(open(vectorizer_path, "rb"))
label_encoder = pickle.load(open(label_encoder_path, "rb"))

# Text cleaner
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# Streamlit UI
st.set_page_config(page_title="Emotion Detection", layout="centered")
st.title("🧠 Emotion Detection from Text")
st.write("Enter a sentence and the model will predict the emotional tone.")

# Input
user_input = st.text_area("✏️ Enter your sentence here", "")

if st.button("🔍 Detect Emotion"):
    if user_input.strip() == "":
        st.warning("Please enter a valid sentence.")
    else:
        cleaned = clean_text(user_input)
        vectorized = tfidf.transform([cleaned])
        pred = model.predict(vectorized)[0]
        predicted_emotion = label_encoder.inverse_transform([pred])[0]
        st.success(f"✅ **Predicted Emotion:** `{predicted_emotion.upper()}`")
