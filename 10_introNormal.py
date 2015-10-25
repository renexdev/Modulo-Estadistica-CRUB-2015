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
#python 09_introNormal.py
##########################################################################################################

# Importo librerias
import numpy as np
import pylab as P
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import math
import scipy.stats as stats
import scipy as sp

mean=0.0
std=1.0

x = sp.linspace(-4*std, 4*std, 50)

cumlative = stats.norm.cdf(x, loc=mean, scale=std)

normalDistrib = stats.norm.pdf(x, loc=mean, scale=std)

plt.plot(x,normalDistrib, color="blue", label = " dens de prob ")
plt.plot(x,cumlative, color="red", label = "Cumulante")
plt.plot( (-4*std, 0),(0.5, 0.5), 'k--')
plt.plot( (-4*std, -1*std),(0.158, 0.158), 'k--')
plt.plot( (-4*std, -2*std),(0.0228, 0.0228), 'k--')
plt.xlabel("Y")
plt.ylabel("Den de Prob Normal & Cumulative Probability")
plt.title("PDF & CDF for Gaussian of mean = {0} & std. deviation = {1}".format(mean, std))
plt.legend( loc='upper left', numpoints = 1 )
print "Cumulante at 0: ", stats.norm.cdf(0, loc=mean, scale=std)
print "Cumulante at sigma: ", stats.norm.cdf(-1*std, loc=mean, scale=std)
print "Cumulante at 2*sigma: ", stats.norm.cdf(-2*std, loc=mean, scale=std)
#Dibujo
plt.show()
