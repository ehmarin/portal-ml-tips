# Requerimientos: MLtips (POC E-commerce)

## 1. Requisitos Funcionales
*   **Catálogo de Productos:** El sistema debe mostrar un catálogo con al menos tres productos iniciales (Shampoo, Acondicionador, Crema para peinar).
*   **Detalle de Producto:** Cada producto debe mostrar su nombre, descripción, precio y una imagen representativa.
*   **Carrito de Compras:** Los usuarios deben poder agregar productos al carrito, ver el resumen de su compra (cantidad, subtotal, total) y proceder al pago.
*   **Gestión de Usuarios:** Los usuarios deben poder registrarse y/o iniciar sesión para completar una compra.
*   **Gestión de Órdenes:** El sistema debe registrar las órdenes de compra generadas, asociándolas al usuario correspondiente.

## 2. Requisitos No Funcionales
*   **Arquitectura Base:** La aplicación debe estar construida usando Python y el framework Flask.
*   **Despliegue Contenerizado:** El proyecto debe ser empaquetado en un contenedor Docker, optimizado para ejecutarse en el servidor Tierra (Sistema Operativo Zorin).
*   **Base de Datos (POC):** El sistema utilizará SQLite local (gestionado vía SQLAlchemy) para almacenar datos durante la prueba de concepto. Esta base de datos debe ser fácilmente migrable a una solución SQL más robusta (LEAZ) en el futuro.
*   **Estética Visual:** La interfaz de usuario debe utilizar una paleta de colores centrada en "Palo de Rosa", con contrastes suaves (verde, azul, naranja).
*   **Diseño Responsivo:** La interfaz debe ser funcional tanto en pantallas de escritorio como en dispositivos móviles (responsivo).
