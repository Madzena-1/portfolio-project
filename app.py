import streamlit as st
import json
from filter import analyze_job

st.set_page_config(page_title="Job Platform", page_icon="💼")

st.title("💼 AI Job Platform")

# Load jobs
def load_jobs():
    try:
        with open("jobs.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_job(job):
    jobs = load_jobs()
    jobs.append(job)

    with open("jobs.json", "w") as f:
        json.dump(jobs, f, indent=2)

# INPUT FORM
title = st.text_input("Job Title")
description = st.text_area("Job Description")

if st.button("Submit Job"):
    if title and description:
        result = analyze_job(description)

        st.write("AI Decision:", result["decision"])
        st.write("Confidence:", result["confidence"])

        if result["decision"] == "APPROVE":
            job = {
                "title": title,
                "description": description
            }

            save_job(job)
            st.success("✅ Job published successfully!")
        else:
            st.error("❌ Job rejected by AI filter")

# DISPLAY JOBS
st.subheader("📢 Active Job Listings")

jobs = load_jobs()

if len(jobs) == 0:
    st.info("No jobs available yet.")
else:
    for job in jobs:
        st.markdown("### " + job["title"])
        st.write(job["description"])
        st.write("---")
