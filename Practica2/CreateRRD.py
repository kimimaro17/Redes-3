#!/usr/bin/env python
import rrdtool
ret = rrdtool.create("segmentosRed.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:multiEnvia:COUNTER:120:U:U",
                     "DS:protoIp:COUNTER:120:U:U",
                     "DS:msjIcmp:COUNTER:120:U:U",
                     "DS:segTcp:COUNTER:120:U:U",
                     "DS:dataEnvia:COUNTER:120:U:U",
                     "RRA:AVERAGE:0.5:5:5",
                     "RRA:AVERAGE:0.5:1:1400")

if ret:
    print (rrdtool.error())
