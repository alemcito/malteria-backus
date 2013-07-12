# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import sqlite3
import matplotlib.dates as mdates
import time
import datetime
from dateutil.parser import parse as dateparse
import datetime as dt  # Importamos el módulo datetime
import matplotlib.ticker as ticker

conn = sqlite3.connect('db/db.sqlite')
c = conn.cursor()


def spines_par(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.itervalues():
        sp.set_visible(False)


def make_spine_invisible(ax, direction):
    if direction in ["right", "left"]:
        ax.yaxis.set_ticks_position(direction)
        ax.yaxis.set_label_position(direction)
    elif direction in ["top", "bottom"]:
        ax.xaxis.set_ticks_position(direction)
        ax.xaxis.set_label_position(direction)
    else:
        raise ValueError("Dirección Desconocida : %s" % (direction,))
    ax.spines[direction].set_visible(True)


def principal(datoinicio, datofin, datdic):

    if True:
        esdelta = False
        curvas = []
        datoscurva = []
        for a in range(1, 13):
            q1 = "select Curva%s from Configuracion where NombreGrafico='%s' \
                and Curva%s!='None' and Curva%s!=''" % (str(a), datdic,
                str(a), str(a))
            query(q1)
            for dato in c:
                curvas.append(str(dato[0]))
            q2 = "select NombreCurva%s || ',' || Min%s || ',' || Max%s from \
                Configuracion where NombreGrafico='%s'" % (str(a), str(a),
                str(a), datdic)
            query(q2)

            for dato in c:
                if dato[0]:
                    datoscurva.append(str(dato[0]))

        curv2 = []
        if datdic == "Tina 1":
            for pt1 in range(0, 12):
                if pt1 % 2 == 0:
                    curv2.append(curvas[pt1])
            curvas = curv2
        total = len(curvas)
        par = {}
        p = {}
        maxim = 0
        cmaxim = 0
        lmaxim = []
        minim = 0
        men = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        men = datetime.datetime.strptime(men, "%Y-%m-%d %H:%M:%S")
        may = datetime.datetime.strptime("1920-01-01 00:00:00",
                                        "%Y-%m-%d %H:%M:%S")

        pre2 = [0.99, 0.96, 0.87, 0.8, 0.75, 0.71, 0.66, 0.62, 0.57, 0.23,
                0.48, 0.51]

        ultimodato = 0
        tmax = 0
        tmin = 9999999
        tmax = 0
        dinicio = ""
        dfin = ""
        macroy = []
        #CURVA PRINCIPAL

        #resize
        plt.figure(figsize=(20.111, 6.5))
        fig = plt.figure(1)
        par.update({"host": fig.add_subplot(111)})

        for a in range(1, total):
            par.update({"par%s" % (str(a)): par['host'].twinx()})

        plt.subplots_adjust(left=0.07, right=pre2[total - 1],
                            top=0.79, bottom=0.05)

        offset = 1  # espacio entre eje Y

        for a in range(1, total):
            par["par%s" % (str(a))].spines["right"].set_position(("axes",
                offset))
            spines_par(par["par%s" % (str(a))])  # hacer uno por curva
            make_spine_invisible(par["par%s" % (str(a))], "right")
            offset += 0.1
        datocurva = datoscurva[0].split(",")
        par["host"].set_ylim(int(datocurva[1]), int(datocurva[2]))

        # ------ OBTENER MAYOR CANTIDAD DE  PUNTOS
        maximopunto = 0
        for ah in range(0, total):
            busqueda = 0  # 0 dato inicial #1 dato final
            puntosx = []
            contenidoy = []
            #leer los archivos de las curvas y generar lista de puntos
            f = open(curvas[ah])
            i = 0
            for linea in f:
                if linea[0:1] != "N":
                    if busqueda == 0:
                        dat1 = fdat(linea[0:17])
                        dat2 = fdat(datoinicio)
                        dinicio = dat2
                        if dat2 <= dat1:
                            puntosx.append(dat1)
                            # print dat1
                            busqueda = 1
                    elif busqueda == 1:
                        contenidoy.append(float(linea[18:26]))
                        dat1 = fdat(linea[0:17])
                        dat2 = fdat(datofin)
                        dfin = dat2
                        # if linea[0:17] < datofin:

                        if dat2 < dat1:
                            break
                            busqueda = 2
                        else:
                            datx = fdat(linea[0:17])
                            puntosx.append(datx)

                    else:
                        break
            if len(puntosx) > maximopunto:
                maximopunto = len(puntosx)

        # ------- FIN
        for ah in range(0, total):

            busqueda = 0  # 0 dato inicial #1 dato final
            puntosx = []
            contenidoy = []
            #leer los archivos de las curvas y generar lista de puntos
            f = open(curvas[ah])
            i = 0

            for linea in f:
                if linea[0:1] != "N":
                    if busqueda == 0:
                        dat1 = fdat(linea[0:17])
                        dat2 = fdat(datoinicio)
                        dinicio = dat2
                        if dat2 <= dat1:
                            puntosx.append(dat1)
                            # print dat1
                            busqueda = 1
                    elif busqueda == 1:
                        contenidoy.append(float(linea[18:26]))
                        dat1 = fdat(linea[0:17])
                        dat2 = fdat(datofin)
                        dfin = dat2
                        # if linea[0:17] < datofin:

                        if dat2 < dat1:
                            break
                            busqueda = 2
                        else:
                            datx = fdat(linea[0:17])
                            puntosx.append(datx)

                    else:
                        break
            try:
                allenar = maximopunto - len(puntosx)
                ultimoallenarx = puntosx[len(puntosx) - 1]

                ultimoallenary = contenidoy[len(contenidoy) - 1]
                for w in range(0, allenar):
                    puntosx.append(ultimoallenarx)
                    contenidoy.append(ultimoallenary)
            except:
                pass
            macroy.append(contenidoy)
            contenidox = map(lambda s: time.mktime(
                        datetime.datetime.strptime(s,
                        "%Y-%m-%d %H:%M:%S").timetuple()), puntosx)
            # print len(puntosx)
            # print "a"
            # print len(contenidox)
            lmaxim.append(len(contenidox))
            if len(contenidox) > maxim:
                maxim = len(contenidox)
                ultimodato = contenidoy[maxim - 1]
            contx = []
            ax = 0
            for a in contenidox:
                contx.append(int(ax))
                ax += 1

            con = len(contenidox)
            #contenidox = map(datetime.datetime.fromtimestamp, contenidox)
                #dts es elcontenido x
            colores = ["b-", "r-", "g-", "#000000", "#008b8b", "#340B8C",
                         "#ff6136", "#b8860b", "#E4007C", "#FFCC00", "#A62A2A",
                        "#ff7f50"]
            datocurva = datoscurva[ah].split(",")

            xxy = [dt.datetime.strptime(dax, '%Y-%m-%d %H:%M:%S')
                                            for dax in puntosx]
            # if ah == 0:

            p.update({"p%s" % (str(ah + 1)): par['host'].plot(contx,
                    contenidoy, colores[ah], label=datocurva[0])})

            # else:
            #     p.update({"p%s" % (str(ah + 1)): par['par%s' % (str(ah))].
                # plot(contenidox,
            #         contenidoy, colores[ah], label=datocurva[0])})
        #MIN Y MAX DE LAS Y
        # par["host"].xaxis.set_major_formatter(mdates.DateFormatter
            # ('%Y-%m-%d %H:%M:%S'))
        # par["host"].xaxis.set_major_locator(mdates.SecondLocator
            # (interval = 20))
        maximo = 0
        maximo2 = 0
        for a in lmaxim:
            if a > maximo:
                maximo = a
        lmaxim.remove(maximo)
        for a in lmaxim:
            if a > maximo2:
                maximo2 = a
        query("select id from posiciontemporal limit 1")

        for a in c:
            if a[0] == 0:
                par['host'].set_xlim(0, maximo)
            else:
                par['host'].set_xlim(0, maximo2)

        for a in range(1, total):
            part = datoscurva[a - 1].split(",")
            par["par%s" % a].set_ylim(int(part[1]), int(part[2]))
        #COLOR DE LOS Y
        for ac in range(0, total):
            if ac == 0:
                par['host'].yaxis.label.set_color(p["p%s" %
                (str(ac + 1))][0].get_color())
            else:
                par["par%s" % (str(ac))].yaxis.label.set_color(p["p%s" %
                 (str(ac + 1))][0].get_color())

    #COLOR DE LOS PUNTOS DEL EJE Y
        tkw = dict(size=4, width=1.5)
        for a in range(0, total):
            if a == 0:
                par['host'].tick_params(axis='y',
                    colors=p["p%s" % (str(a + 1))][0].get_color(), **tkw)
            else:
                par["par%s" % (str(a))].tick_params(axis='y',
                    colors=p["p%s" % (str(a + 1))][0].get_color(), **tkw)
        par["host"].tick_params(axis='x', **tkw)

    #CREANDO LEGEND
        lines = []
        for co in range(1, total + 1):
            lines.append(p["p%s" % (str(co))][0])
        par['host'].legend(lines, [l.get_label() for l in lines])
        par["host"].legend(bbox_to_anchor=(0., 1.1, 1., .102), loc="right",
                                    ncol=2, mode="expand", borderaxespad=0.)

        plt.draw()
        q = "Select MostrarGraficas from ConfiguracionGlobal limit 1"
        query(q)
        fig.autofmt_xdate()
        for rpta in c:
            if rpta[0] == "1":
                plt.show()

        fig.savefig('%s.png' % (datdic))
        plt.close()
        print " "
        print "Gráfico creado --> %s" % datdic
        q = "select id from posiciontemporal limit 1"
        query(q)
        gactual = 0
        for a in c:
            gactual = int(a[0])
            posact = a[0]
        gactual += 1
        q = "update posiciontemporal set id ='%s' where id ='%s'" % (gactual,
             posact)
        query(q)
        lanza = 0
        temp = 0
        contq = 0

        if datdic[0] == "c" or datdic[0] == "C":
            for a in datoscurva:
                if a[0] == "T" or a[0] == "t":
                    temp = 0.0
                    for a in macroy[contq]:
                        if float(a) > temp:
                            temp = a
                elif a[0] == "L" or a[0] == "l":
                    lanza = 0
                    for a in macroy[contq]:
                        if float(a) > lanza:
                            lanza = a
                contq += 1
            delta = float(lanza) - float(temp)
            print "Delta de Temperatura --> %s" % delta
            q = "update temporales set tiemporemojo='', ultimatemperatura='',\
                diferenciatemperatura='', delta='%8.2f',datoinicial='%s' where\
                 id='%s'" % (float(delta), dinicio, gactual)
            query(q)
        else:
            resta = datetime.datetime.strptime(dfin, "%Y-%m-%d %H:%M:%S")\
            - datetime.datetime.strptime(dinicio, "%Y-%m-%d %H:%M:%S")
            print "Tiempo total de remojo --> %s" % (resta)
            print "Ultima Temperatura de CO2 en remojo seco --> %s" %\
float(ultimodato)
            contq = 0
            if datdic[0] == "h" or datdic[0] == "H":
                for a in datoscurva:
                    a = a.split(",")
                    if a[0].find("bajo") >= 0:
                        temp = 0.0
                        for a in macroy[contq]:
                            if float(a) > temp:
                                temp = a
                    elif a[0].find("sobre") >= 0:
                        lanza = 0
                        for a in macroy[contq]:
                            if float(a) > lanza:
                                lanza = a
                    contq += 1
                delta = float(lanza) - float(temp)
                print "Delta de Temperatura --> %s" % delta
                query(q)
            r = minmax(contenidoy)
            rresta = float(r[1]) - float(r[0])
            print "Diferencia máxima de Temperatura entre parte superior e\
 inferior --> %s" % (rresta)
            if datdic[0] == "h" or datdic[0] == "H":
                q = "update temporales set tiemporemojo='%s',\
                    ultimatemperatura='%8.2f', diferenciatemperatura='%8.2f',\
                    delta='%8.2f',datoinicial='%s' where id='%s'" % (resta,
                    float(ultimodato), float(rresta), float(delta), dinicio,
                    gactual)
            else:
                q = "update temporales set tiemporemojo='%s',\
                    ultimatemperatura='%8.2f', diferenciatemperatura='%8.2f',\
                    delta='',datoinicial='%s' where id='%s'" % (resta,
                    float(ultimodato), float(rresta), dinicio, gactual)
            query(q)


def minmax(l):
    l.sort()
    return l[0], l[-1]


def fdat(vdato):
    vdato = str(vdato)
    dat1 = vdato.replace(".", "-")  # dato buscado
    dat1 = "20%s-%s-%s%s" % (str(dat1[6:8]), str(dat1[3:5]),
                             str(dat1[0:2]), str(dat1[8:17]))

    return dat1


def query(query):
    c.execute(query)
    conn.commit()


if __name__ == '__main__':
    principal(datoinicio, datofin, datdic)
