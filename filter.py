from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_job(text):
    result = classifier(text)[0]

    score = result["score"]

    suspicious_keywords = [
        "earn", "weekly", "no experience", "urgent",
        "work from home", "whatsapp", "quick money"
    ]

    text_lower = text.lower()
    keyword_flag = any(word in text_lower for word in suspicious_keywords)

    if keyword_flag or score < 0.7:
        decision = "REJECT"
    else:
        decision = "APPROVE"

    return {
        "decision": decision,
        "confidence": round(score, 2)
    }
