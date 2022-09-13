from agregar import *
from borrar import *
from pdf import *
import os

def menu_s():
    print('-----------Sistema de Administraciòn de Red---------------')
    print('--------Pràctica 1 - Adquisiciòn de Informaciòn-----------')
    print('------------------Hernàndez Oble Axel---------------------')
    print('----------Boleta: 2020630219  Grupo: 4CM13------------')
    print('Menù:')
    print('1. Agregar/Actualizar agente')
    print('2. Eliminar agente')
    print('3. Mostrar reporte')
    print('4. Salir')
    opcion = input('Escoja una opciòn: ')
    opcion = int(opcion)

    if opcion == 1:
        conseguir_datos()
    elif opcion == 2:
        borrar()
    elif opcion == 3:
        gen()
    elif opcion == 4:
        exit()
    else:
        print('Elija una opciòn correcta')
        input('Pulse alguna tecla para continuar...')
        os.system("clear")
        menu_s()
    input('Pulse alguna tecla para continuar...')
    os.system("clear")
    menu_s()

menu_s()
