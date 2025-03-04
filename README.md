# Django REST Framework Authentication with Knox

## 🚀 Project Overview
This project is a Django REST Framework (DRF) API with user authentication handled by **Knox** tokens. It includes user registration, login, logout, and fetching user data.

## 📌 Features
- User Registration
- User Login (using Knox token authentication)
- User Logout & Logout All Sessions
- Retrieve Authenticated User Data
- Secure password handling with Django's built-in authentication

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git https://github.com/snipher-marube/knox-authentication-api.git
cd knox-authentication-api
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations
```sh
python manage.py migrate
```

### 5️⃣ Create a Superuser (Optional)
```sh
python manage.py createsuperuser
```

### 6️⃣ Run the Server
```sh
python manage.py runserver
```

---

## 🔑 API Endpoints

### 📌 User Registration
**Endpoint:** `POST /api/auth/register/`
**Body:**
```json
{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpassword"
}
```
**Response:**
```json
{
    "user": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com"
    },
    "token": "knox-token"
}
```

---

### 📌 User Login
**Endpoint:** `POST /api/auth/login/`
**Body:**
```json
{
    "username": "testuser",
    "password": "testpassword"
}
```
**Response:**
```json
{
    "token": "knox-token"
}
```

---

### 📌 Get Authenticated User Data
**Endpoint:** `GET /api/auth/user/`
**Headers:**
```sh
Authorization: Token knox-token
```
**Response:**
```json
{
    "id": 1,
    "username": "testuser",
    "email": "test@example.com"
}
```

---

### 📌 User Logout
**Endpoint:** `POST /api/auth/logout/`
**Headers:**
```sh
Authorization: Token knox-token
```
**Response:**
```json
{
    "success": "Successfully logged out"
}
```

---

### 📌 Logout from All Sessions
**Endpoint:** `POST /api/auth/logoutall/`
**Headers:**
```sh
Authorization: Token knox-token
```
**Response:**
```json
{
    "success": "Successfully logged out from all sessions"
}
```

---

## 🛠 Debugging & Troubleshooting

### 🔍 Common Issues
1. **Login Not Working in Postman?**
   - Ensure you're sending JSON data (not form-data).
   - Set **`Content-Type: application/json`** in headers.
   - If using Postman, clear cookies and try again.

2. **Knox Tokens Not Generated?**
   - Run migrations: `python manage.py migrate knox`
   - Ensure `rest_framework` settings include Knox authentication:
     ```python
     REST_FRAMEWORK = {
         'DEFAULT_AUTHENTICATION_CLASSES': (
             'knox.auth.TokenAuthentication',
             'rest_framework.authentication.BasicAuthentication',
             'rest_framework.authentication.SessionAuthentication',
         )
     }
     ```

3. **Check Server Logs**
   - Add debug prints in `views.py` if needed.
   - Restart server after changes: `CTRL + C` then `python manage.py runserver`.

---

## 💡 Tech Stack
- **Django** - Web framework
- **Django REST Framework (DRF)** - API development
- **Knox** - Token-based authentication
- **SQLite/PostgreSQL** - Database (configurable)

---

## 📜 License
This project is licensed under the MIT License.

---

## 📞 Contact
For any issues, feel free to raise a GitHub issue or contact me at `your-email@example.com`. 🚀

