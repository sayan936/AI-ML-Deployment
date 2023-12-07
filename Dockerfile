FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

COPY requirements.txt requirements.txt


# Install any needed packages specified in requirements.txt
RUN pip3 install  -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .


# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run your app using gunicorn
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]