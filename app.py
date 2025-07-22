import streamlit as st
import urllib.parse
import random

st.set_page_config(page_title="JobSketcher 2.0", layout="centered")

st.title("🎯 JobSketcher 2.0")
st.write("Helping students explore internships + generate SOPs with ✨ no APIs ✨")

# Step 1: Collect user input
role = st.text_input("Desired Role", "Data Analyst Intern")
location = st.text_input("Preferred Location", "India")
skills = st.text_area("Your Key Skills", "Excel, SQL, Python, Communication")
goals = st.text_area("Your Career Goals", "To gain practical experience in data analysis")

# Step 2: Create job search links
def build_links(role, location):
    query = f"{role} internships in {location}"
    encoded = urllib.parse.quote(query)
    return {
        "LinkedIn": f"https://www.linkedin.com/jobs/search/?keywords={encoded}",
        "Internshala": f"https://internshala.com/internships/keywords-{encoded}",
        "Naukri": f"https://www.naukri.com/{encoded}-jobs",
        "Google Jobs": f"https://www.google.com/search?q={encoded}+jobs",
        "Glassdoor": f"https://www.glassdoor.co.in/Job/jobs.htm?sc.keyword={encoded}"
    }

if st.button("🔍 Show Matching Jobs"):
    links = build_links(role, location)
    st.subheader("🔗 Job Listings")
    for name, link in links.items():
        st.markdown(f"- [{name}]({link})")

# Step 3: SOP Generator
def generate_sop(role, skills, goals):
    templates = [
        f"I am excited to apply for the {role} position. With my skills in {skills}, I aim to contribute effectively to your team and further my goal of {goals}.",
        f"As a passionate learner, I seek the {role} internship to apply my skills in {skills} and grow toward my long-term aspiration of {goals}.",
        f"The opportunity to work as a {role} aligns with my background in {skills}, and I am eager to translate theory into practice while progressing toward {goals}."
    ]
    return random.choice(templates)

if st.button("📝 Generate SOP"):
    sop = generate_sop(role, skills, goals)
    st.subheader("📄 SOP Suggestion")
    st.code(sop, language='markdown')

