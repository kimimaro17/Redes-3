import functools
from fpdf import FPDF
from datetime import date
from datetime import datetime
from pysnmp.hlapi import *

def genpdf(comunidad, ipe):

    conjunto = []

    def vers():
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(comunidad, mpModel=1),
            UdpTransportTarget((ipe, 161)),
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
            conjunto.append(arr[2] + arr[3])
        else:
            conjunto.append(arr[13] + arr[14])

    def nombred():
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(comunidad, mpModel=1),
            UdpTransportTarget((ipe, 161)),
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

    def outOct():
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(comunidad, mpModel=1),
            UdpTransportTarget((ipe, 161)),
            ContextData(),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.10.1'))
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

    def inOct():
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(comunidad, mpModel=1),
            UdpTransportTarget((ipe, 161)),
            ContextData(),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.16.1'))
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

    vers()
    nombred()
    outOct()
    inOct()
    today = datetime.now()

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    pdf.set_font('Arial', '', 20)
    pdf.set_text_color(130, 2, 2)
    pdf.text(x=20, y=20, txt='Administraciòn de Servicios en Red')
    pdf.text(x=20, y=30, txt='Pràctica 2')
    pdf.text(x=20, y=40, txt='Axel Hernàndez Oble')
    pdf.text(x=20, y=50, txt='Grupo: 4CM13')

    pdf.set_text_color(0, 0, 0)
    pdf.text(x=20, y=60, txt='RADIUS accounting data')
    pdf.text(x=20, y=70, txt='version: ' + conjunto[0])
    pdf.text(x=20, y=80, txt='device: server3')
    pdf.text(x=20, y=90, txt='description: Accounting Server 3')
    pdf.text(x=20, y=100, txt='date: ' + str(today))
    pdf.text(x=20, y=110, txt='defaultProtocol: radius')
    pdf.text(x=20, y=120, txt='rdate: ' + str(today))
    pdf.text(x=20, y=130, txt='#NAS-IP-Address')
    pdf.text(x=20, y=140, txt='4: ' + ipe)
    pdf.text(x=20, y=150, txt='#NAS-Port')
    pdf.text(x=20, y=160, txt='5: 161')
    pdf.text(x=20, y=170, txt='#NAS-Port-Type')
    pdf.text(x=20, y=180, txt='61: 2')
    pdf.text(x=20, y=190, txt='#User-Name')
    pdf.text(x=20, y=200, txt='1: ' + str(conjunto[1]))
    pdf.text(x=20, y=210, txt='#Acct-Status-Type')
    pdf.text(x=20, y=220, txt='40: 2')
    pdf.text(x=20, y=230, txt='#Acct-Delay-Time')
    pdf.text(x=20, y=240, txt='41: 14')
    pdf.text(x=20, y=250, txt='#Acct-Input-Octets')
    pdf.text(x=20, y=260, txt='42: ' + str(conjunto[3]))
    pdf.text(x=20, y=270, txt='#Acct-Output-Octets')
    pdf.text(x=20, y=280, txt='43: ' + str(conjunto[2]))
    pdf.add_page()
    pdf.text(x=20, y=20, txt='#Acct-Session-Id')
    pdf.text(x=20, y=30, txt='44: 185')
    pdf.text(x=20, y=40, txt='#Acct-Authentic')
    pdf.text(x=20, y=50, txt='45: 1')
    pdf.text(x=20, y=60, txt='#Acct-Session-Time')
    pdf.text(x=20, y=70, txt='46: 1238')
    pdf.text(x=20, y=80, txt='#Acct-Input-Packets')
    pdf.text(x=20, y=90, txt='47: 153')
    pdf.text(x=20, y=100, txt='#Acct-Output-Packets')
    pdf.text(x=20, y=110, txt='48: 148')
    pdf.text(x=20, y=120, txt='#Acct-Terminate-Cause')
    pdf.text(x=20, y=130, txt='49: 11')
    pdf.text(x=20, y=140, txt='#Acct-Multi-Session-Id')
    pdf.text(x=20, y=150, txt='50: 73')
    pdf.text(x=20, y=160, txt='#Acct-Link-Count')
    pdf.text(x=20, y=170, txt='51: 2')

    pdf.add_page()
    pdf.image('packetMulti.png', x=60, y=20, w=100, h=50)
    pdf.image('ipProtocol.png', x=60, y=70, w=100, h=50)
    pdf.image('msjICMP.png', x=60, y=120, w=100, h=50)
    pdf.image('segTCP.png', x=60, y=170, w=100, h=50)
    pdf.image('datSent.png', x=60, y=220, w=100, h=50)

    pdf.output('Reporte_Admin_' + str(today) + '.pdf')
