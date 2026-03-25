# Lab 10 - Databases Part I (Django)

Project: `lab9`  
Apps: `q1`, `q2`, `a1`

## What was implemented

- **Q1**: Website directory with:
  - `Category(name, visits, likes)`
  - `Page(category, title, url, views)`
  - Forms to insert Category and Page
  - Display of categories and their pages
- **Q2**: WORKS/LIVES with:
  - `WORKS(person_name, company_name, salary)`
  - `LIVES(person_name, street, city)`
  - Form to insert into WORKS
  - Search by company name to show people and their city
- **A1**: Institutes list box:
  - `Institutes(institute_id, name, no_of_courses)`
  - Page shows only institute names in a list box

## Commands used

Run from project folder:

```bash
cd /home/WP_C1/Documents/230905152_WP/L9
```

### 1) Create virtual environment

```bash
python3 -m venv .venv
```

### 2) Install Django

```bash
.venv/bin/pip install django
```

### 3) Create project and apps

```bash
.venv/bin/django-admin startproject lab9 .
.venv/bin/python manage.py startapp q1
.venv/bin/python manage.py startapp q2
.venv/bin/python manage.py startapp a1
```

### 4) Migrations and checks

```bash
.venv/bin/python manage.py makemigrations
.venv/bin/python manage.py migrate
.venv/bin/python manage.py check
```

### 5) Run server

```bash
.venv/bin/python manage.py runserver 0.0.0.0:8000
```

## URLs

- Home: http://127.0.0.1:8000/
- Q1: http://127.0.0.1:8000/q1/
- Q2: http://127.0.0.1:8000/q2/
- A1: http://127.0.0.1:8000/a1/
- Admin: http://127.0.0.1:8000/admin/

## Admin username and password

Use these lab credentials:

- Username: `admin`
- Password: `admin12345`

If not created yet, run this command once:

```bash
.venv/bin/python manage.py shell -c "from django.contrib.auth import get_user_model; User=get_user_model(); username='admin'; password='admin12345'; email='admin@example.com'; u,created=User.objects.get_or_create(username=username, defaults={'email':email,'is_staff':True,'is_superuser':True}); u.is_staff=True; u.is_superuser=True; u.set_password(password); u.email=email; u.save(); print('created' if created else 'updated')"
```

## Demo inputs

### Q1 demo data

Add Category:

- Name: `Programming`
- Visits: `25`
- Likes: `10`

Add Page:

- Category: `Programming`
- Title: `Django Official`
- URL: `https://www.djangoproject.com/`
- Views: `100`

You can add another category/page similarly.

### Q2 demo data

#### Step A: Add LIVES records (via admin)

Go to **Admin -> LIVES** and add:

1. Person Name: `Arun` | Street: `MG Road` | City: `Bengaluru`
2. Person Name: `Riya` | Street: `Park Street` | City: `Kolkata`
3. Person Name: `John` | Street: `Anna Nagar` | City: `Chennai`

#### Step B: Insert WORKS rows (from Q2 page)

Use form on `/q2/`:

1. Person Name: `Arun` | Company Name: `ABC Corp` | Salary: `45000`
2. Person Name: `Riya` | Company Name: `ABC Corp` | Salary: `52000`
3. Person Name: `John` | Company Name: `XYZ Ltd` | Salary: `60000`

#### Step C: Search

Search company name: `ABC Corp`  
Expected output: `Arun - Bengaluru`, `Riya - Kolkata`

### A1 demo data

Go to **Admin -> Institutes** and add:

1. Name: `IIT Delhi` | No of Courses: `120`
2. Name: `NIT Trichy` | No of Courses: `80`
3. Name: `ABC College` | No of Courses: `35`

Open `/a1/` to see only institute names in the list box.

## How to run (quick)

```bash
cd /home/WP_C1/Documents/230905152_WP/L9
python3 -m venv .venv
.venv/bin/pip install django
.venv/bin/python manage.py migrate
.venv/bin/python manage.py runserver
```

Lab No:10
Databases – Part I
Objectives:
In this lab, student will be able to
1. Understand the MTV architecture
2. Create an App in Django and establish a connection with SQLite database
3. Set different privileges to different types of users.
4. Set the Django administrator account.
LAB EXCERCISES
1. Design a web site using Django, which is a website directory – A site containing
links to other websites. A web page has different categories.
• A category table has a name, number of visits, and number of likes.
• A page table refers to a category, has a title, URL, and many views.
Design a form that populates the above database and displays it.
2. Consider the following tables:
WORKS(person-name,Company-name,Salary)
LIVES(Person_name, Street, City)
Assume Table data suitably. Design a Django webpage and include an option to
insert data into WORKS table by accepting data from the user using TextBoxes.
Also, include an option to retrieve the names of people who work for a
particular company along with the cities they live in (particular company name
must be accepted from the user).
ADDITIONAL EXERCISES
1. Assume a table “Institutes” with institute_id, name, and no_of_courses are the
fields. Create a web page that retrieves all the data from “Institutes” table
displays only Institute names in the list box. I want you to do these questions name them as q1, q2 , a1 as apps under the project lab9. Do what is asked only, keep it minimal and simple. The ui should be very basic.