# Lab No. 11 Report - Databases Part II (Django)

## 1) Basic Information
- Project Name: `lab10`
- Apps Created: `q1`, `q2`, `q3`, `a1`
- Database: SQLite (`db.sqlite3`)
- Framework: Django (MTV architecture)

---

## 2) Step-by-Step Implementation

### Step 1: Environment Setup
From project folder:

```bash
python3 -m venv .venv
.venv/bin/pip install django
```

### Step 2: Create Project and Apps
```bash
.venv/bin/django-admin startproject lab10 .
.venv/bin/python manage.py startapp q1
.venv/bin/python manage.py startapp q2
.venv/bin/python manage.py startapp q3
.venv/bin/python manage.py startapp a1
```

### Step 3: Configure Project
Updated `lab10/settings.py`:
- Added apps in `INSTALLED_APPS`: `q1`, `q2`, `q3`, `a1`

Updated `lab10/urls.py`:
- Included app routes:
  - `path('q1/', include('q1.urls'))`
  - `path('q2/', include('q2.urls'))`
  - `path('q3/', include('q3.urls'))`
  - `path('a1/', include('a1.urls'))`

### Step 4: Create Models, Forms, Views, Templates
Implemented each question app separately (details below).

### Step 5: Create and Apply Migrations
```bash
.venv/bin/python manage.py makemigrations
.venv/bin/python manage.py migrate
```

### Step 6: Validate Project
```bash
.venv/bin/python manage.py check
```

---

## 3) Question-wise Implementation Details

## Q1 App (`q1`) - Author, Publisher, Book

### Requirement Covered
Design form(s) to populate and retrieve data for:
- Author: first name, last name, email
- Publisher: name, street address, city, state/province, country, website
- Book: title, publication date, multiple authors, single publisher

### Models Implemented
- `Author(first_name, last_name, email)`
- `Publisher(name, street_address, city, state_province, country, website)`
- `Book(title, publication_date, authors(ManyToMany), publisher(ForeignKey))`

### Forms Implemented
- `AuthorForm`
- `PublisherForm`
- `BookForm`

### View Logic
- Single page with 3 forms.
- Uses hidden `form_type` to detect which form was submitted.
- Saves record and redirects back to same page.
- Retrieves and displays all authors, publishers, books.

### Files
- `q1/models.py`
- `q1/forms.py`
- `q1/views.py`
- `q1/urls.py`
- `q1/templates/q1/index.html`

### URL
- `/q1/`

---

## Q2 App (`q2`) - Product Entry + Index List

### Requirement Covered
- Create product entry page (title, price, description)
- Save to DB
- Create index page to display entries in unordered list

### Model Implemented
- `Product(title, price, description)`

### Form Implemented
- `ProductForm`

### View Logic
- `add_product`: handles form submit and save.
- `index`: retrieves all products and shows them in `<ul><li>` format.

### Files
- `q2/models.py`
- `q2/forms.py`
- `q2/views.py`
- `q2/urls.py`
- `q2/templates/q2/add_product.html`
- `q2/templates/q2/index.html`

### URLs
- `/q2/`
- `/q2/add/`

---

## Q3 App (`q3`) - Human DropDown, Update, Delete

### Requirement Covered
- On page load, dropdown displays first names from `Human` table.
- On selecting a name, details fill textboxes.
- Update button updates selected record.
- Delete button deletes selected record and refreshes dropdown.

### Model Implemented
- `Human(first_name, last_name, phone, address, city)`

### View Logic
- GET: load all humans and selected record from query parameter `?human=id`.
- POST + `action=update`: update selected record from textboxes.
- POST + `action=delete`: delete selected record and redirect to refreshed page.

### Files
- `q3/models.py`
- `q3/views.py`
- `q3/urls.py`
- `q3/templates/q3/index.html`

### URL
- `/q3/`

### Note
- To use Q3 page, at least one `Human` record should exist (can be added from admin).

---

## Additional Question A1 App (`a1`) - Student Entry + Display

### Requirement Covered
Input and display:
- Student Id
- Student Name
- Course Name
- Date of Birth

### Model Implemented
- `Student(student_id, student_name, course_name, date_of_birth)`

### Form Implemented
- `StudentForm`

### View Logic
- Single page:
  - save student via form
  - display all students below form

### Files
- `a1/models.py`
- `a1/forms.py`
- `a1/views.py`
- `a1/urls.py`
- `a1/templates/a1/index.html`

### URL
- `/a1/`

---

## 4) Django Admin (Database Table Management)

Registered all models in admin:
- `q1/admin.py`: `Author`, `Publisher`, `Book`
- `q2/admin.py`: `Product`
- `q3/admin.py`: `Human`
- `a1/admin.py`: `Student`

Create admin user:
```bash
.venv/bin/python manage.py createsuperuser
```

Admin URL:
- `/admin/`

This allows viewing, inserting, updating, and deleting all table records through admin UI.

---

## 5) Mapping to Lab Objectives

1. **Understand MTV architecture**
   - Model: `models.py`
   - View: `views.py`
   - Template: `templates/...`

2. **Create app and connect to SQLite DB**
   - Four apps created and connected to default SQLite DB.

3. **Set different privileges for users**
   - Django admin supports users/groups/permissions.
   - Privileges can be assigned in admin (`/admin/`).

4. **Set Django administrator account**
   - Done via `createsuperuser` command.

---

## 6) How to Run (Final)

From root folder:

```bash
source .venv/bin/activate
python manage.py runserver
```

Open in browser:
- http://127.0.0.1:8000/q1/
- http://127.0.0.1:8000/q2/
- http://127.0.0.1:8000/q2/add/
- http://127.0.0.1:8000/q3/
- http://127.0.0.1:8000/a1/
- http://127.0.0.1:8000/admin/

---

## 7) Minimal Design Constraint Followed

- UI kept basic and simple (plain HTML forms and lists).
- No extra features added beyond asked questions.
- Only required fields, pages, and operations implemented.
