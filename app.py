import streamlit as st
from job_fetcher import fetch_jobs

st.title("🔍 Step-In: Internship Finder")

role = st.text_input("Enter internship role:")
location = st.text_input("Enter preferred location (e.g., India, Remote):")

if st.button("Search Internships"):
    with st.spinner("Finding internships..."):
        results = fetch_jobs(role, location)

        if results:
            for job in results:
                st.subheader(job['title'])
                st.write(f"📍 Company: {job['company_name']}")
                st.write(f"🌍 Location: {job['candidate_required_location']}")
                st.write(f"🔗 [Apply Now]({job['url']})")
                st.markdown("---")
        else:
            st.warning("No internships found. Try different keywords or broader location like 'remote'.")


