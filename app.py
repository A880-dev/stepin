import streamlit as st
from sop_generator import generate_sop
from application_tracker import add_application, get_applications_df

st.set_page_config(page_title="StepIn: Internship Assistant", layout="wide")

st.title("🚀 StepIn - Your Internship Buddy")

tab1, tab2 = st.tabs(["✍️ SOP Generator", "📋 Application Tracker"])

with tab1:
    st.subheader("Generate Your SOP")

    name = st.text_input("Your Name")
    background = st.text_area("Academic Background / Skills")
    internship = st.text_input("Internship Role / Company")
    motivation = st.text_area("Why do you want this internship?")
    
    if st.button("Generate SOP"):
        if name and background and internship and motivation:
            prompt = f"Write a Statement of Purpose for {name}, who is applying to a {internship} internship. Background: {background}. Motivation: {motivation}."
            sop = generate_sop(prompt)
            st.success("Here is your SOP:")
            st.text_area("Generated SOP", sop, height=300)
        else:
            st.warning("Please fill in all fields.")

with tab2:
    st.subheader("Track Your Applications")
    
    with st.form("app_form"):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            company = st.text_input("Company")
        with col2:
            role = st.text_input("Role")
        with col3:
            date_applied = st.date_input("Date Applied")
        with col4:
            status = st.selectbox("Status", ["Applied", "Interviewed", "Offered", "Rejected"])

        submitted = st.form_submit_button("Add Application")
        if submitted and company and role:
            add_application(company, role, date_applied, status)
            st.success("Application Added!")

    st.dataframe(get_applications_df())
