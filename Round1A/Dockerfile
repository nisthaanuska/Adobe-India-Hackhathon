# Use official Python slim image for amd64
FROM --platform=linux/amd64 python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies for PyMuPDF
RUN apt-get update && apt-get install -y \
    libmupdf-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy all project files into the container
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# (Optional) Create input/output folders if not mounted by Docker
RUN mkdir -p /app/input /app/output || true

# Set entrypoint to run the main script
ENTRYPOINT ["python", "main.py"]