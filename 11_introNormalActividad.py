#!/usr/bin/env python

##########################################################################################################
# Modulo Bioestadistica - 2015 de la Universidad del Comahue. Centro Regional Bariloche
#http://crubweb.uncoma.edu.ar/
# Dr. Rene Cejas Bolecek
# email: reneczechdev@gmail.com
# licence: MIT. http://opensource.org/licenses/MIT 

#Ejemplo del libro Sokal, Introduccion a la bioestadistica, Reverte, 2002. version en ingles  p.80
#Distribucion normal o gaussiana
#Ejecutar:
#python 11_introNormalActividad.py
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

item = np.array([x for x in range(0, 100)])

bins = np.array([x for x in range(30, 60)])

alaMosca = np.array([36,37,38,38,39,39,40,40,40,40,41,41,41,41,41,41,42,42,42,42,42,42,42,43,43,43,43,43,43,43,43,44,44,44,44,44,44,44,44,44,45,45,45,45,45,45,45,45,45,45,46,46,46,46,46,46,46,46,46,46,47,47,47,47,47,47,47,47,47,48,48,48,48,48,48,48,48,49,49,49,49,49,49,49,50,50,50,50,50,50,51,51,51,51,52,52,53,53,54,55])
#mm x 1O- 1
leche = np.array([51,51,51,53,53,53,54,55,55,56,56,56,57,57,57,57,57,57,57,57,58,58,58,58,58,58,58,58,58,58,58,59,59,59,60,60,60,60,60,61,61,61,61,61,61,62,62,62,62,63,63,63,64,65,65,65,65,65,67,67,67,67,68,68,69,69,69,69,69,69,70,72,73,73,74,74,74,74,75,76,76,76,79,80,80,81,82,82,82,82,83,85,87,88,88,89,93,94,96,98])

var = 0
for i in range(100):
	var += (leche[i]-leche.mean())**2
print var/100.
print  math.sqrt(var)/math.sqrt(100)

lecheMean = leche.mean()
lecheStd = leche.std()*math.sqrt(len(leche))/math.sqrt(len(leche)-1)
print "meanleche: ", lecheMean,"stdleche: ",lecheStd, "len: ", len(leche)
#45.3592 kg vacas de 2anos
#in 10**-2 mm
sel1 = np.array([41,46,54,44,42])
print "mean1: ", sel1.mean(),"std1: ",sel1.std()*math.sqrt(len(sel1))/math.sqrt(len(sel1)-1)
mean=alaMosca.mean()
std=alaMosca.std()#*math.sqrt(len(alaMosca))/math.sqrt(len(alaMosca)-1)

print "elements: ",len(alaMosca)

width = 1.0
#Defino 2 graficas de barras
hist, bin_edges = np.histogram(alaMosca,  bins=bins, density=True)
#print len(bin_edges),len(hist)
bin_edges = np.array(bin_edges)
hist = np.array(hist)
plt.bar(bin_edges[0:(len(hist)-0)] ,  hist, align='center', width = width, color = 'b', label='Poblacion')

x = sp.linspace(30, 60, 500)

cumlative = stats.norm.cdf(x, loc=mean, scale=2*std)

print "mean: ",mean,"std: ",std
normalDistrib = stats.norm.pdf(x, loc=mean, scale=std)

plt.plot(x,normalDistrib, color="k", label = " dens de prob ")


plt.xlim(30,60)


print "HACER UN MUESTREO de m valores:"
print "5 , 50, 100, 500"
tomaMuestreo = 200
muestreo1 = []
for i in range(tomaMuestreo):
	muestreo1.append(alaMosca[randint(0,99)])
	
print muestreo1	
print "mean muestreo: ", np.array(muestreo1).mean(),"std muestreo: ",np.array(muestreo1).std()*math.sqrt(tomaMuestreo)/math.sqrt(tomaMuestreo-1)
print 1/math.sqrt(tomaMuestreo)
muestreoHist1 = []
muestreobins1 = []
muestreoHist1, muestreobins1 = np.histogram(muestreo1,  bins=bins, density=True)
muestreobins1 = np.array(muestreobins1)
muestreoHist1 = np.array(muestreoHist1)

plt.bar(muestreobins1[0:(len(muestreoHist1)-0)] ,  muestreoHist1, align='center', width = width, color = 'red', label='Muestreo de %d'%(tomaMuestreo))

plt.legend( loc='upper left', numpoints = 1 )
plt.xlabel("Long ala mosca (10**-1mm)")
plt.ylabel("frel")
plt.title("Actividad Clase Sokal p80")
plt.show()

cuantosSigma = []
for i in range(tomaMuestreo):
	cuantosSigma.append((muestreo1[i]-alaMosca.mean())/alaMosca.std())
	
print cuantosSigma
newBins = np.array([x for x in range(-4, 4)])
sigmaHist, sigmaBins = np.histogram(cuantosSigma,  bins=newBins, density=False)
plt.bar(sigmaBins[0:(len(sigmaHist)-0)] ,  sigmaHist, align='center', width = width, color = 'k', label='Muestreo de %d'%(tomaMuestreo))
plt.legend( loc='upper left', numpoints = 1 )
plt.xlabel("Desviacion estandarizada ")
plt.ylabel("fabs")
plt.title("Actividad Clase Sokal p80")
plt.xlim(-4,4)

plt.show()
#normalizado
alaMoscaNorm = (alaMosca -mean)/std
lecheNorm = (leche - lecheMean)/lecheStd


def filliben(n):
	val = zeros(n)
	for i in range(n):
		if (i == n-1):
			val[i] = 0.5**(1/n)
		if(i>0 and i<n-1):
			val[i] = (i - 0.3175) / (n + 0.365)
        if (i == 0):
			val[i] = 1 - 0.5**(1/n)
	return val
#Testing For Normality
#By Henry C. Thode
#pag 31
x = filliben(100)
print len(x), len(alaMoscaNorm)
quantiles = stats.norm.ppf(x)
#, loc=mean, scale=std

plt.subplot(2, 1, 1)
plt.plot(quantiles,alaMoscaNorm, lw = 2, color = "r", label='Metodo Filliben')
stats.probplot(alaMoscaNorm, plot=plt)
plt.title('Cuantificacion del alejamiento de una distribucion normal ')
plt.legend( loc='upper left', numpoints = 1 )
plt.subplot(2, 1, 2)
stats.probplot(lecheNorm, plot=plt)

plt.show()

stats.probplot(alaMosca, plot=plt)
plt.plot( (0, 0),(30,60), 'k--')
plt.plot( (-1, -1),(30,60), 'k--')

plt.show()

