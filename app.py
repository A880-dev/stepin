import streamlit as st
from job_fetcher import fetch_jobs  # This should be defined in job_fetcher.py

# Streamlit page settings
st.set_page_config(page_title="Stepin – Internship Finder", layout="wide")

# App title
st.title("🚀 Stepin – Your Personalized Internship Finder")

# Input fields
job_title = st.text_input("🎯 Enter Internship Role (e.g., Data Analyst Intern)")
location = st.text_input("🌍 Enter Preferred Location (e.g., India, Remote)")

# Search button
if st.button("🔎 Search Opportunities"):
    if job_title:
        with st.spinner("Looking for matching internships..."):
            jobs = fetch_jobs(job_title, location)
            if jobs:
                st.success(f"✅ Found {len(jobs)} matching internships!")
                for job in jobs[:10]:  # Show top 10 jobs
                    st.markdown(f"### [{job['title']}]({job['url']})")
                    st.write(f"**Company:** {job['company_name']}")
                    st.write(f"**Location:** {job['candidate_required_location']}")
                    st.write(f"**Type:** {job.get('job_type', 'Not specified')}")
                    st.write(f"**Description:** {job['description'][:250]}...")  # Trimmed for display
                    st.markdown("---")
            else:
                st.warning("❌ No internships found for this search.")
    else:
        st.warning("⚠️ Please enter at least a job title.")

