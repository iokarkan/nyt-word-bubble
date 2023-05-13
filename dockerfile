# Use an official Python runtime based on Debian 10 "buster" as a parent image
FROM python:3.10-slim-buster

# Set environment variables
ENV FLASK_APP app.py
ENV FLASK_CONFIG docker

# Add a new user "hostuser"
RUN adduser --disabled-password --gecos "" hostuser

# Set the working directory in the container to /home/hostuser
WORKDIR /home/hostuser

# Copy files into the working directory
COPY nyt_word_bubble nyt_word_bubble
COPY migrations migrations
COPY app.py config.py boot.sh ./

# Give execute permission to boot.sh
RUN chmod 755 ./boot.sh

# Change to non-root user
USER hostuser

# Copy requirements and .env file
COPY requirements.txt requirements.txt
COPY .env .env

# Create a Python virtual environment and install dependencies
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip setuptools
RUN venv/bin/pip install -r requirements.txt

# Expose port 5000 and set the Docker entrypoint to boot.sh
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
