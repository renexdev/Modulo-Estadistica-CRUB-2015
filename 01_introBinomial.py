#!/usr/bin/env python

##########################################################################################################
# Modulo Bioestadistica - 2015 de la Universidad del Comahue. Centro Regional Bariloche
#http://crubweb.uncoma.edu.ar/
# Dr. Rene Cejas Bolecek
# email: reneczechdev@gmail.com
# licence: MIT. http://opensource.org/licenses/MIT 

#Ejemplo del libro Sokal, Introduccion a la bioestadistica, Reverte, 2002. version en ingles  p.42
#Ejecutar:
#python 01_introBinomial.py
##########################################################################################################

# Importo librerias
import numpy as np
import pylab as P
import matplotlib.pyplot as plt

#Defino bin
bins = np.array([(59.5 + x*8)*0.0283495 for x in range(0, 15,1)])
#Defino frecuencias
x = np.array([2,6,39,385,888,1729,2240,2007,1233,641,201,74,14,5,1])
print x.sum()
print bins.mean()
#Defino titulos
plt.ylabel("Frec. Abs.")
plt.xlabel("Peso (kg).")
plt.title("Peso de neonatos varones - China. p.42 Biostatistics")

#Defino ancho de barra
width = 8.0
#Defino grafica de barras
plt.bar(bins, x, align='center', width=(width*0.0283495),color = 'r')

#Dibujo
plt.show()
