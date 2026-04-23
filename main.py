import json
from filter import filter_active_jobs

# Load jobs
with open("jobs.json", "r") as file:
    jobs = json.load(file)

# Filter jobs
active_jobs = filter_active_jobs(jobs)

# Display results
print("Active Job Listings:\n")

for job in active_jobs:
    print(f"{job['title']} at {job['company']} (Expires: {job['expiry_date']})")
