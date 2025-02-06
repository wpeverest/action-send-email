FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the Python script into the container
COPY send_email.py .

# Run the Python script
CMD ["python", "send_email.py"]
