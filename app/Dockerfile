# ./django-docker/app/Dockerfile
FROM python:3.8-buster
# set work directory
WORKDIR /opt/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /opt/app/requirements.txt 
RUN chmod +x /opt/app/requirements.txt
RUN pip install -r requirements.txt
# copy project
COPY . /opt/app/
CMD python manage.py runserver_plus --cert-file cert/server.cert --key-file cert/server.key 0.0.0.0:8000
