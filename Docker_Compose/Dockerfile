FROM python:3.7-alpine

# Set the working directory
WORKDIR /code

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Copy application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask application port
EXPOSE 5000

# Set the command to run the Flask app
CMD ["flask", "run"]
