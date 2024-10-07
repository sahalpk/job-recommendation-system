class RecommendationAlgorithm:
    def __init__(self, jobs=None, users=None):
        self.jobs = jobs if jobs is not None else []
        self.users = users if users is not None else []

    def add_job(self, job):
        self.jobs.append(job)

    def add_user(self, user):
        self.users.append(user)

    def filter_jobs(self, user):
        filtered_jobs = []
        for job in self.jobs:
            if (self.match_skill(job, user) and 
                self.match_experience(job, user) and 
                self.match_location(job, user) and 
                self.match_salary(job, user)):
                filtered_jobs.append(job)
        return filtered_jobs

    def match_skill(self, job, user):
        required_skills = job.required_skills
        user_skills = user.skills
        matched_skills = [skill for skill in required_skills if skill in user_skills]
        return len(matched_skills) / len(required_skills) >= 0.6

    def match_experience(self, job, user):
        required_experience = job.experience_level
        user_experience = user.experience_level
        return user_experience >= required_experience

    def match_location(self, job, user):
        job_location = job.location
        user_location = user.preferences['location']
        return job_location == user_location

    def match_salary(self, job, user):
        job_salary = job.salary_range
        user_salary = user.preferences['salary']
        return job_salary[0] <= user_salary <= job_salary[1]

    def score_jobs(self, user, jobs):
        scored_jobs = []
        for job in jobs:
            score = self.calculate_score(job, user)
            scored_jobs.append((job, score))
        return scored_jobs

    def calculate_score(self, job, user):
        skill_match_score = self.calculate_skill_match_score(job, user)
        experience_score = self.calculate_experience_score(job, user)
        location_score = self.calculate_location_score(job, user)
        salary_score = self.calculate_salary_score(job, user)
        # Weighted score calculation
        return (skill_match_score * 0.5) + (experience_score * 0.2) + (location_score * 0.2) + (salary_score * 0.1)

    def calculate_skill_match_score(self, job, user):
        required_skills = job.required_skills
        user_skills = user.skills
        matched_skills = [skill for skill in required_skills if skill in user_skills]
        return len(matched_skills) / len(required_skills)

    def calculate_experience_score(self, job, user):
        required_experience = job.experience_level
        user_experience = user.experience_level
        return 1 if user_experience >= required_experience else 0

    def calculate_location_score(self, job, user):
        job_location = job.location
        user_location = user.preferences['location']
        return 1 if job_location == user_location else 0

    def calculate_salary_score(self, job, user):
        job_salary = job.salary_range
        user_salary = user.preferences['salary']
        return 1 if job_salary[0] <= user_salary <= job_salary[1] else 0

    def rank_jobs(self, scored_jobs):
        # Rank the jobs based on their score in descending order
        return sorted(scored_jobs, key=lambda x: x[1], reverse=True)

    def recommend(self, user):
        # Step 1: Filter jobs based on user preferences and required criteria
        filtered_jobs = self.filter_jobs(user)
        
        # Step 2: Score the filtered jobs
        scored_jobs = self.score_jobs(user, filtered_jobs)
        
        # Step 3: Rank the scored jobs
        ranked_jobs = self.rank_jobs(scored_jobs)
        
        # Step 4: Return the ranked list of jobs
        return ranked_jobs
