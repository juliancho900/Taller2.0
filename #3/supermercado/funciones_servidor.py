import json

def menu():
    lista = ["Bienvenidos al supermercado La Economia","1.comprar productos", "2.ventas del dia", "3.inventarios", "4.salir"]
    cadena = json.dumps(lista)
    return cadena

def comprar_productos():
    lista = ["1. zanahoria   $ 2500","2. yuca   $ 1500", "3.pasta dental $ 3000", "4. cepillo dental $ 2000", "5. harina de trigo $1000", "6.pulpa de fruta $ 800", "7. fruta $ 1200", "8. arroz $ 1300", "9. papel $ 1800", "10. toallas $ 3500"]
    cadena = "comprar productos"
    return cadena

def ventas_dia():
    cadena = "ventas dia"
    return cadena

def inventarios():
    cadena = "inventarios"
    return cadena

