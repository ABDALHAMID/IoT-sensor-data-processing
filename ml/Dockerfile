FROM python:3.13-alpine

# Install build dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev python3-dev openssl-dev

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . .

# Run the training script
CMD ["python", "train_model.py"]
