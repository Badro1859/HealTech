# base image  
FROM python:3.10-slim

# setup environment variable  
ENV DockerHOME=/home/healtech-backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

# install all dependencies  
COPY requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt  

# copy whole project to your DockerHOME directory. 
COPY . .

# release port where the Django app runs  
EXPOSE 8000

# start server  
CMD python src/manage.py runserver  0.0.0.0:8000