FROM python:3.9-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python3", "./src/telegram_bot.py"]