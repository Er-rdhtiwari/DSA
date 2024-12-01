# Use the official Python 3.10 base image.
# This provides a lightweight Python runtime environment.
FROM python:3.10

# Expose port 5000 to allow communication with the Flask app.
# The application will listen on this port for incoming requests.
EXPOSE 5000

# Set the working directory inside the container to /app.
# This ensures that all subsequent commands are executed relative to this directory.
WORKDIR /app

# Install Flask globally in the container using pip.
# Flask is a lightweight web framework required to run the application.
RUN pip install flask

# Copy all files from the current directory (host machine) into the /app directory in the container.
# This includes the application code and any other required files.
COPY . .

# Define the command to run the Flask application.
# 'flask run --host=0.0.0.0' tells Flask to start the app and bind to all network interfaces.
CMD ["flask", "run", "--host=0.0.0.0"]

#docker build -t flask-app .
#docker run -p 5000:5000 flask-app
