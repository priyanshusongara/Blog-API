 <img width="100" height="100" alt="favicon" src="https://github.com/user-attachments/assets/e7252b88-137f-47be-85ee-fbb37ab36b23" />  # Blog API (Django REST Framework)
## Live API

🔗 https://blog-api-production-00ec.up.railway.app/

---

## Overview

A production-ready Blog API built using Django REST Framework with JWT authentication, allowing users to create, manage, and interact with blog posts securely.

This project demonstrates real-world backend concepts such as authentication, permissions, and scalable API design.

---

## Features

### Authentication

* User Registration
* Login with JWT Authentication
* Token-based secure access

### Blog Functionality

* Create posts
* View all posts
* Update & delete own posts only
* View other users' posts (read-only)

### Comments System

* Add comments to posts
* View comments on posts

### Advanced Features

* Search functionality
* Pagination for large datasets
* Permission-based access control
 

  ---

## 📸 API Preview & Testing  

  <img width="1920" height="1080" alt="Screenshot (3591)" src="https://github.com/user-attachments/assets/aff14491-4811-413f-8992-2a9e4ca67f81" />  
  API Interface :  
  
  <img width="1920" height="1080" alt="Screenshot (3592)" src="https://github.com/user-attachments/assets/d341efae-83fa-4899-92b0-1bba50bd36e3" />

---

## Tech Stack

* **Backend:** Django, Django REST Framework
* **Authentication:** JWT (JSON Web Tokens)
* **Database:** PostgreSQL
* **Deployment:** Railway
* **Frontend (Demo UI):** HTML, CSS

---

## 📡 API Endpoints

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| POST   | /api/register/   | Register new user |
| POST   | /api/login/      | Login & get token |
| GET    | /api/posts/      | Get all posts     |
| POST   | /api/posts/      | Create post       |
| PUT    | /api/posts/{id}/ | Update own post   |
| DELETE | /api/posts/{id}/ | Delete own post   |
| GET    | /api/comments/   | View comments     |
| POST   | /api/comments/   | Add comment       |

---

## Authentication Usage

Add token in headers:

```id="token1"
Authorization: Bearer <your_token>
```

---

## Installation

```bash id="install2"
git clone https://github.com/priyanshusongara/Blog-API.git
cd blog-api
pip install -r requirements.txt
python manage.py runserver
```

---

## Concepts Used

* Django REST Framework (APIView / ViewSets)
* JWT Authentication
* Permissions & Authorization
* Serializers
* Pagination
* Filtering & Search
* RESTful API Design

---

## What I Learned

* Built a secure API with JWT authentication
* Implemented user-based permissions (ownership logic)
* Designed scalable REST APIs
* Improved backend architecture and debugging skills

---

##  Developed by : **Priyanshu Songara**





