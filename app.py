import streamlit as st
from filter import analyze_job

st.set_page_config(page_title="AI Job Finder", page_icon="💼")

st.title("💼 AI Job Search Tool")

st.write("Paste a job description below:")

job_text = st.text_area("Job Description")

if st.button("Analyse Job"):
    if job_text.strip() == "":
        st.warning("Please enter a job description")
    else:
        result = analyze_job(job_text)

        st.subheader("Result")
        st.write("Decision:", result["decision"])
        st.write("Confidence:", result["confidence"])
