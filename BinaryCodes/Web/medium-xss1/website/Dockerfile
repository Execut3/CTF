# Dockerfile
FROM python:2.7
WORKDIR /website
COPY . .
COPY manage.py requirements.txt /app/
RUN pip install -r requirements.txt
EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
