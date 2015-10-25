#!/usr/bin/env python

##########################################################################################################
# Modulo Bioestadistica - 2015 de la Universidad del Comahue. Centro Regional Bariloche
#http://crubweb.uncoma.edu.ar/
# Dr. Rene Cejas Bolecek
# email: reneczechdev@gmail.com
# licence: MIT. http://opensource.org/licenses/MIT 

#Ejemplo del libro Sokal, Introduccion a la bioestadistica, Reverte, 2002. version en ingles  p.79
#Distribucion normal o gaussiana
#Ejecutar:
#python 09_introNormal.py
##########################################################################################################


# Importo librerias
import numpy as np
import pylab as P
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import math
import scipy.stats as stats

#Generador de coef binomial
def normpdf(x, mean, sd):
    var = float(sd)**2
    pi = 3.1415926
    denom = (2*pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom


#Generador de coef binomial
def binCoefGen(k):
    f = math.factorial
    coef = []
    print k
    for i in range(k+1):
        #print i
        a = f(k)/f(i)/f(k-i)
        print a
        coef.append(a)
    return coef
    
#Defino el k    
print "Efecto del k -> inf. Probar k = 5, 10, 50, 150. criterio pqk > 3"
k = 150

#calculo los bin
bins = np.array([x for x in range(0, k+1)])

#Defino la probabilidad de ocurrencia    
p = 0.5


columna2p = np.array([p**(k-x) for x in range(0, k+1)])
print columna2p

#calculo la probabilidad de no ocurrencia
q = 1-p
columna3q = np.array([q**x for x in range(0, k+1)])
print columna3q
print "approx: ", p*q*k
bincoef = np.array(binCoefGen(k))

columna4relfrec = np.array([columna2p[x]*columna3q[x]*bincoef[x] for x in range(0, k+1)])
print columna4relfrec

totalMuestras = 1
frecAbsTeor = np.array([columna4relfrec[x]*totalMuestras for x in range(0, k+1)])
print frecAbsTeor
mean= k*p
sigma = math.sqrt(k)*p*q
print "mean teorico:", mean
print "sigma teorico:", sigma
#Defino titulos
plt.ylabel("Funcion densidad de probabilidad Normal")
plt.xlabel("Y")
plt.title("Distribuciones normales")

#Defino ancho de barra
width = 1.0


#Defino 2 graficas de barras
normalWLib1stats = stats.norm.pdf(bins,mean,2*sigma) 
normalWLib2mlab = mlab.normpdf(bins,mean,2*sigma)

#Check with other library

means = [4,8,8]
stds = [2,2,1]

normVals = []
normVals.append([])
normVals.append([])
normVals.append([])

for k in range(len(means)):
	for i in range(len(bins)):
		normVals[k].append(normpdf(bins[i],means[k],stds[k]))

colors = ["red","blue","green"]
labels = ["Propongan 1","Propongan 2","Propongan 3"]

#labels = ["Norm mu=%d sigma=%d"%(means[0],stds[0]),"Norm mu=%d sigma=%d"%(means[1],stds[1]),"Norm mu=%d sigma=%d"%(means[2],stds[2])]

for k in range(len(means)):
	plt.plot(bins,normVals[k],lw = 2, color = colors[k], label=labels[k])	
plt.xlim(0,15)

#Ubico leyenda
plt.legend( loc='upper left', numpoints = 1 )

#Dibujo
plt.show()
