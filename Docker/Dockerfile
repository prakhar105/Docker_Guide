# Use a specific version of Python
FROM python:3.8.3-alpine

# Set the working directory in the container
WORKDIR /app

# Copy requirements first to leverage Docker caching
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the application code
COPY ./app.py .

# Define the command to run the application
CMD ["python", "app.py"]