# Use minimal linux image
FROM python:3.11-alpine

# Data and logs should always persist
VOLUME [ "/app/data" ]
VOLUME [ "/app/logs" ]

WORKDIR /app

# Install python requirements
RUN apk add git
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# This enables python-logging to actually show in the logs
ENV PYTHONUNBUFFERED true

# Transfer in files
COPY ./common.py .
COPY ./main.py .
COPY ./exts ./exts

ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]