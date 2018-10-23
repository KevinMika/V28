import numpy as np
import csv
from uncertainties import ufloat
import uncertainties.unumpy as unp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#Hol dir die scheiSS Daten aus der csv
f = np.genfromtxt("messwerte.csv",delimiter=",",unpack=True,usecols=0)*10**6 #frequenzen halt,umrechung Mhz->hz
x = np.genfromtxt("messwerte.csv",delimiter=",",unpack=True,usecols=1)
#Bfeld für Helmholtz
def B(i):
    n = 156
    r = 0.1
    u0= 4*np.pi*10**(-7)
    B = (8*u0*n*i)/((125)**(1/2)*r)
    return B
#Konstanten
h = ufloat(6.626070040*10**(-34),0.000000081*10**(-34)) #https://physics.nist.gov/cgi-bin/cuu/Value?h
uB= ufloat(927.4009994*10**(-26),0.0000057*10**(-26))#https://physics.nist.gov/cgi-bin/cuu/Value?mub
#cm -> mA
y = x*50*10**(-3)
#gyromagnetisches Verhätnis
g = (h*f)/(uB*B(y))
#print(g) #zum sehen der Daten, nur testweise
#Splitten von g, damit python schreiben kann
gwert = unp.nominal_values(g)
gerr = unp.std_devs(g)
#print(gwert)
#print(gerr)
# umrechnungen wieder rückgängig
f1 = f*10**(-6)
x1 = x
B1 = B(y)*10**3
#runden zum schreiben
frund = ["%.3f" % elem for elem in f1]
xrund = ["%.1f" % elem for elem in x1]
Brund = ["%.2f" % elem for elem in B1]
gwertrund = ["%.2f" % elem for elem in gwert]
gerrrund= ["%.2f" % elem for elem in gerr]
#von Noah kopiert, kp wieso es funktioniert aber es funktioniert, Nachtrag: jetzt versteh ich den code lol
with open("messwerte.csv", "w") as f:
    writer= csv.writer(f)
    writer.writerows(zip(frund,xrund,Brund,gwertrund,gerrrund))
print(np.mean(gwert))
print(np.std(gwert))
