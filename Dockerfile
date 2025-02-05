FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the Python script into the container
COPY send_email.py .

# Install necessary Python libraries (if you need any external libraries)
# Example: RUN pip install some-library

# Run the Python script
CMD ["python", "send_email.py"]
