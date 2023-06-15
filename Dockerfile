# Use an official Python runtime as a parent image
FROM python:3.11.1

# Set the working directory in the container
WORKDIR /app

# Add current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install cron
RUN apt-get update && apt-get -y install cron

# Make  fetch script executable
RUN chmod +x /app/fetch.py

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/fetch-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/fetch-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log

# Make port 80 available to the world outside this container
EXPOSE 5000

# Run the application when the container launches
CMD ["python", "app.py"]
