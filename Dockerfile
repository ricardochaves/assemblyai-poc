FROM python:3.12-alpine

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt

CMD ["python", "main.py"]