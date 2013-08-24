# -*- coding: utf-8 -*-
try:
    import pygtk
    pygtk.require("2.0")
except Exception, e:
    print e

try:
    import gtk
except Exception, e:
    print "GTK no disponible"
    sys.exit(1)
import sqlite3
import curva
import reportar
import os
import sys
import matplotlib
import reportlab
import platform
import subprocess
import glob
import datetime
conn = sqlite3.connect('db/db.sqlite')
c = conn.cursor()
clic = False
clik = False


class main:
    wTree = gtk.Builder()
    lista = {}

    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("interfaces/main.glade")
        self.window = self.builder.get_object("principal")
        if self.window:
            self.window.connect("destroy", gtk.main_quit)
            self.ttr1 = self.builder.get_object("ttr1")
            self.ttr2 = self.builder.get_object("ttr2")
            self.ttr3 = self.builder.get_object("ttr3")
            self.ttr4 = self.builder.get_object("ttr4")
            self.ttr5 = self.builder.get_object("ttr5")
            self.lbla1 = self.builder.get_object("lbla1")
            self.lblb1 = self.builder.get_object("lblb1")
            self.lblc1 = self.builder.get_object("lblc1")
            self.lbld1 = self.builder.get_object("lbld1")
            self.lbla2 = self.builder.get_object("lbla2")
            self.lblb2 = self.builder.get_object("lblb2")
            self.lblc2 = self.builder.get_object("lblc2")
            self.lbld2 = self.builder.get_object("lbld2")
            self.lbla3 = self.builder.get_object("lbla3")
            self.lblb3 = self.builder.get_object("lblb3")
            self.lblc3 = self.builder.get_object("lblc3")
            self.lbld3 = self.builder.get_object("lbld3")
            self.lbla4 = self.builder.get_object("lbla4")
            self.lblb4 = self.builder.get_object("lblb4")
            self.lblc4 = self.builder.get_object("lblc4")
            self.lbld4 = self.builder.get_object("lbld4")
            self.lbla5 = self.builder.get_object("lbla5")
            self.lblb5 = self.builder.get_object("lblb5")
            self.lblc5 = self.builder.get_object("lblc5")
            self.lbld5 = self.builder.get_object("lbld5")
            self.hora1 = self.builder.get_object("hora1")
            self.hora2 = self.builder.get_object("hora2")
            self.hora3 = self.builder.get_object("hora3")
            self.hora4 = self.builder.get_object("hora4")
            self.hora5 = self.builder.get_object("hora5")
            self.dmax1 = self.builder.get_object("dmax1")
            self.dmax2 = self.builder.get_object("dmax2")
            self.dmax3 = self.builder.get_object("dmax3")
            self.dmax4 = self.builder.get_object("dmax4")
            self.dmax5 = self.builder.get_object("dmax5")
            self.utcrs1 = self.builder.get_object("utcrs1")
            self.utcrs2 = self.builder.get_object("utcrs2")
            self.utcrs3 = self.builder.get_object("utcrs3")
            self.utcrs4 = self.builder.get_object("utcrs4")
            self.utcrs5 = self.builder.get_object("utcrs5")
            self.image1 = self.builder.get_object('image1')
            self.image2 = self.builder.get_object('image2')
            self.image3 = self.builder.get_object('image3')
            self.image4 = self.builder.get_object('image4')
            self.image5 = self.builder.get_object('image5')
            self.lblmsg = self.builder.get_object("lblmsg")
            self.delta1 = self.builder.get_object("delta1")
            self.delta2 = self.builder.get_object("delta2")
            self.delta3 = self.builder.get_object("delta3")
            self.delta4 = self.builder.get_object("delta4")
            self.delta5 = self.builder.get_object("delta5")
            self.cbxdia = self.builder.get_object("cbxdia")
            self.cbxmes = self.builder.get_object("cbxmes")
            self.cbxano = self.builder.get_object("cbxano")
            self.cbxdia1 = self.builder.get_object("cbxdia1")
            self.cbxmes1 = self.builder.get_object("cbxmes1")
            self.cbxano1 = self.builder.get_object("cbxano1")
            self.filepdf = self.builder.get_object("filepdf")
            self.txtlote = self.builder.get_object("txtlote")
            self.mensaje = self.builder.get_object("mensaje")
            self.btnsave = self.builder.get_object("btnsave")
            self.cbxsino = self.builder.get_object("cbxsino")
            self.twminimo = self.builder.get_object("twminimo")
            self.twmaximo = self.builder.get_object("twmaximo")
            self.llbletq1 = self.builder.get_object("llbletq1")
            self.llbletq2 = self.builder.get_object("llbletq2")
            self.llbletq3 = self.builder.get_object("llbletq3")
            self.llbletq4 = self.builder.get_object("llbletq4")
            self.llbletq5 = self.builder.get_object("llbletq5")
            self.cbxgrafica = self.builder.get_object("cbxgrafica")
            self.lblrutapdf = self.builder.get_object("lblrutapdf")
            self.filearchivo = self.builder.get_object("filearchivo")
            self.btnarchivos = self.builder.get_object("btnarchivos")
            self.indiceoculto = self.builder.get_object("indiceoculto")
            self.configuracion = self.builder.get_object("configuracion")
            self.lblarchivolote = self.builder.get_object("lblarchivolote")
            self.twnombrecurvas = self.builder.get_object("twnombrecurvas")
            self.twarchivocurva = self.builder.get_object("twarchivocurva")
            self.lblrutaarchivos = self.builder.get_object("lblrutaarchivos")
            self.txtnombrearchivo = self.builder.get_object("txtnombrearchivo")
            self.filesarchivolote = self.builder.get_object("filesarchivolote")
            self.txtnombrearchivo = self.builder.get_object("txtnombrearchivo")

        #diccionario de eventos
        dic = {
            "on_btnpdf_clicked": self.on_btnpdf_clicked,
            "on_btnsave_clicked": self.on_btnsave_clicked,
            "on_cbxsino_changed": self.on_cbxsino_changed,
            "on_button1_clicked": self.on_button1_clicked,
            "on_button2_clicked": self.on_button2_clicked,
            "on_exportar_clicked": self.on_exportar_clicked,
            "on_btngrafica_clicked": self.on_btngrafica_clicked,
            "on_cbxgrafica_changed": self.on_cbxgrafica_changed,
            "on_linkbutton1_clicked": self.on_linkbutton1_clicked,
            "on_btnarchivos_clicked": self.on_btnarchivos_clicked
        }
        self.builder.connect_signals(dic)
        print "INICIANDO SISTEMA DE INFORMES MALTERIA LIMA"
        inicio = datetime.date.today().strftime("%d.%m.%Y")
        fin = (datetime.date.today() -
                datetime.timedelta(days=7)).strftime("%d.%m.%Y")

        print " "
        print "********** REPORTE BOTEC v1.0 **********"
        print "* Versión de MatPlotLib -> %s       *" % matplotlib.__version__
        print "* Versión de ReportLab -> %s          *" % reportlab.Version
        print "* Versión de Python -> %s           *" %\
            platform.python_version()
        vpygtk = gtk.pygtk_version
        print "* Versión de PyGTK -> %s.%s.%s           *" % (vpygtk[0],
                                                            vpygtk[1],
                                                            vpygtk[2])
        print "* Versión de SQLITE -> %s           *" % sqlite3.version
        print "****************************************"
        # print "Versión de Python -> %s" % python.__version__

        listaelementos = gtk.ListStore(str)
        for a in range(1, 32):
            listaelementos.append([a])
        self.cbxdia.set_model(listaelementos)
        self.cbxdia1.set_model(listaelementos)
        render = gtk.CellRendererText()
        self.cbxdia.pack_start(render, True)
        self.cbxdia.add_attribute(render, 'text', 0)
        self.cbxdia1.pack_start(render, True)
        self.cbxdia1.add_attribute(render, 'text', 0)
        self.cbxdia.set_active(0)
        self.cbxdia1.set_active(0)

        listaelementos2 = gtk.ListStore(str)

        for a in range(1, 13):
            listaelementos2.append([a])
        self.cbxmes.set_model(listaelementos2)
        self.cbxmes1.set_model(listaelementos2)
        self.cbxmes.pack_start(render, True)
        self.cbxmes.add_attribute(render, 'text', 0)
        self.cbxmes1.pack_start(render, True)
        self.cbxmes1.add_attribute(render, 'text', 0)
        self.cbxmes.set_active(0)
        self.cbxmes1.set_active(0)

        listaelementos3 = gtk.ListStore(str)

        for a in range(2013, 2015):
            listaelementos3.append([a])
        self.cbxano.set_model(listaelementos3)
        self.cbxano1.set_model(listaelementos3)
        self.cbxano1.pack_start(render, True)
        self.cbxano1.add_attribute(render, 'text', 0)
        self.cbxano.pack_start(render, True)
        self.cbxano.add_attribute(render, 'text', 0)
        self.cbxano.set_active(0)
        self.cbxano1.set_active(0)

    def on_button2_clicked(self, widget):
        self.configuracion.hide()

    def on_button1_clicked(self, widget):
        inicio = "%s.%s.%s" % (self.cbxdia.get_active_text(),
                                self.cbxmes.get_active_text(),
                                self.cbxano.get_active_text())
        fin = "%s.%s.%s" % (self.cbxdia1.get_active_text(),
                            self.cbxmes1.get_active_text(),
                            self.cbxano1.get_active_text())

        actualizar_datos_botec(inicio, fin, self)

    def on_cbxsino_changed(self, widget):
        quer = "update ConfiguracionGlobal set MostrarGraficas = '%s' where Id\
 = '1'" % self.cbxsino.get_active()
        query(quer, self)

    def on_btnsave_clicked(self, widget):
        #obtener variables
        archivo = self.filesarchivolote.get_filename()
        nombre = self.txtnombrearchivo.get_text()
        query2 = "update Configuracion set "
        if archivo:
            query2 = "%sRutaLote = '%s', " % (query2, archivo)

        query2 = extraer_texto(self.twarchivocurva.get_buffer(), query2,
                                "Curva")
        query2 = extraer_texto(self.twnombrecurvas.get_buffer(), query2,
                                "NombreCurva")
        query2 = extraer_texto(self.twminimo.get_buffer(), query2, "Min")
        query2 = extraer_texto(self.twmaximo.get_buffer(), query2, "Max")
        if nombre:
            query2 = "%sNombreGrafico = '%s', " % (query2, nombre)
        query2 = query2[0:len(query2) - 2]
        query2 = "%s where NombreGrafico = '%s'" % (query2,
                                                self.indiceoculto.get_text())
        query(query2, self)
        self.indiceoculto.set_text(nombre)

    def on_btnarchivos_clicked(self, widget):
        act(self.filearchivo.get_filename(), "EnlaceArchivos",
            self.lblrutaarchivos, self)

    def on_btnpdf_clicked(self, widget):
        act(self.filepdf.get_filename(), "EnlacePdf", self.lblrutapdf, self)

    def on_linkbutton1_clicked(self, widget):
        self.configuracion.show()
        query("Select NombreGrafico from Configuracion", self)
        pos = 0
        ls = gtk.ListStore(str)
        ls2 = gtk.ListStore(str)
        for rpta in c:
            repta = list(rpta)
            ls.append([repta[0]])
        ls2.append(['NO'])
        ls2.append(['SI'])
        self.cbxgrafica.set_model(ls)
        cellr = gtk.CellRendererText()
        self.cbxgrafica.pack_start(cellr, True)
        self.cbxgrafica.add_attribute(cellr, 'text', 0)
        self.cbxgrafica.set_active(0)
        self.cbxsino.set_model(ls2)
        cellr2 = gtk.CellRendererText()
        self.cbxsino.pack_start(cellr2, True)
        self.cbxsino.add_attribute(cellr2, 'text', 0)
        self.cbxsino.set_active(0)
        query("select EnlaceArchivos,EnlacePdf,MostrarGraficas from\
 ConfiguracionGlobal", self)
        for rpta in c:
            self.lblrutapdf.set_text(str(rpta[1]))
            self.lblrutaarchivos.set_text(str(rpta[0]))
            self.cbxsino.set_active(int(rpta[2]))
            self.lblmsg.set_text("")
        # quer = "select MostrarGraficas from ConfiguracionGlobal"
        # query(quer, self)
        # for rpta in c:
           # self.cbxsino.set_active(1)

    def on_exportar_clicked(self, widget):
        # reportar.principal(lista)
        global clic
        global clik
        if clic:
            clic = False
            clik = True
            lote = self.txtlote.get_text()
            if len(lote) > 0:
                if self.hora1.get_text() == "":
                    self.mensaje.set_markup("<span color='red'>Primero debe de\
 Graficar, por favor de clic en 'Mostrar Gráficas'</span>")
                else:
                    lista5 = {}
                    query("select NombreGrafico, RutaLote from Configuracion",
                        self)
                    datoinicio = 0
                    datofin = 0
                    for valquer in c:
                        f = open(valquer[1])
                        for linea in f:
                            if linea[0] != "N":
                                dat = linea[18:22]
                                try:
                                    datoa = int(dat)
                                except Exception, e:
                                    datoa = dat[0:3]
                                datoa = str(datoa)

                                if datoa == lote:
                                    lista5.update({valquer[0]: valquer[1]})
                                    break

                    reportar.principal(lista5, lote)
                    query("update temporales set tiemporemojo = '',\
    ultimatemperatura= '', diferenciatemperatura = '', delta = '', \
    datoinicial = '' ", self)
                    abrirpdf(self, lote)
            else:
                self.mensaje.set_markup("<span color='red'>Ingrese Nro de\
 Lote.</span>")
        else:
            self.mensaje.set_markup("<span color='red'>Ya realizó\
 la exportación del lote.</span>")

    def on_cbxgrafica_changed(self, widget):
        sel = self.cbxgrafica.get_active_text()
        query("Select * from Configuracion where NombreGrafico='%s'" % sel,
                                                                    self)
        for valor in c:
            self.lblarchivolote.set_text(str(valor[1]))
            self.txtnombrearchivo.set_text(str(valor[0]))
            self.indiceoculto.set_text(str(valor[0]))
            llena_text_view(2, self.twarchivocurva, valor)
            llena_text_view(14, self.twnombrecurvas, valor)
            llena_text_view(26, self.twminimo, valor)
            llena_text_view(38, self.twmaximo, valor)
        self.lblmsg.set_text("")

    def on_btngrafica_clicked(self, widget):
        global clic
        global clik
        if not clik:
            clic = True
            clik = False
        eliminar_imagenes(self)
        lote = self.txtlote.get_text()
        lista5 = {}
        query("select EnlacePdf, EnlaceArchivos from ConfiguracionGlobal\
 limit 1", self)
        elpdf = ""
        for pdf in c:
            elpdf = pdf[0]
        if lote.strip() == "":
            self.mensaje.set_markup("<span color='red'>Ingrese Valor de\
 Lote.</span>")
        elif not lote.isdigit():
            self.mensaje.set_markup("<span color='red'>Sólo Números en el\
 Lote.</span>")
        else:
            self.mensaje.set_markup("<span color='red'></span>")
            #verificar si existe el archivo pdf ya creado
            existencia = False
            try:
                fichero = open("%s/%s.pdf" % (str(elpdf), str(lote)))

                fichero.close()
                existencia = True
            except:
                existencia = False

            if existencia:  # si existe el archivo
                abrirpdf(self, lote)
            else:  # si no existe se crear las gráficas y se muestra
                query("select NombreGrafico, RutaLote from Configuracion",
                                                                    self)
                datoinicio = ""
                datofin = ""
                for valquer in c:
                    f = open(valquer[1])
                    for linea in f:
                        if linea[0] != "N":

                            dat = linea[18:22]
                            try:
                                dato1 = int(dat)
                            except Exception, e:
                                dato1 = dat[0:3]

                            dato = str(dato1)

                            if dato == lote:
                                lista5.update({valquer[0]: valquer[1]})
                                break
                lista = lista5
                lenlista5 = len(lista5)
                dibuja = 1
                if lenlista5 == 0:
                    self.mensaje.set_markup("<span color='red'>NO SE ENCONTRÓ\
 EL LOTE BUSCADO</span>")
                    dibuja = 0
                elif lenlista5 < 4:
                    self.mensaje.set_markup("<span color='red'>SE ENCONTRARON\
 MENOS DE 4 GRAFICAS</span>")
                    dibuja = 0
                else:
                    self.mensaje.set_markup("<span color='red'>SE ENCONTRARON\
 %s GRAFICAS</span>" % (str(lenlista5)))
                q = "update posiciontemporal set id ='0'"
                query(q, self)
                if dibuja > 0:
                    for key, values in lista5.iteritems():
                        f = open(values)
                        for linea in f:
                            sgt = 0
                            for linea in f:
                                if linea[0] != "N":
                                    dat = linea[18:22]
                                    try:
                                        datoa = int(dat)
                                    except Exception, e:
                                        datoa = dat[0:3]
                                    datoa = str(datoa)
                                    if sgt == 0:
                                        if datoa == lote:
                                            datoinicio = linea
                                            sgt = 1
                                    else:
                                        datofin = linea
                                        break
                        curva.principal(datoinicio, datofin, key)
                cimg = [self.image1, self.image2, self.image3,
                        self.image4, self.image5]
                lbl = [self.llbletq1, self.llbletq2, self.llbletq3,
                        self.llbletq4, self.llbletq5]
                ccont = 0
                for img in lista5:
                    pixbuf = gtk.gdk.pixbuf_new_from_file("%s.png" % img)
                    scaled_buf = pixbuf.scale_simple(999, 333,
                                                    gtk.gdk.INTERP_BILINEAR)
                    cimg[ccont].set_from_pixbuf(scaled_buf)
                    cimg[ccont].show()
                    lbl[ccont].set_text(img)
                    ccont += 1
                q = "select * from temporales"
                query(q, self)
                con = 0
                diccionario_valores = {}
                for a in c:
                    diccionario_valores.update({con: a})
                    con += 1
                    # if con == 1:
                    #     self.hora1.set_text(a[0])
                    #     self.ttr1.set_text(a[2])
                    #     self.utcrs1.set_text(a[3])
                    #     self.dmax1.set_text(a[4])
                    # elif con == 2:
                    #     self.hora2.set_text(a[0])
                    #     self.ttr2.set_text(a[2])
                    #     self.utcrs2.set_text(a[3])
                    #     self.dmax2.set_text(a[4])
                    # elif con == 3:
                    #     self.hora3.set_text(a[0])
                    #     self.ttr3.set_text(a[2])
                    #     self.utcrs3.set_text(a[3])
                    #     self.dmax3.set_text(a[4])
                    # elif con == 4:
                    #     self.hora4.set_text(a[0])
                    # else:
                    #     self.hora5.set_text(a[0])
                con = 0
                for key, values in lista5.iteritems():
                    dicval = diccionario_valores[con]
                    if key[0] == "c" or key[0] == "C":
                        if con == 0:
                            self.hora1.set_text(dicval[0])
                            self.lbla1.set_label("")
                            self.lblb1.set_label("")
                            self.lblc1.set_label("")
                            self.delta1.set_text("%8.2f" % float(dicval[5]))
                        elif con == 1:
                            self.hora2.set_text(dicval[0])
                            self.lbla2.set_label("")
                            self.lblb2.set_label("")
                            self.lblc2.set_label("")
                            self.delta2.set_text("%8.2f" % float(dicval[5]))
                        elif con == 2:
                            self.hora3.set_text(dicval[0])
                            self.lbla3.set_label("")
                            self.lblb3.set_label("")
                            self.lblc3.set_label("")
                            self.delta3.set_text("%8.2f" % float(dicval[5]))
                        elif con == 3:
                            self.hora4.set_text(dicval[0])
                            self.lbla4.set_label("")
                            self.lblb4.set_label("")
                            self.lblc4.set_label("")
                            self.delta4.set_text("%8.2f" % float(dicval[5]))
                        elif con == 4:
                            self.hora5.set_text(dicval[0])
                            self.lbla5.set_label("")
                            self.lblb5.set_label("")
                            self.lblc5.set_label("")
                            self.delta5.set_text("%8.2f" % float(dicval[5]))
                    else:
                        if con == 0:
                            self.hora1.set_text(dicval[0])
                            self.ttr1.set_text(dicval[2])
                            self.utcrs1.set_text("%8.2f" % float(dicval[3]))
                            self.dmax1.set_text("%8.2f" % float(dicval[4]))
                            if key[0] == "H" or key[0] == "h":
                                self.delta1.set_text("%8.2f" %
                                            float(dicval[5]))
                        elif con == 1:
                            self.hora2.set_text(dicval[0])
                            self.ttr2.set_text(dicval[2])
                            self.utcrs2.set_text("%8.2f" % float(dicval[3]))
                            self.dmax2.set_text("%8.2f" % float(dicval[4]))
                            self.lbld2.set_label("")
                        elif con == 2:
                            self.hora3.set_text(dicval[0])
                            self.ttr3.set_text(dicval[2])
                            self.utcrs3.set_text("%8.2f" % float(dicval[3]))
                            self.dmax3.set_text("%8.2f" % float(dicval[4]))
                            self.lbld3.set_label("")
                        elif con == 3:
                            self.hora4.set_text(dicval[0])
                            self.ttr4.set_text(dicval[2])
                            self.utcrs4.set_text("%8.2f" % float(dicval[3]))
                            self.dmax4.set_text("%8.2f" % float(dicval[4]))
                            self.lbld4.set_label("")
                        elif con == 4:
                            self.hora5.set_text(dicval[0])
                            self.ttr5.set_text(dicval[2])
                            self.utcrs5.set_text("%8.2f" % float(dicval[3]))
                            self.dmax5.set_text("%8.2f" % float(dicval[4]))
                            self.lbld5.set_label("")
                    con += 1


