# Base Dockerfile
# syntax=docker/dockerfile:1
FROM python:3.11
# Update default packages
RUN apt-get update

# Get Ubuntu packages
# python3-dev may be required to get PyYaml to install
RUN apt-get install -y \
    build-essential \
    python3-dev \
    curl
# Update new packages
RUN apt-get update

# Now install python requirements
WORKDIR /app
COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r rtdrequirements.txt
RUN python3 -m pip install .

# Main application
# run this one if there are problems starting the app with the line above
ENTRYPOINT ["tail", "-f", "/dev/null"]
