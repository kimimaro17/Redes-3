from fpdf import FPDF
import mysql.connector

def gen():
    print('============================================================================')

    miCOnexion = mysql.connector.connect(host='localhost', user='root', passwd='PWD', db='monitoreo')
    cur = miCOnexion.cursor()

    cur.execute("select * From Dispositivos")
    selec = cur.fetchall()

    for fila in selec:
        print(fila)
    print('============================================================================')
    print('Escriba el id (primer dato) del dispositivo del que quiere hacer un reporte de sus interfaces')
    ide = input('ID: ')
    ide = int(ide)

    cur.execute("select * From Interfaces where IDispo = '{0}'".format(ide))
    si = cur.fetchall()

    cur.execute("select nombre From Dispositivos where IDispo = '{0}'".format(ide))
    name = cur.fetchone()

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    pdf.set_font('Arial', '', 20)
    pdf.set_text_color(130, 2, 2)
    pdf.text(x=20, y=20, txt='Administraciòn de Servicios en Red')
    pdf.text(x=20, y=30, txt='Pràctica 1')
    pdf.text(x=20, y=40, txt='Axel Hernàndez Oble')
    pdf.text(x=20, y=50, txt='Grupo: 4CM13')

    pdf.set_text_color(0, 0, 0)
    pdf.text(x=20, y=60, txt= 'Informaciòn del Inventario')
    pdf.set_font('Arial', '', 16)
    pdf.text(x=20, y=70, txt='ID del dispositivo: '+str(ide))
    cur.execute("select host From Dispositivos where IDispo = '{0}'".format(ide))
    host = cur.fetchone()
    pdf.text(x=20, y=80, txt='Host/IP: '+str(host[0]))
    cur.execute("select comunidad From Dispositivos where IDispo = '{0}'".format(ide))
    comunidad = cur.fetchone()
    pdf.text(x=20, y=90, txt='Comunidad: '+str(comunidad[0]))
    cur.execute("select puerto From Dispositivos where IDispo = '{0}'".format(ide))
    puerto = cur.fetchone()
    pdf.text(x=20, y=100, txt='Puerto: '+str(puerto[0]))
    cur.execute("select nombre From Dispositivos where IDispo = '{0}'".format(ide))
    nombre = cur.fetchone()
    pdf.text(x=20, y=110, txt='Nombre: '+str(nombre[0]))
    cur.execute("select contacto From Dispositivos where IDispo = '{0}'".format(ide))
    contacto = cur.fetchone()
    pdf.text(x=20, y=120, txt='Contacto: '+str(contacto[0]))
    cur.execute("select ubicacion From Dispositivos where IDispo = '{0}'".format(ide))
    ubi = cur.fetchone()
    pdf.text(x=20, y=130, txt='Ubicaciòn: '+str(ubi[0]))
    cur.execute("select ninter From Dispositivos where IDispo = '{0}'".format(ide))
    ni = cur.fetchone()
    pdf.text(x=20, y=140, txt='Nùmero de interfaces: '+str(ni[0]))
    cur.execute("select so From Dispositivos where IDispo = '{0}'".format(ide))
    so = cur.fetchone()
    cur.execute("select version From Dispositivos where IDispo = '{0}'".format(ide))
    version = cur.fetchone()
    if str(so) == "('Linux',)":
        pdf.text(x=20, y=150, txt='Sistema operativo: '+str(so[0]))
        pdf.text(x=20, y=160, txt='Version: '+str(version[0]))
        pdf.image('Linux_logo.jpg', x = 120, y = 180, w= 70, h = 70)
    else:
        pdf.text(x=20, y=150, txt='Sistema operativo: ' + str(so[0]))
        pdf.text(x=20, y=160, txt='Version: ' + str(version[0]))
        pdf.image('wind.png', x=120, y=180, w=70, h=70)

    pdf.add_page()
    #titulo
    pdf.cell(w=0, h=15, txt= 'Reporte informaciòn de interfaz', border= 1, ln=1, align='C', fill = 0)

    pdf.set_font('Arial', '', 10)
    #columnas
    pdf.cell(w=10, h=15, txt='ID', border=1, align='C', fill=0)
    pdf.cell(w=150, h=15, txt='Descripciòn', border=1, align='C', fill=0)
    pdf.multi_cell(w=0, h=15, txt='Estado', border=1, align='C', fill=0)

    #filas
    for valor in si:
        pdf.cell(w=10, h=15, txt=str(valor[1]), border=1, align='C', fill=0)
        pdf.cell(w=150, h=15, txt=valor[2], border=1, align='C', fill=0)
        pdf.multi_cell(w=0, h=15, txt=valor[3], border=1, align='C', fill=0)

    pdf.output('Reporte_Dispositivo_'+str(nombre[0])+str(so[0])+'.pdf')
