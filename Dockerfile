FROM python:3.10

WORKDIR /usr/src/
COPY . .
RUN pip3 install -r requirements.txt