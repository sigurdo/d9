# -*- coding: utf-8 -*-

import numpy as np
import matplotlib as plt
from pylab import *
import amplituderespons as ampRes

startPlot = 0     #Frekvens å plotte fra i Hz 
endPlot = 1200    #Frekvens å plotte til i Hz
f_0 = 340         #f_0 i Hz
f_1 = 850         #f_1 i Hz
N_0 = 2           #N for middelverdifilter H0
N_1 = N_0         #N for middelverdifilter H1
T_S0 = 6.5*10**-4 #Samplingsperiode for S0 i sek
T_S1 = 2 * T_S0   #Samplingsperiode for S0 i sek

#def ampRes.plottMiddel(startfrekvens[Hz], sluttfrekvens[Hz], N, samplingsfrekvens T_S[Hz])
ampRes.plottMiddel(startPlot, endPlot, N_0, T_S0) #Plotter amplituderespons for H1
ampRes.plottMiddel(startPlot, endPlot, N_1, T_S1) #Plotter ampituderesponse for H2

plt.plot([f_0, f_0], [0, 1]) #Plotter vertikal linje ved f = f_0
plt.plot([f_1, f_1], [0, 1]) #Plotter vertikal linje ved f = f_1
plt.xlabel("f[Hz]")
plt.legend(["H0", "H1", "f_0", "f_1"])

plt.savefig("amplituderesponser.png", dpi=400)
