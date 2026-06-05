# Tareas y Backlog: MLtips (POC)

## Fase 1: Configuración Inicial y Documentación (Actual)
- [x] Crear estructura de documentación (`docs/`).
- [x] Redactar `requerimientos.md`.
- [x] Redactar `diseno.md` con arquitectura y modelo de datos.
- [x] Redactar `tareas.md` (este archivo).
- [x] Configurar dependencias (`requirements.txt`).
- [x] Configurar entorno Docker (`Dockerfile`).

## Fase 2: Desarrollo del Backend (Modelos y Base de Datos)
- [x] Configurar la estructura de la aplicación Flask (`app/`).
- [x] Implementar modelos de SQLAlchemy (`User`, `Product`, `Order`, `OrderItem`).
- [x] Crear script de inicialización de la base de datos (SQLite) y poblar con datos dummy (Shampoo, Acondicionador, Crema).

## Fase 3: Desarrollo del Frontend y Rutas
- [x] Crear el layout base (`base.html`) aplicando la paleta de colores CSS (Palo de rosa, verde suave, etc.).
- [x] Implementar vista de Catálogo de Productos (`index.html`).
- [x] Implementar la lógica del Carrito de Compras (usando sesiones de Flask).
- [x] Implementar vista del Carrito (`cart.html`).
- [x] Implementar vista simulada de Checkout/Registro básico.

## Fase 4: Despliegue y Pruebas
- [x] Probar la construcción del contenedor Docker localmente.
- [x] Ejecutar el contenedor y validar el flujo completo (Ver catálogo -> Añadir al carrito -> Pagar).
- [x] Documentar instrucciones de despliegue en Zorin OS en el `README.md`.
