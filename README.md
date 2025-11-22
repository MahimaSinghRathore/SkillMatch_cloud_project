SkillMatch

SkillMatch is a simple web application that helps match students with internships based on their skills and interests. The front end is a single HTML file, and the backend runs on AWS using Lambda, API Gateway and DynamoDB.

This project is designed as a lightweight demo that shows how a serverless architecture can power a real matching system.

Features

Create and update user profiles

Add internships with required skills

Fetch all internships

Match a user with the most relevant internships

Apply for an internship

View all applications

Works directly with AWS API Gateway + Lambda

Fully client-side UI built with plain HTML, CSS and JavaScript

Tech Stack

Frontend:
HTML, CSS, Vanilla JavaScript

Backend:
AWS Lambda
AWS API Gateway
AWS DynamoDB
AWS S3 (optional for hosting)

Project Structure
SkillMatch/
│── index.html     # Main UI (single page app)
│── README.md      # Documentation


All logic for UI interactions and API calls exists inside the index.html file.

How It Works

The user interacts with the UI in index.html.

Each button triggers a JavaScript fetch() call to your API Gateway URL.

API Gateway routes the call to Lambda functions.

Lambda reads/writes data in DynamoDB tables:

Profiles

Internships

Applications

The response is shown instantly in the UI.

API Base URL

Inside the index.html, update this line with your API Gateway base URL:

const API_BASE = "https://your-api-url.execute-api.region.amazonaws.com/prod";

API Endpoints
1. Save or Update Profile

POST /profiles
Body:

{
  "userId": "mahima001",
  "name": "Mahima",
  "skills": ["aws", "cpp"],
  "interests": ["backend", "cloud"]
}

2. Add Internship

POST /internships
Body:

{
  "title": "Cloud Intern",
  "requiredSkills": ["aws"],
  "company": "TechCorp"
}

3. Get All Internships

GET /internships

4. Get Matches for a User

GET /match/{userId}

5. Apply for Internship

POST /apply
Body:

{
  "userId": "mahima001",
  "internshipId": "intern123"
}

6. Get All Applications

GET /applications

Running Locally

You can open the project locally without any server.

Method 1: Direct open

Just double-click index.html.

Method 2: Start simple server
python -m http.server 8000


Then open:

http://localhost:8000/index.html

Deploying to AWS

To deploy the backend:

Create DynamoDB tables:

Profiles (Partition key: userId)

Internships (Partition key: internshipId)

Applications (Partition key: applicationId)

Create Lambda functions:

Save profile

Add internship

Get internships

Get matches

Apply

Get applications

Create API Gateway REST API with routes matching the endpoints.

Deploy the API and copy its base URL into API_BASE.

How to Use the UI

Fill out profile details and click Save Profile

Add internships from the Add Internship section

Enter a userId and click Get Matches to see recommended internships

Click Apply inside a matching internship

View all applications in the Applications section

Future Improvements

Add authentication (AWS Cognito)

Better ranking algorithm for matching

Pagination and filters

Email notifications after application
