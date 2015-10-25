#!/usr/bin/env python

##########################################################################################################
# Modulo Bioestadistica - 2015 de la Universidad del Comahue. Centro Regional Bariloche
#http://crubweb.uncoma.edu.ar/
# Dr. Rene Cejas Bolecek
# email: reneczechdev@gmail.com
# licence: MIT. http://opensource.org/licenses/MIT 

#Ejemplo del libro Sokal, Introduccion a la bioestadistica, Reverte, 2002. version en ingles  p.42
#Ejecutar:
#python 03_introBinomial.py
##########################################################################################################

# Importo librerias
import numpy as np
import pylab as P
import matplotlib.pyplot as plt

#Defino bin
bins = np.array([x for x in range(0, 6)])


#Calculos previos
n =5

p = 0.4
columna2p = np.array([p**(n-x) for x in range(0, 6)])
print columna2p

q = 1-p
columna3q = np.array([q**x for x in range(0, 6)])
print columna3q

bincoef = np.array([1,5,10,10,5,1])

columna4relfrec = np.array([columna2p[x]*columna3q[x]*bincoef[x] for x in range(0, 6)])
print columna4relfrec

totalMuestras = 2423
frecAbsTeor = np.array([columna4relfrec[x]*totalMuestras for x in range(0, 6)])
print frecAbsTeor

#Defino frecuencias
frecClumped = np.array([47,227,558,663,703,225])
frecRepulsed = np.array([14,157,548,943,618,143])
#Defino titulos
plt.ylabel("Frec. Abs.")
plt.xlabel("Numero insectos infectados por muestra")
plt.title("Comparacion distribucion Binomial con Aglutinada-Repulsiva")

#Defino ancho de barra
width = 1.0
#Defino 2 graficas de barras
plt.bar(bins, frecAbsTeor, align='center', width=width*0.3,color = 'b', label='Teorico')
plt.bar(bins+0.3, frecClumped, align='center', width=width*0.3,color = 'r', label='Clumped')
plt.bar(bins+0.6, frecRepulsed, align='center', width=width*0.3,color = 'g', label='Repulsed')
#Ubico leyenda
plt.legend( loc='upper left', numpoints = 1 )

#Dibujo
plt.show()

#Calculo diferencia entre teoria y experimento
diff1 = frecAbsTeor - frecClumped
diff2 = frecAbsTeor - frecRepulsed
#Defino titulos
plt.ylabel("Diferencia porcentual")
plt.xlabel("Numero insectos infectados por muestra")
plt.title("Comparacion distribucion Binomial con Aglutinada-Repulsiva")

#Defino grafica
plt.plot(bins,diff1/totalMuestras*100,label='Clumped')
plt.plot(bins,diff2/totalMuestras*100,label='Repulsed')
plt.legend( loc='upper left', numpoints = 1 )
#Dibujo
plt.show()
