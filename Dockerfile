FROM python:3.11.3-alpine

WORKDIR /app

COPY requirements.txt .

ENV TZ=America/Fortaleza

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "main.py"]
