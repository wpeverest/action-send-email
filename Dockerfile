# Use an official Python image as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/src/app

# Install necessary Python libraries
RUN pip install smtplib

# Copy the Python script into the container
COPY send_email.py .

# Set the default command to run when the container starts
ENTRYPOINT ["python", "send_email.py"]
