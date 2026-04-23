from datetime import datetime

def filter_active_jobs(jobs):
    active_jobs = []
    today = datetime.today()

    for job in jobs:
        expiry = datetime.strptime(job["expiry_date"], "%Y-%m-%d")
        if expiry >= today:
            active_jobs.append(job)

    return active_jobs
