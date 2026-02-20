# 📘 SnipBox API Documentation

Base URL


http://127.0.0.1:8000/api/


Authentication
All endpoints (except register/login) require:


Authorization: Bearer <access_token>


---

# 🔐 AUTH APIs

---

## Register User

**POST** `/auth/register/`

**Body**

{
  "username": "rahul",
  "password": "123456",
  "email": "rahul@mail.com"
}


**Response — 201**

{
  "id": 1,
  "username": "rahul",
  "email": "rahul@mail.com"
}


---

## Login

**POST** `/auth/login/`

**Body**

{
  "username": "rahul",
  "password": "123456"
}


**Response**

{
  "access": "ACCESS_TOKEN",
  "refresh": "REFRESH_TOKEN"
}


---

## Refresh Token

**POST** `/auth/refresh/`

{
  "refresh": "REFRESH_TOKEN"
}


---

---

# 📝 SNIPPET APIs

---

## 1️⃣ List Snippets

**GET** `/snippets/`

Returns paginated snippets belonging to logged-in user.

**Response — 200**

{
  "count": 4,
  "next": null,
  "previous": null,
  "results": {
    "total_snippets": 4,
    "snippets": [
      {
        "id": 4,
        "title": "Test Meeting",
        "note": "Discuss release timeline",
        "tag_titles": ["Meetings"],
        "created_at": "2026-02-20T05:02:19Z",
        "updated_at": "2026-02-20T05:02:19Z"
      }
    ]
  }
}


---

## 2️⃣ Create Snippet

**POST** `/snippets/`

Creates snippet and attaches tags.

If tag exists → reused
If not → created automatically

**Body**

{
  "title": "Test Meeting",
  "note": "Discuss release timeline",
  "tags": ["Meetings"]
}


**Response — 201**

{
  "id": 4,
  "title": "Test Meeting",
  "note": "Discuss release timeline",
  "tag_titles": ["Meetings"],
  "created_at": "2026-02-20T05:02:19Z",
  "updated_at": "2026-02-20T05:02:19Z"
}

---

# 👨‍💻 Author

Rahul K S

---
