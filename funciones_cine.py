import time
import os

palabra = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
asientos = [["O" for i in range(10)] for x in range(10)]


def menu_opciones(p_opcs):
    while True:
        print('\tMenu Cine-K\n\n\t1. Mostrar asiento\n\t2. Reservar un asiento\n\t3. Cancelar una reservación\n\t4. Salir\n')
        try:
            opc = int(input('\tIngrese una opción: '))
            if opc in p_opcs:
                return opc
            else:
                print(
                    'ERROR! debe ingresar una opcion valida, opciones validas (1,2,3,4)!')
            limpiar_pantalla_esperar()
        except:
            print('ERROR! debe ingresar un número entero!')


def mostrar_asiento_dispon_ocupados():
    print('Ver asientos cine-k!')
    limpiar_pantalla_esperar()
    cont = 0
    while True:
        print('Listado de asientos Cine-K\n\t')
        print('    1    2    3    4    5    6    7    8    9    10')
        for asiento in asientos:
            print(palabra[cont], asiento)
            cont = cont + 1
        mensaje = str(input('¿Desea salir? Ingrese ("S":si  o "N":no): '))
        if mensaje.upper() in ("S", "N"):
            if mensaje.upper() == "S":
                print('Saliendo.')
                limpiar_pantalla_esperar()
                break
            else:
                print('Redirigiendo ver asientos.')
                cont = 0
            limpiar_pantalla_esperar()
        else:
            print('ERROR! debe ingresar una opción valida, opciones validas("S" o "N")!')
            cont = 0
        time.sleep(2)
        os.system('cls')


def reserva_asiento():
    print('Reservar asiento!')
    limpiar_pantalla_esperar()
    cont = 0
    while True:
        print('Listado de asientos Cine-K\n\t')
        print('    1    2    3    4    5    6    7    8    9    10')
        for asiento in asientos:
            print(palabra[cont], asiento)
            cont = cont + 1

        while True:
            fila = str(
                input('Ingrese la fila ("A","B","C","D","E","F","G","H","I","J"): '))
            if fila.upper() in palabra:
                for i in range(len(palabra)):
                    if fila.upper() == palabra[i]:
                        fila = i
                        break
                print('Fila seleccionada correctamente')
                limpiar_pantalla_esperar()
                break
            else:
                print(
                    'ERROR! fila ingresada invalida, filas validas(A,B,C,D,E,F,G,H,I,J)!')
            limpiar_pantalla_esperar()

        while True:
            try:
                num_asiento = int(input('Ingrese el numero de asiento: '))
                if num_asiento in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
                    print('Asiento seleccionado correctamente')
                    limpiar_pantalla_esperar()
                    break
                else:
                    print(
                        'ERROR! debe ingresar un asiento valido, asiento valido (1,2,3,4,5,6,7,8,9,10)!')
                limpiar_pantalla_esperar()
            except:
                print('ERROR! debe ingresar un número entero!')

        if asientos[fila][num_asiento-1] == "O":
            asientos[fila][num_asiento-1] = "X"
            print('Asiento reservado!')
            limpiar_pantalla_esperar()
            break
        else:
            print('El Asiento no esta disponible!')
            time.sleep(2)
            os.system('cls')
            while True:
                mensaje = str(
                    input('¿Desea comprar otro asiento? Ingrese ("S":si  "N": para salir): '))
                if mensaje.upper() in ("S", "N"):
                    if mensaje.upper() == "S":
                        print('Cargando.')
                        limpiar_pantalla_esperar()
                        cont = 0
                        break
                    else:
                        print('Saliendo.')
                        limpiar_pantalla_esperar()
                        break
                else:
                    print(
                        'ERROR! debe ingresar una opcion valida, opciones validas("S" o "N")')

        if mensaje.upper() == "N":
            break


def cancelar_reservacion():
    print('Cancelar reservacion!')
    limpiar_pantalla_esperar()
    band = False
    for n in range(10):
        for a in range(10):
            if asientos[n][a] == "X":
                band = True
                break

    if band == True:
        cont = 0
        while True:
            print('Listado de asientos Cine-K\n\t')
            print('    1    2    3    4    5    6    7    8    9    10')
            for asiento in asientos:
                print(palabra[cont], asiento)
                cont = cont + 1

            while True:
                fila = str(input('Ingrese la fila (A,B,C,D,E,F,G,H,I,J): '))
                if fila.upper() in palabra:
                    for i in range(len(palabra)):
                        if palabra[i] == fila.upper():
                            fila = i
                            break
                    print('Fila seleccionada correctamente!')
                    break
                else:
                    print(
                        'ERROR! debe ingresar una fila valida, filas validas(A,B,C,D,E,F,G,H,I,J)')
                limpiar_pantalla_esperar()

            while True:
                try:
                    num_asiento = int(input("Ingrese el numero del asiento: "))
                    if num_asiento in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
                        print('Asiento seleccionado correctamente!')
                        limpiar_pantalla_esperar()
                        break
                    else:
                        print(
                            'ERROR! debe ingresar un nro asiento valido, nro de asiento valido(1,2,3,4,5,6,7,8,9,10)!')
                    limpiar_pantalla_esperar()
                except:
                    print('ERROR! debe ingresar un número entero!')

            if asientos[fila][num_asiento-1] == "X":
                asientos[fila][num_asiento-1] = "O"
                print('RESERVACIÓN CANCELADA!')
                break
            else:
                print('NO EXISTE RESERVACION PARA EL ASIENTO SELECCIONADO!')
                break
    else:
        print('No hay registro!')


def salir():
    for x in range(1, 4):
        print('Saliendo de Cine-k', ("."*x))
        limpiar_pantalla_esperar()


def limpiar_pantalla_esperar():
    time.sleep(1)
    os.system('cls')
