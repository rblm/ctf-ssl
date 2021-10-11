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
# install nginx
RUN apt-get -y update && apt-get -y install nginx
COPY ./config/nginx/nginx.conf /etc/nginx/nginx.conf.new
# copy project
COPY . /opt/app/
CMD /opt/app/scripts/run_server.sh
