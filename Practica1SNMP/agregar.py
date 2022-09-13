"""
"""#
import functools

import mysql.connector
from pysnmp.hlapi import *

def conseguir_datos():

    miCOnexion = mysql.connector.connect(host='localhost', user='root' ,passwd='PWD', db='monitoreo')

    print("Digite el nombre de la comunidad")
    comunidad = input()
    print("Digite la ip")
    ipe = input()
    print("Digite el puerto")
    puerto = input()
    puerto = int(puerto)
    print("Digite la version smnp a trabajar (Para version 1 pulsar 0, para version 2 pulsar 1)")
    version = input()
    if version == '0':
        version = int(version)
    elif version == '1':
        version = int(version)
    else:
        version = 1

    conjunto = []
    interfaces = []
    desc = []

    def dat_so():
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(comunidad, mpModel=version),
            UdpTransportTarget((ipe, puerto)),
            ContextData(),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0'))
        )
        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        if errorIndication:
            print(errorIndication)
            print('Digite una comunidad valida')
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in varBinds:
                datos = []
                for x in varBind:
                    datos.append(x)
        y = datos[1]
        y = str(y)
        arr = y.split()
        if arr[0] == 'Linux':
            conjunto.append(arr[0])
        else:
            conjunto.append(arr[12])

    def dat_verso():
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(comunidad, mpModel=version),
            UdpTransportTarget((ipe, puerto)),
            ContextData(),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0'))
        )
        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        if errorIndication:
            print(errorIndication)
            print('Digite una comunidad valida')
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in varBinds:
                datos = []
                for x in varBind:
                    datos.append(x)
        y = datos[1]
        y = str(y)
        arr = y.split()
        if arr[0] == 'Linux':
            conjunto.append(arr[2]+arr[3])
        else:
            conjunto.append(arr[13]+arr[14])

    def dat_contacto():
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(comunidad, mpModel=version),
            UdpTransportTarget((ipe, puerto)),
            ContextData(),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.1.4.0'))
        )
        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        if errorIndication:
            print(errorIndication)
            print('Digite una comunidad valida')
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in varBinds:
                datos = []
                for x in varBind:
                    datos.append(x)
        conjunto.append(datos[1])

    def dat_nombred():
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(comunidad, mpModel=version),
            UdpTransportTarget((ipe, puerto)),
            ContextData(),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.1.5.0'))
        )
        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        if errorIndication:
            print(errorIndication)
            print('Digite una comunidad valida')
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in varBinds:
                datos = []
                for x in varBind:
                    datos.append(x)
        conjunto.append(datos[1])

    def dat_location():
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(comunidad, mpModel=version),
            UdpTransportTarget((ipe, puerto)),
            ContextData(),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.1.6.0'))
        )
        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        if errorIndication:
            print(errorIndication)
            print('Digite una comunidad valida')
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in varBinds:
                datos = []
                for x in varBind:
                    datos.append(x)
        conjunto.append(datos[1])

    def dat_ni():
        datos=[]
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(comunidad, mpModel=version),
            UdpTransportTarget((ipe, puerto)),
            ContextData(),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.1.0'))
        )
        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        if errorIndication:
            print(errorIndication)
            print('Digite una comunidad valida')
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in varBinds:
                for x in varBind:
                    datos.append(x)
        conjunto.append(datos[1])

    def dat_inter():
        tam = int(conjunto[5])
        tam = tam + 1
        for n in range(1, tam):
            valor = str(n)
            iterator = getCmd(
                SnmpEngine(),
                CommunityData(comunidad, mpModel=version),
                UdpTransportTarget((ipe, puerto)),
                ContextData(),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.'+ valor))
            )
            errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
            if errorIndication:
                print(errorIndication)
                print('Digite una comunidad valida')
            elif errorStatus:
                print('%s at %s' % (errorStatus.prettyPrint(),
                                    errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            else:
                for varBind in varBinds:
                    for x in varBind:
                        if x == 1:
                            interfaces.append('up')
                        elif x == 2:
                            interfaces.append('down')
                        elif x == 3:
                            interfaces.append('testing')
                        elif x == 4:
                            interfaces.append('unknown')
                        elif x == 5:
                            interfaces.append('dormant')
                        elif x == 6:
                            interfaces.append('notPresent')
                        elif x == 7:
                            interfaces.append('lowerLayerDown')

    def dat_desin():
         tam = int(conjunto[5])
         tam = tam + 1
         for n in range(1, tam):
            valor = str(n)
            iterator = getCmd(
                SnmpEngine(),
                CommunityData(comunidad, mpModel=version),
                UdpTransportTarget((ipe, puerto)),
                ContextData(),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.'+ valor))
            )
            errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
            if errorIndication:
                print(errorIndication)
                print('Digite una comunidad valida')
            elif errorStatus:
                print('%s at %s' % (errorStatus.prettyPrint(),
                                    errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            else:
                for varBind in varBinds:
                    datos = []
                    for x in varBind:
                        datos.append(x)
                    desc.append(datos[1])

    def inserDispo():
        cur = miCOnexion.cursor()
        cur.execute("select IDispo From Dispositivos where so = '{0}' and version = '{1}' and nombre = '{2}' and contacto = '{3}' and ubicacion = '{4}' and ninter = '{5}'".format(conjunto[0], conjunto[1], conjunto[2], conjunto[3], conjunto[4], conjunto[5]))
        selec = cur.fetchone()
        if selec == None:
            cur.execute("insert into Dispositivos(host, comunidad, puerto, so, version, nombre, contacto, ubicacion, ninter) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')".format(ipe, comunidad, puerto, conjunto[0], conjunto[1], conjunto[2], conjunto[3], conjunto[4],conjunto[5]))
            miCOnexion.commit()
        else:
            print("El dispositivo actualmente esta dentro del registro, se procedera a actualizar los datos")
            cur.execute("update Dispositivos set so = '{0}', version = '{1}', nombre = '{2}', contacto = '{3}', ubicacion = '{4}', ninter = '{5}' where IDispo = '{5}'".format(conjunto[0], conjunto[1], conjunto[2], conjunto[3], conjunto[4], conjunto[5], selec[0]))
            miCOnexion.commit()
        cur.close()

    def inserInter():
        cur = miCOnexion.cursor()
        cur.execute("select IDispo From Dispositivos where so = '{0}' and version = '{1}' and nombre = '{2}' and contacto = '{3}' and ubicacion = '{4}' and ninter = '{5}'".format(conjunto[0], conjunto[1], conjunto[2], conjunto[3], conjunto[4], conjunto[5]))
        selec = cur.fetchone()
        cur.execute("select id From Interfaces where IDispo = '{0}'".format(selec[0]))
        aba = cur.fetchall()
        if aba == []:
            for count, ele in enumerate(interfaces):
                cur = miCOnexion.cursor()
                cur.execute("insert into Interfaces(IDispo, descripcion, estado) values ('{0}','{1}','{2}')".format(selec[0],desc[count],ele))
                miCOnexion.commit()
                cur.close()
        else:
            for count, ele in enumerate(interfaces):
                pe = functools.reduce(lambda sub, te: sub * 10 + te, aba[count])
                cur = miCOnexion.cursor()
                cur.execute("update Interfaces set descripcion = '{0}', estado = '{1}' where id = '{2}'".format(desc[count],ele,pe))
                miCOnexion.commit()
                cur.close()

    dat_so()
    dat_verso()
    dat_nombred()
    dat_contacto()
    dat_location()
    dat_ni()
    dat_inter()
    dat_desin()

    inserDispo()
    inserInter()

    print('Datos guardados')
