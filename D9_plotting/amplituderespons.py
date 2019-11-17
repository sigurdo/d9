# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as plt
from pylab import *;plot();show()

def fillList(fList, hList, N, T_S):
    HList = []
    for f in fList:
        w = 2*np.pi*f*T_S
        Hw = complex(0, 0)
        for k in range(len(hList)):
            Hw += hList[k] * complex(np.cos(-w*k), np.sin(-w*k))
        HList.append(abs(Hw))
    return HList

#Plotter amplituderesponsen til et middelverdifilter med gitte parameter
def plottMiddel(start, end, N, T_S):
    hList = [1/N for k in range(N)]
    fList = range(start, end, 1)
    HList = fillList(fList, hList, N, T_S)
    plt.plot(fList, HList)
    return 0