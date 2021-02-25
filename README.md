# Ecommerce_Assignment_AyushKC

This is lab for lab exam of ecommerce.

Some info reguarding Python, Django ,SQLite DB
Python: Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together.

SQL lite: 
SQLite is a C-language library that implements a small, fast, self-contained, high- reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world. SQLite is built into all mobile phones and most computers and comes bundled inside countless other applications that people use every day

Django:
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source

Summary:
This is a project made for lab exam purpose. The project uses default database provided by django. It consistes of one app module i.e exam_module Module. Also it has only one table that consists of exam date, exam name, description, exam status, total marks and pass marks. These datas can be viewed and edited by the admin of the system i.e superuser.

Some terminal codes:

for making virtual env:

      python3 -m venv vir-env
      source vir-env/bin/activate

      To delete
      deactivate
      rm -rf vir-env

to create a django project - 

    django-admin startproject ecommerce_project_name
    cd ecommerce_yourname to perform manage.py actions

migrating - 

    python manage.py makemigrations 
    python manage.py migrate 

to create new app:
            
    python manage.py startapp app_name

Features:
- We can do CRUD operation via Admin Panel
- There is one super user who manages the system
- You can create more users and assign them roles via the admin panel
- login system for admin and users which is handled by django admin with its default template

NOTE: Primary Keys
By default, Django adds an id field to each model, which is used as the primary key for that model. You can create your own primary key field by adding the keyword arg primary_key=True to a field.

