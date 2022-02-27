FROM python:latest

WORKDIR /code

# Install dependencies

COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt

COPY . /code/