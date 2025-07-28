# Use the official Python image as a base, specify amd64 architecture
FROM --platform=linux/amd64 python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY ../../requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the 1b application code
COPY . ./1b

# Set environment variables (optional)
ENV PYTHONUNBUFFERED=1

# Entrypoint: process all PDFs in /app/input and output JSONs to /app/output
CMD ["python", "mainb.py"]
