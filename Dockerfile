

FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1


# Install gcc and other necessary packages
RUN apt-get update && apt-get install -y gcc libffi-dev musl-dev

WORKDIR /django



COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
