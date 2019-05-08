FROM python:3-alpine

RUN mkdir -p /var/www
COPY src /var/www/

CMD ["python", "/var/www/index.py"]
