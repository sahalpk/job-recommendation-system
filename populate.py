# populate_db.py
import random
import requests

# Define a list of job titles, companies, locations, job types, experience levels, and salary ranges
job_titles = ["Software Engineer", "Data Scientist", "DevOps Engineer", "Product Manager", "UX Designer", "Cybersecurity Engineer", "Data Analyst", "Full Stack Developer", "Artificial Intelligence Engineer", "Cloud Engineer", "Network Engineer"]
companies = ["ABC Corporation", "XYZ Inc.", "DEF Startups", "GHI Ventures", "JKL Design", "MNO Security", "PQR Analytics", "STU Development", "VWX AI", "YZA Cloud", "BCD Networks"]
locations = ["New York", "San Francisco", "Seattle", "Los Angeles", "Chicago", "Washington D.C.", "Boston", "Austin", "San Jose", "Denver", "Dallas"]
job_types = ["Full-time", "Part-time", "Internship", "Contract"]
experience_levels = ["Junior", "Mid-level", "Senior"]
salary_ranges = [(50000, 80000), (80000, 120000), (120000, 180000), (180000, 250000)]

# Define the API endpoint URL
api_endpoint = "http://127.0.0.1:5000/jobs"

# Create a list to store the job samples
job_samples = []

# Generate 500 job samples
for i in range(500):
    job_id = f"J{i+1}"
    job_title = random.choice(job_titles)
    company = random.choice(companies)
    location = random.choice(locations)
    job_type = random.choice(job_types)
    experience_level = random.choice(experience_levels)
    salary_range = random.choice(salary_ranges)
    required_skills = [f"Skill {i+1}", f"Skill {i+2}", f"Skill {i+3}"]

    job_sample = {
        "_id": i+1,
        "job_id": job_id,
        "job_title": job_title,
        "company": company,
        "required_skills": required_skills,
        "location": location,
        "job_type": job_type,
        "experience_level": experience_level,
        "salary_range": salary_range
    }

    job_samples.append(job_sample)

# Send a POST request to the API endpoint for each job sample
# populate_db.py
for job_sample in job_samples:
    response = requests.post(api_endpoint, json=job_sample)

    # Check if the request was successful
    if response.status_code == 201:
        print("Job sample {} added successfully".format(job_sample["job_id"]))
    else:
        print("Error adding job sample {}: {}".format(job_sample["job_id"], response.text))