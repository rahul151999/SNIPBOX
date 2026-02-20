# 📝 SnipBox Backend API

SnipBox is a Django REST Framework backend API for saving short notes (snippets) and organizing them using tags. It supports authentication, CRUD operations, pagination, tagging, and bulk deletion.

---

# 🚀 Features

* JWT Authentication (Login + Refresh)
* Create, Read, Update, Delete snippets
* Partial updates using PATCH
* Tag system with uniqueness enforcement
* Reuse existing tags automatically
* Owner-based access control
* Pagination support
* Bulk delete API
* Hyperlinked overview endpoint
* Docker support (optional setup)

---

# 🛠 Tech Stack

* Python 3.12
* Django
* Django REST Framework
* PostgreSQL
* JWT Authentication
* PDM (package manager)
* Docker (optional)

---

# 📦 Installation (Local Setup)

### 1️⃣ Clone Repository


git clone https://github.com/rahul151999/SNIPBOX.git
cd snipbox

---

### 2️⃣ Install Dependencies


pdm install

---

### 3️⃣ Create `.env` file

DEBUG=True

DB_NAME=DB_NAME
DB_USER=DB_USER
DB_PASSWORD=DB_PASSWORD
DB_HOST=localhost
DB_PORT=5432

---

### 4️⃣ Run Migrations


pdm run python manage.py migrate

---

### 5️⃣ Run Server


pdm run python manage.py runserver

Server runs at:

http://127.0.0.1:8000

---

---

# 🔐 Authentication

Login:

POST /api/auth/login/

Use token:

Authorization: Bearer <access_token>

---

---

# 📚 API Endpoints

---

## Snippets

| Method | Endpoint                | Description      |
| ------ | ----------------------- | ---------------- |
| GET    | `/api/snippets/`        | List snippets    |
| POST   | `/api/snippets/`        | Create snippet   |
| GET    | `/api/snippet/<id>`     | Retrieve snippet |
| PUT    | `/api/snippet/<id>`     | Full update      |
| PATCH  | `/api/snippet/<id>`     | Partial update   |
| DELETE | `/api/snippet/<id>`     | Delete single    |
| DELETE | `/api/snippets/delete/` | Bulk delete      |

---

---

## Tags

| Method | Endpoint          | Description        |
| ------ | ----------------- | ------------------ |
| GET    | `/api/tags/`      | List all tags      |
| GET    | `/api/tags/<id>/` | Snippets under tag |

---

---

# 🔗 Overview API Response Example

GET /api/snippets/

```json
{
  "total_snippets": 2,
  "snippets": [
    {
      "id": 1,
      "title": "Meeting Notes",
      "detail_url": "http://127.0.0.1:8000/api/snippet/1"
    }
  ]
}

Each snippet contains a hyperlink to its detail API.

---

---

# 🏷 Tag Behavior

* Tags are sent as list of titles
* Titles must be unique
* Existing tags reused
* No duplicates created

---

---

# 📄 Pagination

Enabled globally.

/api/snippets/?page=2

---

---

# 🔒 Permissions

| Action         | Access              |
| -------------- | ------------------- |
| View snippet   | Owner only          |
| Edit snippet   | Owner only          |
| Delete snippet | Owner only          |
| Bulk delete    | Owner only          |
| Tags           | Authenticated users |

---

---

# 🧪 Example Requests

Create snippet:


curl -X POST http://127.0.0.1:8000/api/snippets/ \
-H "Authorization: Bearer TOKEN" \
-H "Content-Type: application/json" \
-d '{"title":"Note","note":"Hello","tags":["Work"]}'

---

---

# 🐳 Docker Setup (Optional)

### Run Project in Docker


docker compose build
docker compose up

Run migrations:


docker compose exec web python manage.py migrate

---

---

# 📊 Database Schema (Conceptual)

User
 └── Snippet
        ├── title
        ├── note
        ├── timestamps
        └── tags (M2M)

Tag
 └── title (unique)

---

---

# 📏 Coding Standards

* PEP-8 compliant
* Clean architecture
* Serializer inheritance
* DRF generic views
* Proper permissions

---

---

# 🧠 Design Decisions

* Tags reused instead of recreated
* Separate serializers for overview and detail
* Bulk delete endpoint added for efficiency
* Pagination enforced for scalability
* Hyperlinks included for REST navigation

---

---

# 👨‍💻 Author

**Rahul K S**

---

---

# ⭐ Reviewer Notes

This project demonstrates:

* RESTful API design
* authentication handling
* database optimization
* scalable architecture
* production-ready structure

---
