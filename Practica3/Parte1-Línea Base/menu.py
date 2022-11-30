import os
import threading
import rrdtool
from TrendUpdate import *
from trendGraphDetection import *

def menu_s():
    print('-----------Sistema de Administraciòn de Red---------------')
    print('--------Pràctica 3 - Monitorizar el rendimiento de un agente usando SNMP-----------')
    print('------------------Hernàndez Oble Axel---------------------')
    print('----------Boleta: 2020630219  Grupo: 4CM13------------')
    print('Menù:')
    print('1. Agregar')
    print('2. Salir')
    opcion = input('Escoja una opciòn: ')
    opcion = int(opcion)

    if opcion == 1:
        print("Digite el nombre de la comunidad")
        comu = input()
        print("Digite la ip")
        ippe = input()

        hilo1 = threading.Thread(target=update,
                                 args=(comu, ippe))
        hilo1.start()
        input('Pulse alguna tecla para continuar...')

        hilo2 = threading.Thread(target=grafi,
                                 args=(comu, ippe))
        hilo2.start()
        exit()

    elif opcion == 2:
        exit()
    else:
        print('Elija una opciòn correcta')
        input('Pulse alguna tecla para continuar...')
        os.system("clear")
        menu_s()
    os.system("clear")

menu_s()