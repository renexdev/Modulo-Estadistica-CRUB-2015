#!/usr/bin/env python

##########################################################################################################
# Modulo Bioestadistica - 2015 de la Universidad del Comahue. Centro Regional Bariloche
#http://crubweb.uncoma.edu.ar/
# Dr. Rene Cejas Bolecek
# email: reneczechdev@gmail.com
# licence: MIT. http://opensource.org/licenses/MIT 

#Ejemplo del libro Sokal, Introduccion a la bioestadistica, Reverte, 2002. version en ingles  p.106
#Distribucion t-Student
#Ejecutar:
#python 14_introTStudentCalc.py
##########################################################################################################

# Importo librerias
import numpy as np
import pylab as P
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import math
import scipy.stats as stats
import scipy as sp
from numpy import zeros, sqrt, where, pi, average, arange, histogram,log,log10 # log is ln
from random import randint
from scipy.stats import t as student_t

width = 1/100.
x = np.linspace(-5, 5, 1./width)

alaMosca = np.array([36,37,38,38,39,39,40,40,40,40,41,41,41,41,41,41,42,42,42,42,42,42,42,43,43,43,43,43,43,43,43,44,44,44,44,44,44,44,44,44,45,45,45,45,45,45,45,45,45,45,46,46,46,46,46,46,46,46,46,46,47,47,47,47,47,47,47,47,47,48,48,48,48,48,48,48,48,49,49,49,49,49,49,49,50,50,50,50,50,50,51,51,51,51,52,52,53,53,54,55])


mean=alaMosca.mean()
std=alaMosca.std()*math.sqrt(len(alaMosca))/math.sqrt(len(alaMosca)-1)

print "HACER UN MUESTREO de m valores:"
print "5 , 50, 100, 500"
times = 1400
print "5,50,500"
tomaMuestreo = 5

muestreo1Av = []
muestreo1SE = []
muestroY = []
flaDeb= False
if(times<10): flaDeb= True

for i in range(times):
	muestreo1 = []
	for j in range(tomaMuestreo):
		muestreo1.append(alaMosca[randint(0,99)])
	tmpSE  = (np.array(muestreo1).std()*math.sqrt(tomaMuestreo)/math.sqrt(tomaMuestreo-1)/math.sqrt(tomaMuestreo))
	if(flaDeb): print "tmpSE: ",tmpSE
	tmpAv = np.array(muestreo1).mean()
	muestreo1SE.append(tmpSE)
	muestreo1Av.append(tmpAv)
	muestroY.append((tmpAv-mean)/tmpSE)
	if(flaDeb): print "muestroY: ", muestroY
	
if(flaDeb): print "mean muestreo: ",muestroY,"std muestreo: ",np.array(muestreo1).std()*math.sqrt(tomaMuestreo)/math.sqrt(tomaMuestreo-1)

muestreoHist1 = []
muestreobins1 = []
muestreoHist1, muestreobins1 = np.histogram(muestroY,  bins=x, density=True)
muestreobins1 = np.array(muestreobins1)
muestreoHist1 = np.array(muestreoHist1)
plt.subplot(2, 1, 1)
plt.bar(muestreobins1[0:(len(muestreoHist1)-0)] ,  muestreoHist1, align='center', width = width*2, color = 'red', label='Muestreo de %d'%(tomaMuestreo))
dist = student_t(tomaMuestreo-1, 0)
plt.plot(x, dist.pdf(x), lw=2, c='blue', label="t-Student df: (%d-1)"%(tomaMuestreo))
normalDistrib = stats.norm.pdf(x, loc=0, scale=1)
plt.plot(x,normalDistrib,color='red',lw=2,label="normal (${\mu=}0,{\sigma=}1$)")
plt.legend( loc='upper left', numpoints = 1 )
plt.xlabel("Desviacion estandarizada ")
plt.ylabel("Probabilidad")
plt.title("Distribuciones de $<Y>$ para muestras de  %d"%(tomaMuestreo))
plt.xlim(-4, 4)

plt.subplot(2, 1, 2)
stats.probplot(muestroY, plot=plt)
plt.show()

