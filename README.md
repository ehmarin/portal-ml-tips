# portal-ml-tips

Prueba de Concepto (POC) para la aplicación web orientada a e-commerce **MLtips**.

## Requisitos Previos
- Docker instalado en el servidor Tierra (Sistema Operativo Zorin).
- Puerto 5000 disponible.

## Instrucciones de Despliegue con Docker (Fase 4)

Abre una terminal en tu Visual Studio Code (asegúrate de estar en la raíz del proyecto, donde se encuentra el `Dockerfile`) y ejecuta los siguientes pasos:

### 1. Construir la imagen de Docker
Este comando leerá el Dockerfile y preparará el entorno con Python y Flask:
```bash
docker build -t mltips-app .
```

### 2. Inicializar la Base de Datos con datos Dummy
Usaremos un contenedor efímero para correr el script de inicialización y crear el archivo `mltips.db` que persistirá en tu directorio:
```bash
docker run --rm -v $(pwd):/app mltips-app python init_db.py
```
*(Nota: Si por algún motivo usas una terminal de Windows conectada a Tierra, cambia `$(pwd)` por `${PWD}`)*

### 3. Ejecutar la Aplicación
Levantaremos el contenedor mapeando el puerto 5000 de Tierra hacia el 5000 del contenedor:
```bash
docker run -d -p 5000:5000 -v $(pwd):/app --name portal-mltips mltips-app
```

### 4. Validar el funcionamiento
Abre un navegador en Tierra (o desde Mercurio apuntando a la IP de Tierra) e ingresa a:
`http://localhost:5000` (o `http://192.168.31.10:5000`)

## Detener y Limpiar el Contenedor
Si necesitas detener la aplicación en el futuro, ejecuta:
```bash
docker stop portal-mltips
docker rm portal-mltips
```
