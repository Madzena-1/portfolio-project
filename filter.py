from datetime import datetime

def filter_active_jobs(jobs):
    active_jobs = []
    today = datetime.today()

    for job in jobs:
        expiry = datetime.strptime(job["expiry_date"], "%Y-%m-%d")
        if expiry >= today:
            active_jobs.append(job)

    return active_jobs
    from datetime import datetime
from transformers import pipeline

# Load AI model once
job_classifier = pipeline("text-classification")

def is_job_legit(job):
    text = job["title"] + " " + job["company"]

    result = job_classifier(text)[0]

    # Very simple rule (we refine later)
    if result["score"] > 0.5:
        return True
    return False


def filter_active_jobs(jobs):
    active_jobs = []
    today = datetime.today()

    for job in jobs:
        expiry = datetime.strptime(job["expiry_date"], "%Y-%m-%d")

        if expiry >= today and is_job_legit(job):
            active_jobs.append(job)

    return active_jobs
