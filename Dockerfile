# Use the official Python base image with the desired version
FROM python:3.6.13

# Set the working directory within the container
WORKDIR /app

# Copy the project files to the container's working directory
COPY . /app

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your Flask app is running on
EXPOSE 8000

# Set the entry point to run the Flask app
CMD ["python", "main.py", "--port", "8000"]

