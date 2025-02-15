# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del repositorio al contenedor
COPY . /app

# Instala las dependencias del bot
RUN pip install -r requirements.txt

# Comando para ejecutar el bot
CMD ["python", "Bot.py"]
