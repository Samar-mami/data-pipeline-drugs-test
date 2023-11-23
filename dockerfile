FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy the Pipfiles to the working directory
COPY Pipfile Pipfile.lock /app/

# Install pipenv
RUN pip install pipenv

# Install dependencies
RUN pipenv install --ignore-pipfile --deploy --system --python $(which python3)
RUN pipenv install pandas

# Copy the rest of the application files
COPY . /app

# Set environment variables
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Expose port 80
EXPOSE 80

# Set the command to run your application
CMD ["pipenv", "run", "python", "drug_analyzer.py"]
