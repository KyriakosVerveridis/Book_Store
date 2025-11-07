# 🏛️ Django Book Store App

A simple Django web application for managing books, authors, and published countries.

The app allows admins to:
- Add, edit, and delete books
- Add authors and link them to addresses
- Track which countries a book is published in via a ManyToMany relationship
- Manage all data using Django admin

---

## 🚀 Features
- ManyToMany relationship for `published_countries` in Books
- OneToOne relationship for `address` in Authors
- Admin dashboard for managing entries

---

## 🛠️ Tech Stack
- Backend: Django 5.2.7 (Python 3.12)
- Frontend: HTML, CSS
- Database: SQLite (default Django DB)
- Environment Management: Virtual Environment + requirements.txt
- Dependencies: asgiref, sqlparse, tzdata, pillow

---

## ⚙️ Installation & Setup

1. Clone the repository
```
git clone https://github.com/yourusername/book_store.git
cd book_store
```

2. Create and activate a virtual environment
# Windows PowerShell
```
python -m venv venv
.\venv\Scripts\Activate.ps1
```

# macOS/Linux
```
python -m venv venv
source venv/bin/activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Set up environment variables
Create a .env file in the project root and add:
```
SECRET_KEY=your_secret_key
DEBUG=True
```

5. Run database migrations
```
python manage.py migrate
```

6. Create a superuser (for admin access)
```
python manage.py createsuperuser
```

7. Start the development server
```
python manage.py runserver
```

8. Access the app
- Main app: http://127.0.0.1:8000
- Admin panel: http://127.0.0.1:8000/admin

---

## 🧩 Project Structure
```
book_store/
├── book_store/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── book_outlet/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── book_outlet/
│           ├── base.html
│           ├── book_detail.html
│           └── index.html
│
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## 🧠 Learning Outcomes
Through this project, I learned how to:
- Use Django ORM for relational data management
- Implement ManyToMany and OneToOne relationships
- Build and manage data through Django admin
- Organize templates and static files in a Django project
- Create a clean and functional project structure

---

## 👤 Author
Kyriakos Ververidis
📍 Based in Greece
💬 Open to remote opportunities
📧 ververidiskyriakos@gmail.com
🔗 https://www.linkedin.com/in/kyriakos-ververidis-593a8561/

---

## 📝 License
This project is open-source and free to use for educational purposes.
License: MIT License – see LICENSE for details.
