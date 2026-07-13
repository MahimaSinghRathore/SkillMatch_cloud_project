# SkillMatch

SkillMatch is a serverless web application that helps connect students with internship opportunities based on their skills and interests. The project demonstrates how AWS services such as Lambda, API Gateway, and DynamoDB can be used to build a scalable internship recommendation platform.

The frontend is built using HTML, CSS, and JavaScript, while the backend consists of AWS Lambda functions that interact with DynamoDB through Amazon API Gateway.

---

## Features

- Create and update student profiles
- Add internship opportunities
- View available internships
- Match students with internships based on their skills
- Apply for internships
- View submitted applications
- Single-page responsive user interface
- Serverless backend using AWS services

---

## Technologies Used

### Frontend

- HTML5
- CSS3
- JavaScript (Vanilla)

### Backend

- AWS Lambda
- Amazon API Gateway

### Database

- Amazon DynamoDB

### Cloud

- AWS

---

## Project Structure

```text
SkillMatch/
│
├── index.html
├── Lambda_function_create_or_update_profile.py
├── Lambda_function_get_profile
├── Lambda_function_create_internship.py
├── Lambda_function_list_internship.py
├── Lambda_function_match_for_user.py
├── Lambda_function_apply_internship.py
└── README.md
```

---

## System Architecture

```text
                User
                  │
                  ▼
HTML • CSS • JavaScript Frontend
                  │
                  ▼
          Amazon API Gateway
                  │
                  ▼
          AWS Lambda Functions
                  │
                  ▼
         Amazon DynamoDB
```

---

## How It Works

1. Students create their profiles with skills and interests.
2. Organizations add internship opportunities.
3. Internship details are stored in DynamoDB.
4. Lambda functions retrieve and match internships.
5. Students can apply for internships.
6. Applications are stored for later retrieval.

---

## AWS Lambda Functions

The project contains separate Lambda functions for each operation.

| Function | Purpose |
|----------|---------|
| Create/Update Profile | Stores student profiles |
| Get Profile | Retrieves user profile |
| Create Internship | Adds internship opportunities |
| List Internship | Retrieves all internships |
| Match for User | Matches internships based on user skills |
| Apply Internship | Stores internship applications |

---

## API Endpoints

### POST `/profiles`

Create or update a student profile.

```json
{
  "userId":"mahima001",
  "name":"Mahima",
  "skills":["aws","cpp"],
  "interests":["backend","cloud"]
}
```

---

### POST `/internships`

Create a new internship.

```json
{
  "title":"Cloud Intern",
  "company":"TechCorp",
  "requiredSkills":["aws"]
}
```

---

### GET `/internships`

Returns all internships.

---

### GET `/match/{userId}`

Returns internship recommendations for a student.

---

### POST `/apply`

Apply for an internship.

```json
{
  "userId":"mahima001",
  "internshipId":"intern123"
}
```

---

### GET `/applications`

Returns all submitted applications.

---

## Running the Project

Clone the repository.

```bash
git clone https://github.com/MahimaSinghRathore/SkillMatch.git
```

Open

```
index.html
```

in a modern web browser.

Alternatively, start a local server.

```bash
python -m http.server 8000
```

Then visit

```
http://localhost:8000
```

---

## Backend Setup

Configure the following AWS services.

### DynamoDB Tables

- Profiles
- Internships
- Applications

### AWS Lambda

Deploy each Lambda function individually.

### API Gateway

Create REST API endpoints and connect them to the corresponding Lambda functions.

Update the API Gateway URL inside:

```javascript
const API_BASE = "YOUR_API_GATEWAY_URL";
```

---

## Applications

- Internship Recommendation Platform
- Campus Placement Portal
- Career Development Platform
- Student Recruitment System
- Skill-Based Job Matching

---

## Future Enhancements

- AWS Cognito Authentication
- Resume Upload
- Email Notifications
- Admin Dashboard
- Company Portal
- Search and Filters
- Better Recommendation Algorithm
- Application Status Tracking

---

## Project Status

- Frontend implementation completed.
- Backend Lambda functions implemented.
- Designed for deployment on AWS using API Gateway and DynamoDB.
- Cloud deployment is currently under development.

---

## Author

**Mahima Singh**

B.Tech Computer Science Engineering

Jaypee University of Information Technology (JUIT)

GitHub: https://github.com/MahimaSinghRathore

---

## License

This project was developed for educational purposes to demonstrate serverless web application development using AWS cloud services.
