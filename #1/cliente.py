import socket

cliente = socket.socket()

"""direccion ip servidor, puerto  servidor"""

cliente.connect(("localhost", 35000))

while True:

    mensaje_cliente = raw_input("ingrese su nombre: ")
    cliente.send(mensaje_cliente)

    clave = raw_input("ingrese su contrasena: ")
    cliente.send(clave)

    if (mensaje_cliente == 'julian' and clave == '12345'):
        print "CALCULADORA"

    else:
        print'No puede Ingresar'
        break

    lista = ['1.suma', '2.Resta', '3.Multiplicacion', '4.Division', '5.salir']

    for i in lista:
            print i


    import calculos

    calculos.suma()
    calculos.resta()
    calculos.producto()
    calculos.division()



    if mensaje_cliente == "Exit":

        break



print "vuelva cuando quiera"
cliente.close()
















