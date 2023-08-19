# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install required dependencies
RUN apt-get update && \
    apt-get install -y libgl1 libglib2.0-0

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Expose the port that the app runs on
EXPOSE 8080

# Define the command to run the app when the container starts
CMD ["python", "app.py"]
