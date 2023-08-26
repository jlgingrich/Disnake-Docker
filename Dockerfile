FROM python:3.11-alpine

# Data and logs should persist
VOLUME [ "/app/data" ]
VOLUME [ "/app/logs" ]

WORKDIR /app

# Install python requirements
RUN apk add git
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# This enables python-logging to actually show in the logs
ENV PYTHONUNBUFFERED true

COPY ./common.py .
COPY ./bot.py .
COPY ./main.py .
COPY ./exts ./exts

CMD ["python3", "main.py"]