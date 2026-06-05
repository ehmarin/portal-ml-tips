# Usamos una imagen base ligera de Python optimizada
FROM python:3.11-slim

WORKDIR /app

# Copiamos e instalamos dependencias primero para aprovechar la caché de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del proyecto
COPY . .

EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]