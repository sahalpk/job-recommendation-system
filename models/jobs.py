# models/jobs.py
from bson import ObjectId

class Job:
    def __init__(self, _id, job_id, job_title, company, required_skills, location, job_type, experience_level, salary_range):
        self._id = _id
        self.job_id = job_id
        self.job_title = job_title
        self.company = company
        self.required_skills = required_skills
        self.location = location
        self.job_type = job_type
        self.experience_level = experience_level
        self.salary_range = salary_range

    def to_dict(self):
        return {
            '_id': self._id,
            'job_id': self.job_id,
            'job_title': self.job_title,
            'company': self.company,
            'required_skills': self.required_skills,
            'location': self.location,
            'job_type': self.job_type,
            'experience_level': self.experience_level,
            'salary_range': self.salary_range
        }