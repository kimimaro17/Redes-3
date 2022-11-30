import rrdtool
ret = rrdtool.create("/home/kimi/PycharmProjects/p3/RRD/trend.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:CPUload:GAUGE:60:0:100", #tipo de dato GAUGE para que guarde cada 1 step todos los datos del buffer y le aplica una funciòn, el 0 y 100 son los los limites inferior y superior respectivamente
                     "DS:RAMuse:GAUGE:60:0:7000000",
                     "DS:NETrafsub:GAUGE:60:0:25000000",
                     "DS:NETrafbaj:GAUGE:60:0:25000000",
                     "RRA:AVERAGE:0.5:3:1440")#FUncion de consilodacion, cada 1 step y la base es de 24 filas
if ret:
    print (rrdtool.error())
