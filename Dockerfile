# Use official Python image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire app
COPY . .

# Streamlit default port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "streamlit_app/app.py"]
