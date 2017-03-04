import datetime

def archivos():
    archivo = open("Registro.txt", 'a')
    archivo.close()

def escribir():
    archivo = open("Registro.txt", "a", )

    nombre = raw_input('ingrese Nombre: ')
    archivo.write('nombre: ')
    archivo.write(nombre)


    contrasena = raw_input('ingrese contrasena: ')
    archivo.write('\ncontrasena: ')
    archivo.write(contrasena)

    fecha = str(datetime.datetime.now())
    archivo.write('\n:Fecha y Hora ')
    archivo.write(fecha)

archivos()
escribir()
