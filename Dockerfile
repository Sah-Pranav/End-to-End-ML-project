FROM python:3.11-slim

WORKDIR /app
COPY . /app

EXPOSE 5001

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]