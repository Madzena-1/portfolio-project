import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline(
        "text-classification",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

def analyze_job(text):
    classifier = load_model()
    result = classifier(text)[0]

    label = result["label"]
    score = result["score"]

    if score < 0.70:
        decision = "⚠️ Suspicious Job"
    else:
        decision = "✅ Likely Legit Job"

    return {
        "label": label,
        "confidence": round(score, 2),
        "decision": decision
    }
