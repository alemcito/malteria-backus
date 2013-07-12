# -*- coding: utf-8 -*-
import reportlab.pdfgen.canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
import os
import sqlite3

conn = sqlite3.connect('db/db.sqlite')
b = conn.cursor()


def principal(lista5, lote):
    query("select EnlacePdf, EnlaceArchivos from ConfiguracionGlobal limit 1")
    elpdf = ""
    for pdf in b:
        elpdf = pdf[0]
    try:
        fichero = open("%s/%s.pdf" % (str(elpdf), str(lote)))
        fichero.close()
        abrirpdf(self, lote)
    except:
        # crear lienzo pdf
        c = reportlab.pdfgen.canvas.Canvas('%s/%s.pdf' % (str(elpdf), lote))
        listnombres = []
        lista5 = dict(lista5)
        for key, values in lista5.iteritems():
            listnombres.append(key)
        framePage(c, "NÚMERO DE LOTE: %s" % lote, 11.0)
        grafica3(listnombres, c)
        grafica4(listnombres, c)
        c.showPage()
        if len(listnombres) == 5:
            grafica5(listnombres, c)
            grafica2(listnombres, c, "0")
            c.showPage()
            grafica1(listnombres, c, "1")
        else:
            grafica2(listnombres, c, "1")
            grafica1(listnombres, c, "0")
        c.save()


def grafica1(listnombres, c, pos):
    #GRAFICA 1 ----------------------------------------------------------------

    q = "select * from temporales where id='1'"
    query(q)
    if pos == "1":
        espacios = [11.0, 580, 790, 560, 540, 520, 500]
    else:
        espacios = [6.7, 260, 480, 240, 220, 200, 180]
    for a in b:
        a = a
    posi = 0
    framePage(c, listnombres[0], espacios[posi])
    posi += 1
    fichero_imagen = "%s.png" % listnombres[0]
    c.drawImage(fichero_imagen, -20, espacios[posi], 619, 200)
    posi += 1
    c.setFillColorRGB(0, 0, 0)
    c.drawString(220, espacios[posi], a[0])
    posi += 1
    if a[2].strip() != "":
        c.drawString(75, espacios[posi], "Tiempo Total de Remojo: %s" % a[2])
        posi += 1
    if a[3].strip() != "":
        c.drawString(75, espacios[posi], "Última Temperatura de CO2 en\
 Remojo Seco: %s" % a[3])
        posi += 1
    if a[4].strip() != "":
        c.drawString(75, espacios[posi], "Diferencia Máxima de Temperatura\
 entre parte superior e inferior: %s" % a[4])
        posi += 1
    if a[5].strip() != "":
        c.drawString(75, espacios[posi], "Delta de Temperatura: %s" % a[5])
        posi += 1
    #FIN GRAFICA 1 ------------------------------------------------------------


def grafica2(listnombres, c, pos):
    #GRAFICA 2 ----------------------------------------------------------------
    q = "select * from temporales where id='2'"
    query(q)
    if pos == "1":
        espacios = [10.8, 560, 777, 550, 530, 510, 490]
    else:
        espacios = [7.1, 300, 510, 280, 260, 240, 220]
    for a in b:
        a = a
    posi = 0
    framePage(c, listnombres[1], espacios[posi])
    posi += 1
    fichero_imagen = "%s.png" % listnombres[1]
    c.drawImage(fichero_imagen, -20, espacios[posi], 619, 200)
    posi += 1
    c.setFillColorRGB(0, 0, 0)
    c.drawString(220, espacios[posi], a[0])
    posi += 1
    if a[2].strip() != "":
        c.drawString(75, espacios[posi], "Tiempo Total de Remojo: %s" % a[2])
        posi += 1
    if a[3].strip() != "":
        c.drawString(75, espacios[posi], "Última Temperatura de CO2 en\
 Remojo Seco: %s" % a[3])
        posi += 1
    if a[4].strip() != "":
        c.drawString(75, espacios[posi], "Diferencia Máxima de Temperatura\
 entre parte superior e inferior: %s" % a[4])
        posi += 1
    if a[5].strip() != "":
        c.drawString(75, espacios[posi], "Delta de Temperatura: %s" % a[5])
        posi += 1
    #FIN GRAFICA 2 ------------------------------------------------------------


