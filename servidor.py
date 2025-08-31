import socket
import sqlite3
from datetime import datetime

# Configuración de la base de datos SQLite
def inicializar_db():
    try:
        conn = sqlite3.connect('chat.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mensajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido TEXT NOT NULL,
                fecha_envio TEXT NOT NULL,
                ip_cliente TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error al inicializar la base de datos: {e}")
        exit(1)

# Guardar mensaje en la base de datos
def guardar_mensaje(contenido, fecha_envio, ip_cliente):
    try:
        conn = sqlite3.connect('chat.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO mensajes (contenido, fecha_envio, ip_cliente)
            VALUES (?, ?, ?)
        ''', (contenido, fecha_envio, ip_cliente))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error al guardar mensaje: {e}")

# Configuración del socket TCP/IP
def inicializar_socket():
    try:
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.bind(('127.0.0.1', 5000))
        servidor.listen(5)
        print("Servidor escuchando en 127.0.0.1:5000")
        return servidor
    except OSError as e:
        print(f"Error al iniciar el socket: {e}")
        exit(1)

# Aceptar conexiones y recibir mensajes
def manejar_conexiones(servidor):
    while True:
        try:
            cliente, direccion = servidor.accept()
            print(f"Conexión desde {direccion}")
            while True:
                datos = cliente.recv(1024)
                if not datos:
                    break
                mensaje = datos.decode('utf-8')
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                guardar_mensaje(mensaje, timestamp, direccion[0])
                respuesta = f"Mensaje recibido: {timestamp}"
                cliente.sendall(respuesta.encode('utf-8'))
            cliente.close()
        except Exception as e:
            print(f"Error durante la conexión: {e}")

if __name__ == "__main__":
    inicializar_db()
    servidor = inicializar_socket()
    manejar_conexiones(servidor)