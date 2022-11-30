import smtplib
import functools
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pysnmp.hlapi import *

COMMASPACE = ', '
# Define params
rrdpath = '/home/kimi/PycharmProjects/p3/RRD/'
imgpath = '/home/kimi/PycharmProjects/p3/IMG/'
fname = 'trend.rrd'

mailsender = "dummycuenta3@gmail.com"
mailreceip = "dummycuenta3@gmail.com"
mailserver = 'smtp.gmail.com: 587'
password = 'dvduuffmlhspbmjj'

def send_alert_attached(subject, comunidad, host):

    conjunto = []

    """ Datos sistema op
    """
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(comunidad, mpModel=1),
        UdpTransportTarget((host, 161)),
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

    """ Datos version
    """
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(comunidad, mpModel=1),
        UdpTransportTarget((host, 161)),
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

    """ Datos nombre dispositivo
    """
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(comunidad, mpModel=1),
        UdpTransportTarget((host, 161)),
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


    """ Envía un correo electrónico adjuntando la imagen en IMG
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip
    mens = 'Sistema Operativo: '+conjunto[0]+', Version: '+conjunto[1]+', Nombre de dispositivo: '+conjunto[2]
    msg.attach(MIMEText(str(mens), 'plain'))
    fp = open(imgpath+'deteccionCPU.png', 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    fp = open(imgpath + 'deteccionRAM.png', 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    fp = open(imgpath + 'deteccionNET.png', 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    s = smtplib.SMTP(mailserver)

    s.starttls()
    # Login Credentials for sending the mail
    s.login(mailsender, password)

    s.sendmail(mailsender, mailreceip, msg.as_string())
    s.quit()
