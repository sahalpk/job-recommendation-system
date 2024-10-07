from pymongo import MongoClient
import pymongo

from models.jobs import Job
from models.user import User

# utils/database.py
# utils/database.py
import pymongo

class Database:
    def __init__(self, db_name, collection_name):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]
        self.jobs_collection = self.db[collection_name]
        self.users_collection = self.db["users"]

    def get_all_jobs(self):
        jobs = []
        for job in self.jobs_collection.find():
            try:
                salary_range = job['salary_range']
            except KeyError:
                salary_range = [0, 0]
            jobs.append(Job(
                _id=job['_id'],
                job_id=job['job_id'],
                job_title=job['job_title'],
                company=job['company'],
                required_skills=job['required_skills'],
                location=job['location'],
                job_type=job['job_type'],
                experience_level=job['experience_level'],
                salary_range=salary_range
            ))
        return jobs

    def get_all_users(self):
        users = []
        for user in self.users_collection.find():
            users.append({
                '_id': user['_id'],
                'name': user['name'],
                'skills': user['skills'],
                'experience_level': user['experience_level'],
                'preferences': user['preferences']
            })
        return users

    def insert_job(self, job):
        try:
            self.jobs_collection.insert_one({
                "_id": job["_id"],
                "job_id": job["job_id"],
                "job_title": job["job_title"],
                "company": job["company"],
                "required_skills": job["required_skills"],
                "location": job["location"],
                "job_type": job["job_type"],
                "experience_level": job["experience_level"],
                "salary_range": job["salary_range"]
            })
            return True
        except pymongo.errors.DuplicateKeyError:
            print("Job with _id {} already exists in the database.".format(job["_id"]))
            return False
        except Exception as e:
            print("Error adding job: {}".format(e))
            return False
        
    def insert_user(self, user):
        try:
            self.users_collection.insert_one({
                '_id': user['_id'],
                'name': user['name'],
                'skills': user['skills'],
                'experience_level': user['experience_level'],
                'preferences': user['preferences']
            })
        except pymongo.errors.DuplicateKeyError:
            print("User  with _id {} already exists in the database.".format(user['_id']))

    def update_jobs(self):
        for job in self.jobs_collection.find():
            self.jobs_collection.update_one({'_id': job['_id']}, {'$set': {'salary_range': [50000, 100000]}})