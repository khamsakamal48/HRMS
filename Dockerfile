# Use an official Python runtime as a parent image
FROM python:3

# Install Firefox
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A6DCF7707EBC211F && \
    echo "deb http://ppa.launchpad.net/ubuntu-mozilla-security/ppa/ubuntu bionic main"  > /etc/apt/sources.list.d/firefox.list && \
    apt-get update && \
    apt-get -y install firefox \
    --no-install-recommends

# Install cron
RUN apt-get -y install cron

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set cronjob
ADD cronjob /etc/cron.d/cronjob
RUN chmod 0644 /etc/cron.d/cronjob
RUN crontab /etc/cron.d/cronjob

# Start cron and let the container run indefinetely
CMD cron && tail -f /dev/null
