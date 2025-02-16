# Usa una imagen de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos del repositorio a /app
COPY . /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Ejecuta el bot
CMD ["python", "Bot.py"]
