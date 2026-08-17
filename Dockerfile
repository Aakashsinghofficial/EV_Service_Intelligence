FROM python:3.11-slim

WORKDIR /app

COPY Requirements.txt .

RUN pip install --no-cache-dir -r Requirements.txt

COPY App ./App
COPY Models ./Models

EXPOSE 8000

CMD ["uvicorn", "App.app:app", "--host", "0.0.0.0", "--port", "8000"]
