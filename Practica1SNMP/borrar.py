import mysql.connector

def borrar():
    print('¿Què dispositivo desea borrar?')
    miCOnexion = mysql.connector.connect(host='localhost', user='root', passwd='PWD', db='monitoreo')
    cur = miCOnexion.cursor()
    cur.execute("select * From Dispositivos")
    selec = cur.fetchall()
    if selec == []:
        print('No hay ningun registro guardado')
        cur.close()
    else:
        for fila in selec:
            print(fila)
        print('Escriba el id (primer dato) y la ip (segundo dato) del dispositivo que quiere eliminar')
        ide = input('ID: ')
        ide = int(ide)
        host = input('IP/Host: ')
        try:
            cur.execute("delete from Interfaces where IDispo = '{0}'".format(ide))
            miCOnexion.commit()
        except:
            print('ID incorrecta')
            cur.close()
            borrar()
        else:
            try:
                cur.execute("delete from Dispositivos where IDispo = '{0}' and host = '{1}'".format(ide, host))
                miCOnexion.commit()
            except:
                print('ID incorrecto y/o IP incorrecta')
                cur.close()
                borrar()
    cur.close()
