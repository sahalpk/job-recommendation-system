from flask import Flask, request, jsonify
from models.jobs import Job
from models.user import User
from recommendation.recommendation_algorithm import RecommendationAlgorithm
from utils.database import Database
from utils.json_encoder import CustomJSONEncoder

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder

# Initialize database
db = Database("job_recommender", "jobs")

# Load job postings and user profiles from database
jobs = db.get_all_jobs()
users = db.get_all_users()

# Create recommendation algorithm instance
recommendation_algorithm = RecommendationAlgorithm()
for job in jobs:
    recommendation_algorithm.add_job(job)
for user in users:
    recommendation_algorithm.add_user(user)

@app.route('/')
def index():
    return "Welcome to the Job Recommender System!"

@app.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = db.get_all_jobs()
    return jsonify(jobs)

@app.route('/users', methods=['GET'])
def get_users():
    users = db.get_all_users()
    return jsonify([user.to_dict() for user in users])

@app.route('/users/<user_id>/recommended_jobs', methods=['GET'])
def get_recommended_jobs(user_id):
    user = db.users_collection.find_one({'_id': user_id})
    if user:
        recommended_jobs = db.recommend_jobs(User(user['_id'], user['name'], user['skills'], user['experience_level'], user['preferences']))
        return jsonify([job.to_dict() for job in recommended_jobs])
    else:
        return jsonify({'error': 'User   not found'}), 404

@app.route('/jobs', methods=['POST'])
def create_job():
    job_data = request.get_json()
    if job_data is not None:
        job = Job(job_data['_id'], job_data['job_id'], job_data['job_title'], job_data['company'], job_data['required_skills'], job_data['location'], job_data['job_type'], job_data['experience_level'], job_data['salary_range'])
        db.insert_job(job)
        return jsonify(job.to_dict()), 201
    else:
        return jsonify({'error': 'Invalid job data'}), 400


@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    if user_data is not None:
        user = User(user_data['_id'], user_data['name'], user_data['skills'], user_data['experience_level'], user_data['preferences'])
        db.insert_user(user)
        return jsonify(user.to_dict()), 201
    else:
        return jsonify({'error': 'Invalid user data'}), 400

@app.route('/recommend', methods=['POST'])
def recommend():
    user_profile = request.get_json()
    if user_profile is not None:
        recommended_jobs = recommendation_algorithm.recommend(user_profile)
        return jsonify(recommended_jobs)
    else:
        return jsonify({'error': 'Invalid user profile'}), 400

if __name__ == '__main__':
    app.run(debug=True)
