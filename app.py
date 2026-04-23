import streamlit as st
import json
from filter import analyze_job

st.title("💼 AI Job Search Tool")

job_text = st.text_area("Enter job description")
job_title = st.text_input("Job Title")

if "jobs" not in st.session_state:
    st.session_state.jobs = []

if st.button("Analyse & Release Job"):
    if job_text.strip() == "":
        st.warning("Please enter a job description")
    else:
        result = analyze_job(job_text)

        st.write("Decision:", result["decision"])
        st.write("Confidence:", result["confidence"])

        # 🚀 ONLY RELEASE IF LEGIT
        if "Likely Legit" in result["decision"]:
            job = {
                "title": job_title,
                "description": job_text
            }

            st.session_state.jobs.append(job)
            st.success("✅ Job released to listings!")

st.subheader("📢 Active Jobs")

for job in st.session_state.jobs:
    st.write("**Title:**", job["title"])
    st.write(job["description"])
    st.write("---")
