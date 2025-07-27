FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8081

CMD ["python", "app.py", "--host", "127.0.0.1", "--port", "8081"]