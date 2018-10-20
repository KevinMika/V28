import numpy as np
import csv
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
f = np.genfromtxt("messwerte.csv",delimiter=",",unpack=True,usecols=0)*10**6 #frequenzen halt,umrechung Mhz->hz
x = np.genfromtxt("messwerte.csv",delimiter=",",unpack=True,usecols=1)*10**(-2) #umrechnung cm->m
def B(i):
    n = 156
    r = 0.1
    u0= 4*pi*10**(-7)
    B = (8*u0*n*i)/((125)**(1/2)*r)
    return B

h = ufloat(6.626070040*10**(-34),0.000000081*10**(-34)) #https://physics.nist.gov/cgi-bin/cuu/Value?h
uB= ufloat(927.4009994*10**(-26),0.0000057*10**(-26))#https://physics.nist.gov/cgi-bin/cuu/Value?mub
g= (h*f)/(uB*B(x))
print(g)
