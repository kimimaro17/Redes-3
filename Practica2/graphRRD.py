import sys
import rrdtool
import time

def grafi():
    tiempo_actual = int(time.time())
    #Grafica desde el tiempo actual menos diez minutos
    tiempo_inicial = tiempo_actual - 720

    uno = rrdtool.graphv( "packetMulti.png",
                         "--start",str(tiempo_inicial),
                         "--end",str(tiempo_actual),
                         "--vertical-label=Segmentos",
                         "--title=Paquetes multicast enviados por la insterfaz de un agente \n Usando SNMP y RRDtools",
                         "DEF:mEnviados=segmentosRed.rrd:multiEnvia:AVERAGE",
                         "CDEF:escalaEn=mEnviados,8,*",
                         "LINE1:escalaEn#FF0000:Paquetes multicast")

    dos = rrdtool.graphv( "ipProtocol.png",
                         "--start",str(tiempo_inicial),
                         "--end",str(tiempo_actual),
                         "--vertical-label=Segmentos",
                         "--title=Paquetes IP suministrados en solicitudes \n Usando SNMP y RRDtools",
                         "DEF:ipEnviados=segmentosRed.rrd:protoIp:AVERAGE",
                         "CDEF:escalaIp=ipEnviados,8,*",
                         "LINE1:escalaIp#FF0000:Paquetes IP")

    tres = rrdtool.graphv( "msjICMP.png",
                         "--start",str(tiempo_inicial),
                         "--end",str(tiempo_actual),
                         "--vertical-label=Segmentos",
                         "--title=Mensajes ICMP que ha recibido el agente \n Usando SNMP y RRDtools",
                         "DEF:msjICMPrec=segmentosRed.rrd:msjIcmp:AVERAGE",
                         "CDEF:escalaMs=msjICMPrec,8,*",
                         "LINE1:escalaMs#FF0000:Mensajes ICMP")

    cuatro = rrdtool.graphv( "segTCP.png",
                         "--start",str(tiempo_inicial),
                         "--end",str(tiempo_actual),
                         "--vertical-label=Segmentos",
                         "--title=Segmentos retransmitidos con octetos \n Usando SNMP y RRDtools",
                         "DEF:segRet=segmentosRed.rrd:segTcp:AVERAGE",
                         "CDEF:escalaTCP=segRet,8,*",
                         "LINE1:escalaTCP#FF0000:Segmentos TCP")

    cinco = rrdtool.graphv( "datSent.png",
                         "--start",str(tiempo_inicial),
                         "--end",str(tiempo_actual),
                         "--vertical-label=Segmentos",
                         "--title=Datagramas enviados por el dispositivo \n Usando SNMP y RRDtools",
                         "DEF:dEnviados=segmentosRed.rrd:dataEnvia:AVERAGE",
                         "CDEF:escalaEn=dEnviados,8,*",
                         "LINE1:escalaEn#FF0000:Datagramas enviados")

    print(uno)
    print(dos)
    print(tres)
    print(cuatro)
    print(cinco)
