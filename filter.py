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

    score = result["score"]

    # 🚨 RULE-BASED SCAM DETECTION
    suspicious_keywords = [
        "earn", "weekly", "no experience", "work from home",
        "urgent", "limited spots", "click here", "whatsapp"
    ]

    text_lower = text.lower()

    keyword_flag = any(word in text_lower for word in suspicious_keywords)

    # 🔥 FINAL DECISION LOGIC
    if keyword_flag:
        decision = "⚠️ Suspicious Job"
    elif score < 0.7:
        decision = "⚠️ Suspicious Job"
    else:
        decision = "✅ Likely Legit Job"

    return {
        "confidence": round(score, 2),
        "decision": decision
    }
