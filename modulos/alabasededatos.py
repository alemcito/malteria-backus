#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import sqlite3
except Exception, e:
    print "error"


 #leyendo el archivo
def inicio():
    countbody = 0
    f = open("Index File Exp Trd")
    nombvalgrafica = ""
    for linea in f:
        dato = linea
        if dato[0] == "#":
            dato = dato.replace("#", "")
            dato = dato[0: -3]
            nombvalgrafica = dato
            inse(dato)
            countbody = 1
        else:
            planified = dato[6:9]

            rute = dato.split(":Val/")
            rute = rute[0] + ".dat"
            rute = rute.replace(":", "_")
            update = ""
            if planified != "Seq":
                imp = 0
                mini = 0
                maxi = 0
                try:
                    contenido = open(rute)
                    esplit = contenido.readline().split(":Val/x/t\
                        Bezeichnung:	")
                    arccurva = esplit[0].split("Name:	")
                    arccurva = ("%s.dat" % arccurva[1].replace(":", "_")
                                ).replace("Out", "OUT")
                    nomcurva = esplit[1]
                    update = "update Configuracion set Curva%s='%s',\
                            NombreCurva%s='%s',Min%s='0',Max%s='0' where\
                            NombreGrafico='%s'" % (str(countbody), arccurva,
                                                str(countbody),
                                                nomcurva.replace("\r\n", ""),
                                                str(countbody), str(countbody),
                                                nombvalgrafica)
                    upa(update)
                except Exception, e:
                    print rute
                countbody += 1
            else:
                update = "update Configuracion set RutaLote='%s' where\
                        NombreGrafico='%s'" % (rute, nombvalgrafica)
                upa(update)


def upa(valor):
    conn = sqlite3.connect('../db/db.sqlite')
    c = conn.cursor()
    c.execute(valor)
    conn.commit()
    c.close()


def inse(valor):
    conn = sqlite3.connect('../db/db.sqlite')
    c = conn.cursor()
    c.execute("Insert Into Configuracion (NombreGrafico) Values('%s')" % str(valor))
    conn.commit()
    c.close()


if __name__ == '__main__':
    inicio()
