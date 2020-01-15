FROM python:3-alpine

ADD . /

EXPOSE 8080

CMD ["python", "./server.py"]
