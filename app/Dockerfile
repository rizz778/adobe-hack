
# Use the official Python image as a base
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variables (optional)
ENV PYTHONUNBUFFERED=1

# Default command (change maina.py to your entry point if needed)
CMD ["python", "maina.py"]
