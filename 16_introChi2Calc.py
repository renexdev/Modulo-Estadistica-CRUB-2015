#!/usr/bin/env python

##########################################################################################################
# Modulo Bioestadistica - 2015 de la Universidad del Comahue. Centro Regional Bariloche
#http://crubweb.uncoma.edu.ar/
# Dr. Rene Cejas Bolecek
# email: reneczechdev@gmail.com
# licence: MIT. http://opensource.org/licenses/MIT 

#Ejemplo del libro Sokal, Introduccion a la bioestadistica, Reverte, 2002. version en ingles  p.112
#Distribucion Chi2
#Ejecutar:
#python 16_introChi2Calc.py
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
from scipy.stats import chi2


width = 1/100.
x = np.linspace(0.5, 15.5, 1./width)
print x

alaMosca = np.array([36,37,38,38,39,39,40,40,40,40,41,41,41,41,41,41,42,42,42,42,42,42,42,43,43,43,43,43,43,43,43,44,44,44,44,44,44,44,44,44,45,45,45,45,45,45,45,45,45,45,46,46,46,46,46,46,46,46,46,46,47,47,47,47,47,47,47,47,47,48,48,48,48,48,48,48,48,49,49,49,49,49,49,49,50,50,50,50,50,50,51,51,51,51,52,52,53,53,54,55])


mean=alaMosca.mean()
std=alaMosca.std()*math.sqrt(len(alaMosca))/math.sqrt(len(alaMosca)-1)

print "HACER UN MUESTREO de m valores:"
print "5 , 50, 100, 500"
times = 1400
print "5,50,500"
tomaMuestreo = 5


muestroChi2 = []

flaDeb= False
if(times<10): flaDeb= True

for i in range(times):
	muestreo1 = []
	tmpy2 = []
	for j in range(tomaMuestreo):
		muestreo1.append(alaMosca[randint(0,99)])
	#tmpy2  = np.array([(muestreo1[j]-mean)**2 for j in range(tomaMuestreo)])
	#tmpy2 = tmpy2.sum()
	tmpy2  = (np.array(muestreo1).std()*math.sqrt(tomaMuestreo)/math.sqrt(tomaMuestreo-1))**2*(tomaMuestreo-1)
	if(flaDeb): print tmpy2
	if(flaDeb): print "tmpSE: ",tmpy2
	muestroChi2.append(tmpy2/(std*1.)**2)



muestreoHist1 = []
muestreobins1 = []
muestreoHist1, muestreobins1 = np.histogram(muestroChi2,  bins=x, density=True)
muestreobins1 = np.array(muestreobins1)
muestreoHist1 = np.array(muestreoHist1)
plt.bar(muestreobins1[0:(len(muestreoHist1)-0)] ,  muestreoHist1, align='center', width = width*2, color = 'red', label='Muestreo de %d'%(tomaMuestreo))
dist = chi2(tomaMuestreo-1, 0)
plt.plot(x, dist.pdf(x), lw=2, c='blue', label="$\chi^2$ df: (%d-1)"%(tomaMuestreo))
print x 
print dist.pdf(x)
plt.legend( loc='upper left', numpoints = 1 )
plt.xlabel("(n-1)s^2/$\sigma$")
plt.ylabel("Probabilidad")
plt.title("Distribuciones de (n-1)s^2/$\sigma$ para muestra de  %d"%(tomaMuestreo))
#plt.ylim(0, 1)
#plt.xlim(0, 15)
plt.show()

