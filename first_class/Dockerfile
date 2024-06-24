FROM python:3.10-alpine

RUN pip install --upgrade pip

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY requirements.txt /code/

RUN pip install -r requirements.txt

# Creating folders, and files for a project:
COPY . /code