FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install pymysql

COPY . .

EXPOSE 8000

CMD ["python3", "app.py"]