import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("", 35000))

server.listen(1)

socket_cliente, direccion = server.accept()

while True:

    mensaje_cliente = socket_cliente.recv(1024)
    if mensaje_cliente == "julian":
        print "Usuario Correcto"
    else:
        print "usuario incorrecto"

    clave = socket_cliente.recv(1024)
    if clave == "12345":
        print "clave correta"
        print 'Bienvenido'

        import archivo
        archivo.archivos()
        archivo.escribir()
    else:
        print "clave incorrecta"


    salir = socket_cliente.recv(1024)
    if salir == "Exit":
        break


print "vuelva pronto"
socket_cliente.close()
server.close()




'''
print str(direccion[0]) + " escribio: ", mensaje_cliente
mensaje_servidor = raw_input("Ingrese Respuesta al Cliente >> ")
socket_cliente.send(mensaje_servidor)
'''


