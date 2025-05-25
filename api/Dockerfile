FROM python:3.13-alpine

# Install build dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev python3-dev openssl-dev

WORKDIR /api

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY producer.py .

CMD ["python", "producer.py"]



