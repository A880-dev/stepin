import pandas as pd

applications = []

def add_application(company, role, date_applied, status):
    applications.append({
        "Company": company,
        "Role": role,
        "Date Applied": date_applied,
        "Status": status
    })

def get_applications_df():
    return pd.DataFrame(applications)
