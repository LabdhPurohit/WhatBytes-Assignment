# Whatbytes Healthcare Backend

A Django REST Framework backend for a healthcare application, supporting JWT authentication, patient and doctor management, and patient-doctor mappings. Uses PostgreSQL and environment variables for secure configuration.

---
## All Tested API's with Responses

- Link: https://labdhpurohit.postman.co/workspace/Labdh-Purohit's-Workspace~b36c68a9-ad4e-40cf-87d0-5f184df6400b/collection/46880127-1584966b-c73a-439e-9c12-dfa4d03ce4c3?action=share&creator=46880127

---

## 🚀 Features
- User registration and JWT login
- CRUD for patients (per user)
- CRUD for doctors (global)
- Assign/remove doctors to/from patients
- PostgreSQL database
- Environment variable support via `.env`

---

## 🛠️ Tech Stack
- Django & Django REST Framework
- PostgreSQL
- djangorestframework-simplejwt (JWT auth)
- python-dotenv

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/LabdhPurohit/WhatBytes-Assignment.git
cd Whatbytes
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
Create a `.env` file in the project root:
```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/DBNAME
```

⚠️ Attention:
- The .env file is not included in this repository for security reasons.
- If you need it for local development or testing, feel free to reach out and I’ll provide it securely.

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Start the server
```bash
python manage.py runserver
```

---

## 🔑 API Authentication
- Obtain JWT tokens via `/api/auth/login/`.
- For protected endpoints, add this header:
  ```
  Authorization: Bearer <access_token>
  ```

---

## 📚 API Endpoints Overview

### Authentication
- `POST /api/auth/register/` — Register a new user
- `POST /api/auth/login/` — Log in and get JWT tokens

### Patients
- `POST /api/patients/` — Create patient (auth required)
- `GET /api/patients/` — List your patients
- `GET /api/patients/<id>/` — Get patient details
- `PUT /api/patients/<id>/` — Update patient
- `DELETE /api/patients/<id>/` — Delete patient

### Doctors
- `POST /api/doctors/` — Create doctor (auth required)
- `GET /api/doctors/` — List all doctors
- `GET /api/doctors/<id>/` — Get doctor details
- `PUT /api/doctors/<id>/` — Update doctor
- `DELETE /api/doctors/<id>/` — Delete doctor

### Patient-Doctor Mappings
- `POST /api/mappings/` — Assign doctor to patient
- `GET /api/mappings/` — List all mappings
- `GET /api/mappings/<patient_id>/` — List all doctors for a patient
- `DELETE /api/mappings/<id>/` — Remove doctor from patient

---

## 🧪 Example API Usage (with curl)

### Register
```bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "name": "User", "password": "password123"}'
```

### Login
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "password123"}'
```

### Create Patient
```bash
curl -X POST http://127.0.0.1:8000/api/patients/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "age": 30, "gender": "M"}'
```

---

## 🧑‍💻 Testing
- Use [Postman](https://www.postman.com/) or curl to test all endpoints.
- Link: https://labdhpurohit.postman.co/workspace/Labdh-Purohit's-Workspace~b36c68a9-ad4e-40cf-87d0-5f184df6400b/collection/46880127-1584966b-c73a-439e-9c12-dfa4d03ce4c3?action=share&creator=46880127
