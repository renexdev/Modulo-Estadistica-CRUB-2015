#!/usr/bin/python

##########################################################################################################
# Modulo Bioestadistica - 2015 de la Universidad del Comahue. Centro Regional Bariloche
#http://crubweb.uncoma.edu.ar/
# Dr. Rene Cejas Bolecek
# email: reneczechdev@gmail.com
# licence: MIT. http://opensource.org/licenses/MIT 

#Codigo calculo combinatoria 
#Ejecutar:
#python 06_combinatoriaV1.py
##########################################################################################################


import math
import itertools #https://docs.python.org/2/library/itertools.html


def nCr(k,i):
    f = math.factorial
    return f(k) / f(i) / f(k-i)

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

def printk(k):
	for i in range(k+1):
		print i

        
    
if __name__ == '__main__':
	#print list(itertools.combinations('abcd',2))
	#k = 5
	#for i in range(k+1):
	#	print nCr(k,i)
	print binCoefGen(20)
	
