# Propuesta Formativa Obligatoria (PFO)  
## TP: Implementación de un Chat Básico Cliente-Servidor con Sockets y Base de Datos

### Descripción
Este trabajo práctico consiste en desarrollar un chat básico Cliente-Servidor utilizando **sockets en Python** y una **base de datos SQLite**.  
El servidor recibe mensajes de los clientes, los almacena en la base de datos y envía una confirmación con timestamp.  
El cliente se conecta al servidor, envía mensajes y muestra la respuesta del servidor.

---

### Objetivo
- Configurar un servidor de sockets en Python que reciba mensajes de clientes.  
- Guardar los mensajes en una base de datos SQLite.  
- Aplicar buenas prácticas de **modularización**, **comentarios claros** y **manejo de errores**.  

---

### Requisitos
- Python 3.x  
- Módulo `sqlite3` (incluido en la instalación estándar de Python)  

---

### Instalación
1. Clonar o descargar este repositorio.  
2. Ubicar los archivos `servidor.py` y `cliente.py` en la misma carpeta.  
3. (Opcional) Crear un entorno virtual:  
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux / Mac
   venv\Scripts\activate         # Windows

---

### Uso
1. Abrir una terminal y navegar a la carpeta del proyecto.
2. Ejecutar el servidor:  
   ```bash
   python servidor.py
   ```  
3. El servidor quedará escuchando en `localhost:5000`.
4. En otra terminal, ejecutar el cliente:  
   ```bash
   python cliente.py
   ```
5. Escribir mensajes en la terminal.
6. Ver las respuestas del servidor con timestamp.
7. Para salir, escribir `éxito` en el cliente.