import time
import rrdtool
from getSNMP import consultaSNMP

def update(comunidad,host):
    rrdpath = '/home/kimi/PycharmProjects/p3/RRD/'
    carga_CPU = 0
    memoram = 0
    netraf = 0

    while 1:
        carga_CPU1 = int(consultaSNMP(comunidad,host,'1.3.6.1.2.1.25.3.3.1.2.196608'))
        carga_CPU2 = int(consultaSNMP(comunidad,host,'1.3.6.1.2.1.25.3.3.1.2.196609'))
        carga_CPU = carga_CPU1 + carga_CPU2
        carga_CPU = carga_CPU/2
    #el ultimo numero sacarlo con un walk (esta en teams)

        memoram1 = int(consultaSNMP(comunidad, host, '1.3.6.1.4.1.2021.4.5.0'))
        memoram2 = int(consultaSNMP(comunidad, host, '1.3.6.1.4.1.2021.4.6.0'))
        memoram = memoram1 - memoram2


        netraf1 = int(consultaSNMP(comunidad, host, '1.3.6.1.2.1.2.2.1.16.3'))
        netraf2 = int(consultaSNMP(comunidad, host, '1.3.6.1.2.1.2.2.1.10.3'))


        valor = "N:" + str(carga_CPU) + ':' + str(memoram) + ':' + str(netraf1) + ':' + str(netraf2)
        print (valor)
        rrdtool.update(rrdpath+'trend.rrd', valor)
        #rrdtool.dump(rrdpath+'trend.rrd','trend.xml')

        time.sleep(5)

    if ret:
        print (rrdtool.error())
        time.sleep(300)
