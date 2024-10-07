# Job Recommendation System

This project implements a job recommendation system that matches job seekers with suitable job listings based on their skills and preferences.

## Setup Instructions

1. Clone the repository:

git clone https://github.com/sahalpk/job-recommendation-system.git

2. Install the required dependencies:

pip install -r requirements.txt

3. Set up the database:
[Provide instructions for setting up and populating the database]

4. Start the Flask server:
python app.py

5. The API will be available at `http://127.0.0.1:5000`

## API Endpoints

* GET /jobs: Returns a list of all job postings.
* GET /users: Returns a list of all user profiles.
* GET /users/<user_id>/recommended_jobs: Returns a list of recommended job postings for a specific user.
* POST /jobs: Creates a new job posting.
* POST /users: Creates a new user profile.
* POST /recommend: Returns a list of recommended job postings based on a user's profile.


## Project Structure

* `app.py`: The main application file
* `models/`: The directory containing the data models
* `routes/`: The directory containing the API routes
* `templates/`: The directory containing the HTML templates
* `static/`: The directory containing the static files
* `requirements.txt`: The file containing the dependencies
* `README.md`: This file
* `Documentation.md`: The file containing the project documentation

## Technologies Used

* Flask: The web framework
* MongoDB: The database
* Python: The programming language

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.