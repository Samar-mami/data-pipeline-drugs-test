# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /data
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN apt-get update
#RUN pip install -r requirements.txt
COPY Pipfile ./Pipfile
COPY Pipfile.lock ./Pipfile.lock
RUN pip install pipenv
RUN pipenv install --ignore-pipfile --system
# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
#ENV NAME World

# Run app.py when the container launches
CMD ["python", "main.py"]
