# Use minimal linux image
FROM python:3.11-alpine

# Fix CVE-2023-5752⁠
RUN python3.11 -m pip install --upgrade pip

# Install packages via pypi and git
RUN apk add git
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt
RUN apk del git

# Configure directories
RUN mkdir -p /app/data
RUN mkdir -p /app/logs

WORKDIR /app

# Expose volumes
VOLUME data
VOLUME logs

# Import app code
COPY ./src core

# Allow overwriting of entrypoint
CMD ["python", "core/main.py"]
