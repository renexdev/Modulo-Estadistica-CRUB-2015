#!/usr/bin/env python

##########################################################################################################
# Modulo Bioestadistica - 2015 de la Universidad del Comahue. Centro Regional Bariloche
#http://crubweb.uncoma.edu.ar/
# Dr. Rene Cejas Bolecek
# email: reneczechdev@gmail.com
# licence: MIT. http://opensource.org/licenses/MIT 

#Ejemplo del libro Sokal, Introduccion a la bioestadistica, Reverte, 2002. version en ingles  p.67
#Ejecutar:
#python 04_introPoisson_EjLevadura.py
##########################################################################################################

# Importo librerias
import numpy as np
import pylab as P
import matplotlib.pyplot as plt
import math

def factorial(n):return reduce(lambda x,y:x*y,[1]+range(1,n+1))

yeastCellperSquare = np.array([x for x in range(0, 10)])
print "Yeast cells (celulas de levadura)- Y: ",yeastCellperSquare

ObservedFrec = np.array([75,103,121,54,30,13,2,1,0,1])
print "Cuandrados en los que hay Y yeast cells: ",ObservedFrec

totalMuestras = ObservedFrec.sum()
print "total cuadrados relevados: ",totalMuestras
print "mean: Como lo calcularias?"
YMean = np.array([x*ObservedFrec[x]/(totalMuestras*1.0) for x in range(0, 10)]).sum()
print YMean
terminoComun = totalMuestras/math.exp(YMean)
print "Calculo de las expected frec: ", terminoComun

expFrecPoisson = np.array([(YMean**x)/factorial(x)*terminoComun for x in range(0, 10)])
print expFrecPoisson
#print (expFrecPoisson-expFrecPoissonRed)/expFrecPoisson*100
sumExpFrecPoisson = np.array([(YMean**x)/factorial(x)*terminoComun for x in range(0, 10)]).sum()
print "La suma: ",sumExpFrecPoisson
print range(0, 10)
VarObservedFrec = np.array([(x-YMean)**2*ObservedFrec[x]/(totalMuestras*1.0) for x in range(0, 10)]).sum()
print "Desv estandar: ",VarObservedFrec
print "Como la calculo?"
print "Cociente: ", VarObservedFrec/ YMean
print "Que me dice el cociente?"

#frecAbsTeor = np.array([columna4relfrec[x]*totalMuestras for x in range(0, 6)])
#print frecAbsTeor


#Defino titulos
plt.ylabel("Frec. Abs.")
plt.xlabel("Cel. Levadura por cuadrado")
plt.title("Distribucion de celulas de levadura")

#Defino ancho de barra
width = 1.0
#Defino 2 graficas de barras
plt.bar(yeastCellperSquare, ObservedFrec, align='center', width=width*0.5,color = 'b', label='Obs')
plt.bar(yeastCellperSquare+0.5, expFrecPoisson, align='center', width=width*0.5,color = 'r', label='Distrib. Poisson')
#plt.bar(bins+0.6, frecRepulsed, align='center', width=width*0.3,color = 'g', label='Repulsed')
#Ubico leyenda
plt.legend( loc='upper left', numpoints = 1 )

#Dibujo
plt.show()

#Calculo diferencia entre teoria y experimento
diff1 = ObservedFrec - expFrecPoisson
#Defino titulos
plt.ylabel("Diferencia porcentual")
plt.xlabel("Cel. Levadura por cuadrado")
plt.title("Distribucion de celulas de levadura")


#Defino grafica
plt.plot(yeastCellperSquare,diff1/totalMuestras*100,label='Diferencia obs vs teor')
plt.legend( loc='upper left', numpoints = 1 )
#Dibujo
plt.show()
