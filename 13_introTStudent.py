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
#python 13_introTStudent.py
##########################################################################################################

import numpy as np
from scipy.stats import t as student_t
from matplotlib import pyplot as plt
import scipy.stats as stats
#------------------------------------------------------------
# Define the distribution parameters to be plotted
mu = 0
k_values = [50, 30, 5, 1]
linestyles = ['-', '--', ':', '-.']
x = np.linspace(-10, 10, 1000)

#------------------------------------------------------------
# plot the distributions
fig, ax = plt.subplots(figsize=(5, 3.75))
normalDistrib = stats.norm.pdf(x, loc=0, scale=1)
plt.plot(x,normalDistrib,color='red',lw=2,label="normal (${\mu=}0,{\sigma=}1$)")
for k, ls in zip(k_values, linestyles):
    dist = student_t(k, 0)

    if k >= 1E10:
        label = r'$\mathrm{t}(df=\infty)$'
    else:
        label = r'$\mathrm{t}(df=%d)$' % k

    plt.plot(x, dist.pdf(x), ls=ls, c='black', label=label)




plt.xlim(-5, 5)
#plt.ylim(0.0, 0.45)

plt.xlabel('$t_s$')
plt.ylabel("Probabilidad")
plt.title("Distribucion $t$-Student")

plt.legend()
plt.show()
