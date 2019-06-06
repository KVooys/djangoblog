# official Python image
FROM python:3.7-slim
MAINTAINER www.github.com/KVooys/djangoblog

# create root directory for our project
RUN mkdir /app

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
ADD . /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run on port 8000 inside the container and outside
EXPOSE 8000

# Run db migrations and start server
CMD python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000
