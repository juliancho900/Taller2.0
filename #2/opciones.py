import os

L = []

def menu():
    lista = ['1.Listar', '2.Crear', '3.Modificar', '4.Eliminar', '5.salir']

    for i in lista:
        print i
menu()

def crear():
    opc = int(input("Selecione una Opcion: "))
    if (opc == 2):
        nombre=raw_input('ingrese el Nombre para Crear el Archivo')
        archivo = open(nombre+'.txt', 'w')
        archivo.close()
        print 'Archivo Creado Exitosamente'
crear()

def listar():
    opc = int(input("Selecione una Opcion: "))
    if (opc == 1):
      L.append(archivo)
      for i in L:
          print i
listar()


def modificar():
    opc = int(input("Selecione una Opcion: "))
    if (opc == 3):
        mod=raw_input('Ingrese el nombre del Archivo a modificar:   ')
        if(mod == 'Datos'):
            edicion = raw_input("Escriba lo que desea Ingresar al archivo: \n  ")
            outfile = open('Datos', 'a')
            outfile.write(edicion)


            infile = open('Datos', 'r')

            print(infile.read())



modificar()


def eliminar():
    opc = int(input("Selecione una Opcion: "))
    if (opc == 4):
        eli = raw_input('Ingrese el nombre del Archivo a eliminar:   ')
        if (eli == 'julio'):
            os.remove(eli)
            print('El archivo ha Sido Borrado')
eliminar()

def salir():
    opc = int(input("Selecione una Opcion: "))
    if (opc == 5):
        print 'Eligio salir'

salir()

