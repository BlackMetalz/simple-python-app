# Use the latest Python Alpine image
FROM python:alpine

# Install any needed packages specified in requirements.txt
# --no-cache-dir: Do not use cache when installing packages to reduce the image size
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]