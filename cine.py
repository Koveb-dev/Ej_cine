# EJERCICIO CINE
from funciones_cine import *

print('Bienvenido a la app Cine-K')
limpiar_pantalla_esperar()


opciones = (1, 2, 3, 4)


while True:
    limpiar_pantalla_esperar()
    opc = menu_opciones((opciones))

    if opc == 1:
        mostrar_asiento_dispon_ocupados()
    elif opc == 2:
        reserva_asiento()
    elif opc == 3:
        cancelar_reservacion()
    else:
        salir()
        break
