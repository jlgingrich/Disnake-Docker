FROM python:3.11-alpine

# Data and logs should persist
VOLUME [ "/app/data" ]
VOLUME [ "/app/logs" ]

WORKDIR /app

RUN pip install python-dotenv
RUN pip install disnake
RUN pip install PyNaCl

# This enables python-logging to actually show in the logs
ENV PYTHONUNBUFFERED true

COPY ./common.py .
COPY ./bot.py .
COPY ./main.py .
COPY ./cogs ./cogs

CMD ["python3", "main.py"]