def llena_text_view(adicional, wid, datodb):
    buff = wid.get_buffer()
    texto = ""
    for pos in range(0, 12):
        if pos == 11:
            texto = "%s%s" % (texto, str(datodb[pos + adicional]))
        else:
            texto = "%s%s\n" % (texto, str(datodb[pos + adicional]))
    buff.set_text(texto.replace("None", ""))
    wid.set_buffer(buff)


def query(query, self):
    try:
        c.execute(query)
        conn.commit()
        self.lblmsg.set_text("Consulta Realizada Satisfactoriamente.")
    except Exception, e:
        self.lblmsg.set_text(str(e))
        pass


def act(act, quer, lbl, self):
    try:
        query("update ConfiguracionGlobal set %s = '%s'" % (quer, act), self)
        lbl.set_text(act)
        self.lblmsg.set_text("Datos Modificados Satisfactoriamente.")
    except Exception, e:
        self.lblmsg.set_text(str(e))
        pass


def extraer_texto(buff, query2, tipocampo):
    inicio = buff.get_start_iter()
    fin = buff.get_end_iter()
    cont = buff.get_text(inicio, fin)
    cont = cont.split("\n")
    contador = 1
    for val in cont:
        query2 = "%s%s%s = '%s', " % (query2,  tipocampo, str(contador), val)
        contador += 1
    return query2


def abrirpdf(self, lote):
    query("select EnlacePdf, EnlaceArchivos from ConfiguracionGlobal limit 1",
                                                                        self)
    elpdf = ""
    for pdf in c:
        elpdf = pdf[0]
    os.system('/usr/bin/gnome-open %s/%s.pdf' % (str(elpdf), str(lote)))
    os.system("Adobe\Reader9.0\Reader\AcroRd32.exe %s/%s.pdf" % (str(elpdf),
                                                                str(lote)))


def eliminar_imagenes(self):
    lista = glob.glob("*.png")
    if len(lista) > 0:
        for a in lista:
            os.remove(a)


def actualizar_datos_botec(inicio, fin, self):
    print "1"
    os.system('bde_exp_trd.exe -I="Index File Exp Trd" -w -DA=%s -DE=%s' %
        (inicio, fin))
    print "2"


if __name__ == "__main__":
    main()
    gtk.main()
