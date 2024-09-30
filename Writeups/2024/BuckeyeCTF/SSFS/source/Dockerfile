FROM python:3.12-alpine

RUN apk update

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY static ./static    
COPY templates ./templates
COPY app.py .

COPY flag.txt /flag.txt

EXPOSE 5000
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000", "-k", "eventlet", "--timeout", "500", "--workers", "4", "--access-logfile", "-"]