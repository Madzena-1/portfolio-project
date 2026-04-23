from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_job(text):
    text_lower = text.lower()

    # 🚨 STRONG SCAM SIGNALS (VERY IMPORTANT)
    strong_scam_keywords = [
        "no experience", "earn", "weekly", "urgent",
        "work from home", "quick money", "whatsapp",
        "easy money", "limited slots", "click here"
    ]

    weak_or_empty_job = len(text_lower.split()) < 3

    keyword_hits = [word for word in strong_scam_keywords if word in text_lower]

    ai_result = classifier(text)[0]
    ai_score = ai_result["score"]

    # 🚨 FINAL DECISION LOGIC (RULES FIRST)
    if weak_or_empty_job:
        decision = "⚠️ Suspicious Job (Too vague)"
        confidence = 0.95

    elif len(keyword_hits) >= 1:
        decision = "⚠️ Suspicious Job (Scam signals detected)"
        confidence = 0.90

    elif ai_score < 0.6:
        decision = "⚠️ Suspicious Job"
        confidence = ai_score

    else:
        decision = "❌ Not enough info / likely fake listing"
        confidence = ai_score

    return {
        "decision": decision,
        "confidence": round(confidence, 2),
        "matched_keywords": keyword_hits
    }
