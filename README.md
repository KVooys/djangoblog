# Djangoblog

First attempt at a blog page using Django, still in somewhat early alpha, so don't judge me yet. :)

This is mostly meant as a learning exercise. 

It is based on this tutorial: 

https://tutorial.djangogirls.org/en/

### How to setup:

1) Create a new Python environment with virtualenv/pipenv
2) pip install -r requirements.txt
3) Setup database: python manage.py makemigrations, followed by: python manage.py migrate
4) You need a superuser to create blog posts: python manage.py createsuperuser
5) python manage.py runserver - check if the homepage is working on http://127.0.0.1:8000
6) Login to http://127.0.0.1:8000/admin/ with your superuser account, then go back to the homepage. 
7) You can now add and edit posts!

Alternatively, run the Dockerized version using the Dockerfile:

1) docker build -t djangoblog:v1.0 .
2) docker run -d -p 8000:8000 --name djangoblog djangoblog:v1.0 
3) To create a superuser inside the container: docker exec -ti djangoblog bash; python3 manage.py createsuperuser; enter your credentials
    
### Features:
 
- Homepage with blog posts in order, newest on top
- Creating blog posts
- Access & edit blog post data

### TODO:

- Feature: add tags to blog posts
- Feature: login/register from the front-end
- Feature: leave comments on posts
- Improvement: Decouple config variables from code
- Improvement: use filters or search to find specific posts
