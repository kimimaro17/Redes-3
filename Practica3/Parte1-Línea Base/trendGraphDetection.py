import sys
import rrdtool
import time
import datetime
from  Notify import send_alert_attached
import time
rrdpath = '/home/kimi/PycharmProjects/p3/RRD/'
imgpath = '/home/kimi/PycharmProjects/p3/IMG/'

def grafi(comunidad, host):
    def generarGrafica(ultima_lectura):
        tiempo_final = int(ultima_lectura)
        tiempo_inicial = tiempo_final - 1800
        ret = rrdtool.graphv( imgpath+"deteccionCPU.png",
                         "--start",str(tiempo_inicial),
                         "--end",str(tiempo_final),
                         "--vertical-label=Cpu load",
                        '--lower-limit', '0',
                        '--upper-limit', '100',
                        "--title=Carga del CPU del agente Usando SNMP y RRDtools \n Detección de umbrales Maquina de Axel Hernandez",
                        "DEF:cargaCPU="+rrdpath+"trend.rrd:CPUload:AVERAGE",
                         "VDEF:cargaMAX=cargaCPU,MAXIMUM",
                         "VDEF:cargaMIN=cargaCPU,MINIMUM",
                         "VDEF:cargaSTDEV=cargaCPU,STDEV",
                         "VDEF:cargaLAST=cargaCPU,LAST",
                         "CDEF:umbral20=cargaCPU,20,LT,0,cargaCPU,IF",
                         "CDEF:umbral50=cargaCPU,50,LT,0,cargaCPU,IF",
                         "CDEF:umbral70=cargaCPU,70,LT,0,cargaCPU,IF",
                         "AREA:cargaCPU#00FF00:Carga del CPU",
                         "AREA:umbral50#FF9F00:Carga CPU mayor de 50",
                         "HRULE:20#563AFF:Umbral  20%",
                         "HRULE:50#FF0000:Umbral  50%",
                         "HRULE:70#000000:Umbral  70%",
                         "PRINT:cargaLAST:%6.2lf",
                         "GPRINT:cargaMIN:%6.2lf %SMIN",
                         "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST:%6.2lf %SLAST" )

        ramm = rrdtool.graphv(imgpath + "deteccionRAM.png",
                             "--start", str(tiempo_inicial),
                             "--end", str(tiempo_final),
                             "--vertical-label=Ram load",
                             '--lower-limit', '0',
                             '--upper-limit', '6000000',
                             "--title=Carga de RAM del agente Usando SNMP y RRDtools \n Detección de umbrales Maquina de Axel Hernandez",
                             "DEF:cargaRAM=" + rrdpath + "trend.rrd:RAMuse:AVERAGE",
                             "VDEF:cargaMAX=cargaRAM,MAXIMUM",
                             "VDEF:cargaMIN=cargaRAM,MINIMUM",
                             "VDEF:cargaSTDEV=cargaRAM,STDEV",
                             "VDEF:cargaLAST=cargaRAM,LAST",
                              "CDEF:umbral20=cargaRAM,3515000,LT,0,cargaRAM,IF",
                             "CDEF:umbral50=cargaRAM,3515000,LT,0,cargaRAM,IF",
                              "CDEF:umbral85=cargaRAM,3515000,LT,0,cargaRAM,IF",
                             "AREA:cargaRAM#00FF00:Carga de RAM",
                             "AREA:umbral50#FF9F00:Carga RAM mayor de 50",
                            "HRULE:1515000#563AFF:Umbral  20%",
                             "HRULE:3515000#FF0000:Umbral  50%",
                             "HRULE:5515000#000000:Umbral  85%",
                             "PRINT:cargaLAST:%6.2lf",
                             "GPRINT:cargaMIN:%6.2lf %SMIN",
                             "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                             "GPRINT:cargaLAST:%6.2lf %SLAST")

        nett = rrdtool.graphv(imgpath + "deteccionNET.png",
                             "--start", str(tiempo_inicial),
                             "--end", str(tiempo_final),
                             "--vertical-label=Network load",
                             '--lower-limit', '0',
                             '--upper-limit', '25000000',
                             "--title=Carga de NET del agente Usando SNMP y RRDtools \n Detección de umbrales Maquina de Axel Hernandez",
                             "DEF:cargaNETSubida=" + rrdpath + "trend.rrd:NETrafsub:AVERAGE",
                             "DEF:cargaNETBajada=" + rrdpath + "trend.rrd:NETrafbaj:AVERAGE",
                             "VDEF:cargaMAX=cargaNETSubida,MAXIMUM",
                             "VDEF:cargaMIN=cargaNETSubida,MINIMUM",
                             "VDEF:cargaSTDEV=cargaNETSubida,STDEV",
                             "VDEF:cargaLAST=cargaNETSubida,LAST",
                              "CDEF:umbral20=cargaNETSubida,6500000,LT,0,cargaNETSubida,IF",
                             "CDEF:umbral50=cargaNETSubida,12500000,LT,0,cargaNETSubida,IF",
                              "CDEF:umbral85=cargaNETSubida,20000000,LT,0,cargaNETSubida,IF",
                             "LINE:cargaNETSubida#FF9F00:Carga de NET",
                             "LINE:cargaNETBajada#00FF00:Bajada de NET",
                              "HRULE:6500000#563AFF:Umbral  20%",
                             "HRULE:12500000#FF0000:Umbral  50%",
                              "HRULE:20000000#000000:Umbral  85%",
                             "PRINT:cargaLAST:%6.2lf",
                             "GPRINT:cargaMIN:%6.2lf %SMIN",
                             "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                             "GPRINT:cargaLAST:%6.2lf %SLAST")
        print (ret)
        print (ramm)
        print (nett)

    while (1):
        ultima_actualizacion = rrdtool.lastupdate(rrdpath + "trend.rrd")
        timestamp=ultima_actualizacion['date'].timestamp()
        dato=ultima_actualizacion['ds']["CPUload"]
        dato1= ultima_actualizacion['ds']["RAMuse"]
        dato2= ultima_actualizacion['ds']["NETrafsub"]
        print(dato)
        print(dato1)
        print(dato2)
        if dato> 20 :
            if dato> 50 :
                if dato> 70 :
                    generarGrafica(int(timestamp))
                    send_alert_attached("Sobrepasa los tres umbrales", comunidad, host)
                    print("sobrepasa los tres umbrales")
                else:
                    generarGrafica(int(timestamp))
                    send_alert_attached("Sobrepasa los dos primeros umbrales",comunidad, host)
                    print("sobrepasa los dos primeros umbrales")
            else:
                generarGrafica(int(timestamp))
                send_alert_attached("Sobrepasa el primer umbral", comunidad, host)
                print("sobrepasa el primer umbral")
            break
        time.sleep(20)
