# Use Alpine-based Python image
FROM python:3.13-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Set working directory
WORKDIR /app

# Install system dependencies for building Python packages
RUN apk add --no-cache gcc musl-dev libffi-dev python3-dev openssl-dev

# Create a virtual environment
RUN python -m venv $VIRTUAL_ENV

# Install Python packages inside the virtual environment
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Run the Python producer script
CMD ["python", "producer.py"]
