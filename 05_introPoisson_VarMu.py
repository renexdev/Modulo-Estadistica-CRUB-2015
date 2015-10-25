#!/usr/bin/env python

##########################################################################################################
# Modulo Bioestadistica - 2015 de la Universidad del Comahue. Centro Regional Bariloche
#http://crubweb.uncoma.edu.ar/
# Dr. Rene Cejas Bolecek
# email: reneczechdev@gmail.com
# licence: MIT. http://opensource.org/licenses/MIT 

#Ejemplo del libro Sokal, Introduccion a la bioestadistica, Reverte, 2002. version en ingles  p.67
#Ejecutar:
#python 05_introPoisson_VarMu.py
##########################################################################################################

# Importo librerias
import numpy as np
import pylab as P
import matplotlib.pyplot as plt
import math

def factorial(n):return reduce(lambda x,y:x*y,[1]+range(1,n+1))

def poissonGen(mu1,maxNumEv1):
	terminoComun = 1/math.exp(mu1)
	a = np.array([(mu1**x)/factorial(x)*terminoComun for x in range(0, maxNumEv1)])
	print factorial(5)
	print a
	return a

mu = [0.1,1.0,2.0,5.0,10.0]


maxNumEv = 20
rareEvi = np.array([x for x in range(0, maxNumEv)])
rareEventsPerSample = []
for i in range(0, len(mu)):
	rareEventsPerSample.append(rareEvi)

RelFrecPoisson = []
for i in range(0, len(mu)):
	RelFrecPoisson.append( poissonGen(mu[i],maxNumEv))

#Defino titulos
plt.xlim(0,20)
plt.ylabel("Relative expected Frec.")
plt.xlabel("Rare events per sample")
plt.title("Poisson Distribucion")

#Defino ancho de barra
width = 1.0
#Defino 2 graficas de barras

colors = np.array(['b','g','r','c','m','y','l','w'])

#http://matplotlib.org/api/colors_api.html
#b: blue
#g: green
#r: red
#c: cyan
#m: magenta
#y: yellow
#k: black
#w: white


for i in range(0, len(mu)):
	plt.bar(np.array(rareEventsPerSample[:][i])+i/(len(mu)*1.), np.array(RelFrecPoisson[:][i]), align='center', width=width/(len(mu)*1.),color = colors[i],label='mu = %.1f'%(mu[i]))


#Ubico leyenda
plt.legend( loc='upper left', numpoints = 1 )

#Dibujo
plt.show()
