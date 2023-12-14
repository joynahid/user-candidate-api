FROM python:3.9-slim AS builder

# Update instance and pip
RUN apt update \
    && apt upgrade -y \
    && pip install -U pip

WORKDIR /app

# Copy local requirements.txt to instance's Workdir /app
COPY requirements.txt ./

# Install all the python dependencies
RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0" ]
