# job_fetcher.py

import requests

def fetch_jobs(role, location):
    try:
        # Step 1: Call Remotive API
        url = f"https://remotive.io/api/remote-jobs?search={role}"
        response = requests.get(url)
        response.raise_for_status()  # Ensure HTTP error throws exception

        data = response.json()
        jobs = data.get("jobs", [])

        # Step 2: Smart Filtering
        location = location.strip().lower()
        filtered_jobs = []

        for job in jobs:
            loc = job.get("candidate_required_location", "").lower()

            # If location matches or location is 'anywhere' or 'remote', include
            if location in loc or loc in location or 'anywhere' in loc or 'remote' in loc:
                filtered_jobs.append(job)

        # Step 3: Return top 10 results
        return filtered_jobs[:10]

    except Exception as e:
        print(f"❌ Error while fetching jobs: {e}")
        return []

