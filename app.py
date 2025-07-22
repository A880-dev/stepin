import streamlit as st
from job_fetcher import fetch_jobs
from sop_generator import generate_sop  # Assuming you have this from earlier
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="StepIn - Internship Launcher", layout="centered")

# ------------------ UI TITLE ------------------ #
st.title("🚀 StepIn: Your Internship Launcher")
st.markdown("Craft your SOP and find matching internships all in one place.")

# ------------------ SOP GENERATION ------------------ #
st.header("📝 SOP Generator")
name = st.text_input("Your Name")
background = st.text_area("Academic Background")
interests = st.text_area("Your Interests")
skills = st.text_area("Key Skills (comma-separated)")
goal = st.text_area("Why do you want this internship?")
company = st.text_input("Target Company Name")

if st.button("Generate SOP"):
    if all([name, background, interests, skills, goal, company]):
        with st.spinner("Generating SOP..."):
            sop = generate_sop(name, background, interests, skills, goal, company)
            st.success("✅ SOP Generated!")
            st.text_area("Your SOP", sop, height=300)
    else:
        st.warning("Please fill all the fields to generate SOP.")

# ------------------ INTERNSHIP FINDER ------------------ #
st.header("🔍 Find Matching Internships")

job_query = st.text_input("Internship Role (e.g., Data Analyst Intern)", value="data analyst intern")
location = st.text_input("Location", value="India")

if st.button("Search Internships"):
    with st.spinner("Fetching opportunities..."):
        jobs = fetch_jobs(job_query, location)
        if jobs:
            for job in jobs[:5]:
                st.markdown(f"### 📌 {job.get('job_title')}")
                st.markdown(f"**🏢 Company**: {job.get('employer_name')}")
                st.markdown(f"**🌍 Location**: {job.get('job_city', '')}, {job.get('job_country', '')}")
                st.markdown(f"**📋 Type**: {job.get('job_employment_type', 'Not specified')}")
                st.markdown(f"**🔗 [Apply Here]({job.get('job_apply_link')})**")
                st.markdown("---")
        else:
            st.error("No matching internships found. Try a different keyword or location.")

# ------------------ Footer ------------------ #
st.markdown("---")
st.markdown("Made with ❤️ by StepIn Team")
