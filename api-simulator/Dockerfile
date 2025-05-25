FROM python:3.13-alpine

WORKDIR /simulator

RUN apk add --no-cache gcc musl-dev libffi-dev python3-dev openssl-dev

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY external_api_simulator.py .

CMD ["python", "external_api_simulator.py"]
