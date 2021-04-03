FROM python:3.7-alpine
MAINTAINER Himanshu Chauhan


# Setting PYTHONUNBUFFERED to a non empty value ensures that the python output is sent straight to terminal (e.g. your container log)
# without being first buffered and that you can see the output of your application (e.g. django logs) in real time.
ENV PYTHONUNBUFFERED 1

# Copying requirements.txt from directory to docker
COPY ./requirements.txt /requirements.txt

# installing requirements.txt in docker
RUN pip install -r /requirements.txt

# make a directory within docker image to store our app
RUN mkdir /app

# Switched to the app for default directory
WORKDIR /app

# copy from our local machine app folder to app folder in docker that we created
COPY ./ecomm /app

# We are creating a user to run our application in docker
RUN adduser -D user

#Switches docker to user we created
USER user