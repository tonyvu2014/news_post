############################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM ubuntu

# File Author / Maintainer
MAINTAINER "TONY VU"


# Update the sources list
RUN sudo apt-get -y update

# Install basic applications
RUN sudo apt-get install -y tar git curl nano wget dialog net-tools build-essential supervisor
RUN mkdir -p /var/log/news_post
RUN mkdir -p /var/log/news_post/app.log
RUN mkdir -p /var/log/news_post/err.log

# Install Python and Basic Python Tools
RUN apt-get install -y python python-dev python-distribute python-pip

# Copy the application folder inside the container
COPY . /news_post

# Get pip to download and install requirements:
RUN pip install -r /news_post/requirements.txt


# Expose ports
EXPOSE 8000

# Set the default directory where CMD will execute
WORKDIR /news_post

# Set the default command to execute    
# when creating a new container
CMD gunicorn app:app
