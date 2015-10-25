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
#Adapted from: Thomas Haslwanter's work
##########################################################################################################

# Importo librerias
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import os
import seaborn as sns
from matplotlib.mlab import frange

sns.set(context='poster', style='ticks', palette='deep')

def skewness(ax):
    '''Distribuciones Normal y skewed (obliqua)'''
    
    t = frange(-6,10,0.1) # generate the desirded x-values
    normal = stats.norm.pdf(t,1,1.6)   
    chi2 = stats.chi2.pdf(t,3)
    
    ax.plot(t, normal, '--', label='normal')
    ax.plot(t, chi2, label='positive skew')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.legend()
    
def kurtosis(ax):
    ''' Distribuciones con diferente curtosis'''
    
    # Generate the data
    t = frange(-3,3,0.1) # generate the desirded x-values
    platykurtic = stats.laplace.pdf(t)
    
    wigner = np.zeros(np.size(t))
    wignerIndex = np.abs(t) <= 1
    wigner[wignerIndex] = 2/np.pi * np.sqrt(1-t[wignerIndex]**2)
    
    ax.plot(t, platykurtic, label='curtosis=3')
    ax.plot(t, wigner, '--', label='curtosis=-1')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.legend()

if __name__=='__main__':
    fig, axs = plt.subplots(1,2)    
    
    skewness(axs[0])
    kurtosis(axs[1])    
    plt.show()
