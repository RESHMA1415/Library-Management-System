# 📚 Library Management System (LMS)

A full-stack **Library Management System** developed using **Django** that enables efficient management of books, users, reservations, and reports with role-based authentication.

---

## 🚀 Features

- User Authentication (Login & Logout)
- Role-Based Access Control
  - Admin
  - Librarian
  - Student
- Book Management (CRUD)
- Book Reservation System
- Book Issue & Return
- Fine Calculation
- Search Books
- Dashboard
- Reports
- Responsive UI using Bootstrap

---

## 🛠️ Technologies Used

- Python
- Django
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- SQLite (Default Database)

---

## 📂 Project Structure

```
librarymanagement/
│
├── accounts/
├── books/
├── reservations/
├── reports/
├── templates/
├── static/
├── media/
├── librarymanagement/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── db.sqlite3
└── requirements.txt
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Library-Management-System.git
```

### Move into Project

```bash
cd Library-Management-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

---

## 👥 User Roles

### Admin

- Manage Users
- Manage Books
- View Reports
- Dashboard Access

### Librarian

- Add Books
- Update Books
- Issue Books
- Return Books
- Manage Reservations

### Student

- Search Books
- Reserve Books
- View Issued Books
- Check Fine

---

## 📸 Screenshots

### Home Page

(Add Screenshot)

### Login Page

(Add Screenshot)

### Dashboard

(Add Screenshot)

### Book List

(Add Screenshot)

### Reservation Page

(Add Screenshot)

### Reports

(Add Screenshot)

---

## 📊 Database Models

- User
- Book
- Category
- Reservation
- IssueBook
- Fine

---

## 📌 Future Enhancements

- Email Notification
- QR Code for Books
- Barcode Scanner
- Online Fine Payment
- REST API
- Mobile Application
- PDF Report Generation

---

## 🎯 Learning Outcomes

- Django Authentication
- Django ORM
- CRUD Operations
- Role-Based Authorization
- Template Inheritance
- Database Relationships
- Bootstrap Integration
- Reporting System

---

## 👩‍💻 Developed By

**Reshma**

MCA Graduate

Python & Django Developer

Software Trainer

---

## 📄 License

This project is developed for educational and portfolio purposes.
