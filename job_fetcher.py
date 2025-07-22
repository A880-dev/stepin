# job_fetcher.py

import requests

def fetch_jobs(title, location):
    url = f"https://remotive.io/api/remote-jobs?search={title}"
    response = requests.get(url)

    if response.status_code == 200:
        jobs = response.json().get("jobs", [])
        # Optional filtering by location (Remotive has 'candidate_required_location' field)
        if location:
            jobs = [job for job in jobs if location.lower() in job.get("candidate_required_location", "").lower()]
        return jobs
    else:
        return []
