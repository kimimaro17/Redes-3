import os
from pdf import *
from updateRRD import *
import threading
import rrdtool
from graphRRD import *

def menu_s():
    print('-----------Sistema de Administraciòn de Red---------------')
    print('--------Pràctica 2 - Administraciòn de Informaciòn-----------')
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
        print("Digite el año para la contabilidad")
        an = input()
        an = int(an)
        print("Digite el mes (en numero)")
        mes = input()
        mes = int(mes)
        print("Digite el dia (en numero)")
        dia = input()
        dia = int(dia)
        print("Digite la hora (24hrs)")
        hora = input()
        hora = int(hora)

        hilo1 = threading.Thread(target=agg,
                                 args=(comu, ippe))
        hilo1.start()
        input('Pulse alguna tecla para continuar...')

        last_update = rrdtool.lastupdate("segmentosRed.rrd")
        # Grafica desde la última lectura menos cinco minutos
        print(last_update)
        tiempo_inicial = int(last_update['date'].timestamp()) - 300
        print(tiempo_inicial)
        rrdtool.dump("segmentosRed.rrd", "segmentosRed.xml")
        result = rrdtool.fetch("segmentosRed.rrd", "-s," + str(tiempo_inicial), "LAST")

        grafi()
        genpdf(comu, ippe)
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