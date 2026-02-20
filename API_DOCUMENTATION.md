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
    "count": 2,
    "next": null,
    "previous": null,
    "results": {
        "total_snippets": 2,
        "snippets": [
            {
                "id": 6,
                "title": "Test Meeting2",
                "note": "Discuss release timeline",
                "tag_titles": ["Meetings"],
                "created_at": "2026-02-20T05:54:35.724025Z",
                "updated_at": "2026-02-20T05:54:35.724025Z",
                "detail_url": "http://127.0.0.1:8000/api/snippet/6",
            },
            {
                "id": 5,
                "title": "Reverted",
                "note": "Reverted text",
                "tag_titles": ["1"],
                "created_at": "2026-02-20T05:25:04.683611Z",
                "updated_at": "2026-02-20T05:42:51.972872Z",
                "detail_url": "http://127.0.0.1:8000/api/snippet/5",
            },
        ],
    },
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
3️⃣ Retrieve Snippet

GET /snippet/<id>

Returns snippet details.
---

4️⃣ Update Snippet

PUT /snippet/<id>

Body

{
  "title": "Updated",
  "note": "Updated text",
  "tags": ["Work"]
}

Returns updated snippet object.
---
5️⃣ Partial Update Snippet

PATCH /snippet/<id>

Updates only provided fields.

Example

{
  "title": "Only title changed"
}

----

6️⃣ Delete Single Snippet

DELETE /snippet/<id>

Deletes snippet and returns remaining snippets list.

Response

[
  {
    "id": 2,
    "title": "Note",
    "note": "Hello"
  }
]

---

7️⃣ Bulk Delete Snippets

DELETE /snippets/delete/

Deletes multiple snippets belonging to logged-in user.

Body

{
  "ids": [1,2,3]
}

Response

{
  "message": "Selected snippets deleted",
  "remaining_snippets": [...]
}

Validation Error

{
  "error": "No IDs provided"
}

---
# 🏷 Tag APIs

All tag endpoints require authentication.

Header:

Authorization: Bearer <token>

---

## 1️⃣ List Tags

**GET** `/tags/`

Returns list of all available tags.

Response

json
[
  {
    "id": 1,
    "title": "Meetings"
  },
  {
    "id": 2,
    "title": "Work"
  }
]

---

---

## 2️⃣ Tag Detail — Snippets Under Tag

**GET** `/tags/<id>/`

Returns snippets belonging to authenticated user that are associated with the selected tag.

---

### Example Request

GET /tags/1/

---

### Response

json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 4,
      "title": "Test Meeting",
      "note": "Discuss timeline",
      "tag_titles": ["Meetings"],
      "created_at": "...",
      "updated_at": "..."
    }
  ]
}

---

---

### Behavior Rules

* Returns only snippets owned by logged-in user
* Pagination applied automatically
* Tag must exist
* Unauthorized users cannot access

---

---

### Error Responses

**Unauthorized**

json
{
  "detail": "Authentication credentials were not provided."
}

**Tag Not Found**

json
{
  "detail": "Not found."
}

---

---

### Query Parameters

Pagination:

?page=2

---

---

### Status Codes

| Code | Meaning       |
| ---- | ------------- |
| 200  | Success       |
| 401  | Unauthorized  |
| 404  | Tag not found |

---

# 👨‍💻 Author

Rahul K S

---
