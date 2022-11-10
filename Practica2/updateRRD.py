import time
import rrdtool
from getSNMP import consultaSNMP

def agg(comunidad, ipe):
    while 1:
        multicast_sent_agent = int(
            consultaSNMP(comunidad,ipe,
                         '1.3.6.1.2.1.2.2.1.12.2'))
                         #'1.3.6.1.2.1.2.2.1.12.1'))
        ip_soli_trans = int(
            consultaSNMP(comunidad,ipe,
                         '1.3.6.1.2.1.4.9.0'))
                         #'1.3.6.1.2.1.4.10.0'))
        icmp_sent_agent = int(
            consultaSNMP(comunidad, ipe,
                         '1.3.6.1.2.1.5.9.0'))
                         #'1.3.6.1.2.1.5.1.0'))
        tcp_retrans_s = int(
            consultaSNMP(comunidad, ipe,
                         '1.3.6.1.2.1.6.12.0'))
                         #'1.3.6.1.2.1.6.12.0'))
        udp_datagrams_dis = int(
            consultaSNMP(comunidad, ipe,
                         '1.3.6.1.2.1.7.4.0'))
                         #'1.3.6.1.2.1.7.4.0'))
        valor = "N:" + str(multicast_sent_agent) + ':' + str(ip_soli_trans) + ':' + str(icmp_sent_agent) + ':' + str(tcp_retrans_s) + ':' + str(udp_datagrams_dis)
        print (valor)
        rrdtool.update('segmentosRed.rrd', valor)
       # rrdtool.dump('traficoRED.rrd','traficoRED.xml')
        time.sleep(1)

    if ret:
        print (rrdtool.error())
        time.sleep(300)
