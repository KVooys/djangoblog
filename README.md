# Djangoblog

Attempt at a blog page using Django, still in somewhat early alpha, so don't judge me yet. :) This is mostly meant as a learning exercise. 

Following [12-factor app principles](https://12factor.net/).

### How to setup

1) Create a new Python environment with virtualenv/pipenv
2) pip install -r requirements.txt - if psycopg2 fails, follow these [instructions]([http://web.archive.org/web/20140615091953/http://goshawknest.wordpress.com/2011/02/16/how-to-install-psycopg2-under-virtualenv/)
3) Setup database: python manage.py makemigrations, followed by: python manage.py migrate
4) Collect static files: python manage.py collectstatic 
5) You need a superuser to create blog posts: python manage.py createsuperuser
6) python manage.py runserver - check if the homepage is working on http://127.0.0.1:8000
7) Login to http://127.0.0.1:8000/admin/ with your superuser account, then go back to the homepage. 
8) You can now add and edit posts!

Alternatively, run the Dockerized version using the Dockerfile:

1) docker build -t djangoblog:v1.0 .
2) docker run --rm -d -p 8000:8000 --name djangoblog djangoblog:v1.0 
3) To create a superuser inside the container: docker exec -ti djangoblog sh; python3 manage.py createsuperuser; enter your credentials
    
### Features
 
- Homepage with blog posts in order, newest on top
- Creating blog posts with POST API (or by logging in)
- Access & edit blog posts
- Uses PostgreSQL database
- Decoupled config variables from code using python-decouple
- Login/register from the front-end

### Future ideas

- Feature: add tags to blog posts
- Feature: leave comments on posts
- Improvement: use filters or search to find specific posts
- Improvement: prettify menu for login/register
