#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
	import sqlite3
except Exception, e:
	print "error"

	#leyendo el archivo 
def inicio():
	countbody=0
	f = open("Index File Exp Trd")
	nombvalgrafica=""
	for linea in f:
		
		dato=linea
		if dato[0]=="#":
			dato=dato.replace("#", "")
			dato=dato[0:-3]
			nombvalgrafica=dato
			inse(dato)
			countbody = 1
		else:
			planified=dato[6:9]

			rute = dato.split(":Val/")
			rute=rute[0]+".dat"
			rute=rute.replace(":","_")
			update=""
			if planified != "Seq":
				imp=0
				mini=0
				maxi=0
				try:
					contenido=open(rute)
					esplit= contenido.readline().split(":Val/x/t	Bezeichnung:	")
					arccurva=esplit[0].split("Name:	")
					arccurva=(arccurva[1].replace(":","_")+".dat").replace("Out","OUT")
					nomcurva=esplit[1]
					update="update Configuracion set Curva"+str(countbody)+"='"+arccurva+"',NombreCurva"+str(countbody)+"='"+nomcurva.replace("\r\n","")+"',Min"+str(countbody)+"='0',Max"+str(countbody)+"='0' where NombreGrafico='"+nombvalgrafica+"'"
					upa(update)
				except Exception, e:
					print rute
				countbody += 1
			else:
				update="update Configuracion set RutaLote='"+rute+"' where NombreGrafico='"+nombvalgrafica+"'"
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
	c.execute("Insert Into Configuracion (NombreGrafico) Values('"+valor+"')")
	conn.commit()
	c.close()	
	
if __name__ == '__main__':
    inicio()