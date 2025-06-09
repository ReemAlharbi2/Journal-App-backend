# Journal App

Journal App, a personal journaling application where users can register, log in, and create, edit, and delete notes with moods and categories. The app is built using React and communicates with a Django backend.

## Frontend Repository
[Frontend Repository Link] (https://github.com/ReemAlharbi2/Journal-App-frontend.git)

## Tech Stack
- **Django**
- **Django REST Framework**
- **PostgreSQL**
- **JWT (JSON Web Token)**
- **Python**

## IceBox Features
- Add a "Favorite" feature to mark important notes
- Add search and filter functionality for journal entries by mood, category, or keyword.

## Installation Instructions
```bash
git clone https://github.com/ReemAlharbi2/Journal-App-backend.git
cd Journal-App-backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


```