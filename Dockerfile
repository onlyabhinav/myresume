FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Set default PORT if not provided
ENV PORT=8080

# Expose port
EXPOSE 8080

# Run the application with gunicorn
CMD gunicorn --bind 0.0.0.0:${PORT} --workers 2 --threads 4 app:app