def grafica3(listnombres, c):
    #GRAFICA 3 ----------------------------------------------------------------
    q = "select * from temporales where id='3'"
    query(q)
    espacios = [10.7, 770, 550, 530, 510, 490, 470]
    posi = 0
    for a in b:
        a = a
    fichero_imagen = "%s.png" % listnombres[2]
    c.drawImage(fichero_imagen, -20, 560, 619, 200)
    framePage(c, listnombres[2], espacios[posi])
    posi += 1
    c.drawString(220, espacios[posi], a[0])
    posi += 1
    if a[2].strip() != "":
        c.drawString(75, espacios[posi], "Tiempo Total de Remojo: %s" % a[2])
        posi += 1
    if a[3].strip() != "":
        c.drawString(75, espacios[posi], "Última Temperatura de CO2 en\
 Remojo Seco: %s" % a[3])
        posi += 1
    if a[4].strip() != "":
        c.drawString(75, espacios[posi], "Diferencia Máxima de Temperatura\
 entre parte superior e inferior: %s" % a[4])
        posi += 1
    if a[5].strip() != "":
        c.drawString(75, espacios[posi], "Delta de Temperatura: %s" % a[5])
        posi += 1
    #FIN GRAFICA 3 ------------------------------------------------------------


def grafica4(listnombres, c):
    #GRAFICA 4 ----------------------------------------------------------------
    q = "select * from temporales where id='4'"
    query(q)
    espacios = [6.5, 465, 250, 230, 210, 190, 170]
    posi = 0
    for a in b:
        a = a
    fichero_imagen = "%s.png" % listnombres[3]
    c.drawImage(fichero_imagen, -20, 260, 619, 200)
    framePage(c, listnombres[3], espacios[posi])
    posi += 1
    c.drawString(220, espacios[posi], a[0])
    posi += 1
    if a[2].strip() != "":
        c.drawString(75, espacios[posi], "Tiempo Total de Remojo: %s" % a[2])
        posi += 1
    if a[3].strip() != "":
        c.drawString(75, espacios[posi], "Última Temperatura de CO2 en\
 Remojo Seco: %s" % a[3])
        posi += 1
    if a[4].strip() != "":
        c.drawString(75, espacios[posi], "Diferencia Máxima de Temperatura\
 entre parte superior e inferior: %s" % a[4])
        posi += 1
    if a[5].strip() != "":
        c.drawString(75, espacios[posi], "Delta de Temperatura: %s" % a[5])
        posi += 1
    c.drawString(75, 280, " ")
    # FIN GRAFICA 4 -----------------------------------------------------------


def grafica5(listnombres, c):
    #GRAFICA 5 ----------------------------------------------------------------
    q = "select * from temporales where id='5'"
    query(q)
    espacios = [11.0, 790, 580, 560, 540, 520, 500]
    #titulo, hora,
    posi = 0
    for a in b:
        a = a
    fichero_imagen = "%s.png" % listnombres[4]
    c.drawImage(fichero_imagen, -20, 590, 619, 200)
    framePage(c, listnombres[4], espacios[posi])
    posi += 1
    c.drawString(220, espacios[posi], a[0])
    posi += 1
    if a[2].strip() != "":
        c.drawString(75, espacios[posi], "Tiempo Total de Remojo: %s" % a[2])
        posi += 1
    if a[3].strip() != "":
        c.drawString(75, espacios[posi], "Última Temperatura de CO2 en Remojo\
 Seco: %s"
 % a[3])
        posi += 1
    if a[4].strip() != "":
        c.drawString(75, espacios[posi], "Diferencia Máxima de Temperatura\
 entre parte superior e inferior: %s" % a[4])
        posi += 1
    if a[5].strip() != "":
        c.drawString(75, espacios[posi], "Delta de Temperatura: %s" % a[5])
        posi += 1
    # FIN GRAFICA 5 -----------------------------------------------------------


def framePage(canvas, title, pos):
    canvas.setFont('Times-Roman', 15)
    canvas.drawString(inch, pos * inch, title)
    canvas.setFont('Times-Roman', 10)
    canvas.drawCentredString(4.135 * inch, 0.75 * inch,
                            'Página %d' % canvas.getPageNumber())
    #reset carefully afterwards
    canvas.setLineWidth(1)
    canvas.setStrokeColorRGB(0, 0, 0)


def query(query):
    b.execute(query)
    conn.commit()


def abrirpdf(self, lote):
    query("select EnlacePdf, EnlaceArchivos from ConfiguracionGlobal limit 1",
         self)
    elpdf = ""
    for pdf in c:
        elpdf = pdf[0]
    os.system('/usr/bin/gnome-open %s/%s.pdf' % (str(elpdf), str(lote)))
    os.system("Adobe\Reader9.0\Reader\AcroRd32.exe %s/%s.pdf" % (str(elpdf),
             str(lote)))


if __name__ == '__main__':
    principal(lista5, lote)
