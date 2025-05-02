<h1 align="center">DRF-Practice</h1>

This repository contains practice projects and examples built using **Django REST Framework (DRF)**. The goal is to get hands-on experience with building *RESTful APIs* using Django's robust tools and serializers.

## 🚀 Features Implemented

- Model definition using Django ORM
- Serializer creation with `HyperlinkedModelSerializer`
- ViewSet implementation with `ModelViewSet`
- URL routing using DRF's `DefaultRouter`
- Browsable API interface
- API authentication via session login/logout

## 🛠 Tech Stack

- Python 3
- Django 4.x
- Django REST Framework
- SQLite (default DB)

## 📂 Project Structure

```

DRF-Practice/
├── apis/
│   ├── models.py          # GeeksModel definition
│   ├── serializers.py     # GeeksSerializer using HyperlinkedModelSerializer
│   ├── views.py           # GeeksViewSet for full CRUD API
│   └── urls.py            # DRF router and URL configuration
├── drf\_practice/          # Main Django project config
│   └── urls.py            # Includes API URLs and admin route
└── manage.py

````

## ⚙️ How to Run Locally

1. **Clone the repo**
   ```
   git clone https://github.com/RR0327/DRF-Practice.git
   cd DRF-Practice
   ```

2. **Create and activate a virtual environment**
   ```
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the development server**
   ```
   python manage.py runserver
   ```

## 📌 Endpoints Overview

| Method | Endpoint       | Description            |
| ------ | -------------- | ---------------------- |
| GET    | `/geeks/`      | List all entries       |
| POST   | `/geeks/`      | Create new entry       |
| GET    | `/geeks/<id>/` | Retrieve specific item |
| PUT    | `/geeks/<id>/` | Update specific item   |
| DELETE | `/geeks/<id>/` | Delete specific item   |

## 🙋‍♂️ About Me

Md Rakibul Hassan

CSE Undergraduate | Backend Developer | Robotics & IoT Enthusiast

🔗 [LinkedIn](https://www.linkedin.com/in/md-rakibul-hassan-507b00308)

🐙 [GitHub](https://github.com/RR0327)

---

This is a growing repository for exploring Django REST Framework — feel free to clone and experiment!

