import socket

# Configuración del cliente TCP/IP
def main():
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect(('127.0.0.1', 5000))
    except Exception as e:
        print(f"No se pudo conectar al servidor: {e}")
        return

    print("Conectado al servidor. Escriba 'éxito' para salir.")
    while True:
        mensaje = input("Mensaje: ")
        if mensaje.lower() == "éxito":
            break
        try:
            cliente.sendall(mensaje.encode('utf-8'))
            respuesta = cliente.recv(1024)
            print("Servidor:", respuesta.decode('utf-8'))
        except Exception as e:
            print(f"Error al enviar/recibir: {e}")
            break
    cliente.close()

if __name__ == "__main__":
    main()