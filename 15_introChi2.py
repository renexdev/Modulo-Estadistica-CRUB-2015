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
#python 15_introChi2.py
##########################################################################################################

import numpy as np
from scipy.stats import t as student_t
from matplotlib import pyplot as plt
import scipy.stats as stats
from scipy.stats import chi2
#------------------------------------------------------------
# Define the distribution parameters to be plotted
mu = 0
k_values = [ 5, 2, 1]
linestyles = ['-', '--', ':', '-.']
x = np.linspace(0, 25, 1000)

#------------------------------------------------------------
# plot the distributions
fig, ax = plt.subplots(figsize=(5, 3.75))

for k, ls in zip(k_values, linestyles):
    dist = chi2(k, 0)

    if k >= 1E10:
        label = r'$\chi ^2(df=\infty)$'
    else:
        label = r'$\chi ^2(df=%d)$' % k

    plt.plot(x, dist.pdf(x), ls=ls, c='black', label=label)




plt.xlim(0, 25)
plt.ylim(0.0, 0.45)

plt.xlabel('$\chi ^2$')
plt.ylabel("Probabilidad")
plt.title("Distribucion $\chi ^2$")

plt.legend()
plt.show()
