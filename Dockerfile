# Gunakan base image resmi Python
FROM python:3.11-slim

# Set working directory di dalam container
WORKDIR /app

# Copy file requirements.txt ke working directory
COPY requirements.txt .

# Install dependencies dari requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh kode project ke working directory
COPY . .

# Expose port 8000 yang digunakan oleh FastAPI
EXPOSE 8000

# Perintah untuk menjalankan aplikasi
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
