# -*- coding: utf-8 -*-

import numpy as np
import matplotlib as plt
from pylab import *;plot();show()
import amplituderespons as ampRes

startPlot = 0  #Frekvens å plotte fra i Hz 
endPlot = 1200 #Frekvens å plotte til i Hz
N0 = 2
N1 = N0
T_S0 = 6.5*10**-4
T_S1 = 2 * T_S0

#ampRes.plottMiddel(startfrekvens[Hz], sluttfrekvens[Hz], N, samplingsfrekvens T_S[Hz])
ampRes.plottMiddel(startPlot, endPlot, N0, T_S0) #Plotter amplituderespons for H1
ampRes.plottMiddel(startPlot, endPlot, N1, T_S1) #Plotter ampituderesponse for H2

plt.plot([340, 340], [0, 1])
plt.plot([850, 850], [0, 1])
plt.xlabel("f[Hz]")
plt.legend(["H0", "H1", "f_0", "f_1"])

plt.savefig("test.png", dpi=400)
