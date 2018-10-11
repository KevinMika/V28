import numpy as np
import csv
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
output1rund = [ "%.2f"  % elem for elem in output1]
output2rund = [ "%.2f"  % elem for elem in output1]
with open(messwerte1.csv, w) as f:
    writer= csv.writer(f)
    writer.writerows(zip(output1rund,output2rund))
