# -*- coding: utf-8 -*-

import numpy as np
import matplotlib as plt
from pylab import *;plot();show()
#import cmath

N = 2
T_S = 6.5*10**-4

h = [1/N for k in range(N)]
print(h)

H = []
wList = []
FList = []
for i in range(500):
    wList.append(i * 0.01)
    FList.append(wList[i]/(T_S * 2 * np.pi))

for i in range(len(wList)):
    w = wList[i]
    Hw = complex(0, 0)
    for k in range(N):
        Hw += h[k] * complex(np.cos(-w*k), np.sin(-w*k))
    H.append(abs(Hw))
    if w == 1.07:
        print("w1:", H[i])
    elif w == 2.67:
        print("w2:", H[i])
        
plt.plot(FList, H)

T_S *= 2

h = [1/N for k in range(N)]
print(h)

H = []
wList = []
FList = []
for i in range(1000):
    wList.append(i * 0.01)
    FList.append(wList[i]/(T_S * 2 * np.pi))

for i in range(len(wList)):
    w = wList[i]
    Hw = complex(0, 0)
    for k in range(N):
        Hw += h[k] * complex(np.cos(-w*k), np.sin(-w*k))
    H.append(abs(Hw))
    if w == 1.07:
        print("w1:", H[i])
    elif w == 2.67:
        print("w2:", H[i])

plt.plot(FList, H)
plt.plot([340, 340], [0, 1])
plt.plot([850, 850], [0, 1])
plt.xlabel("f[Hz]")
#plt.ylabel("H(f)[1]")
plt.legend(["H0", "H1", "f_0", "f_1"])

plt.savefig("test.png", dpi=400)
"""
for i in range(len(FList)):
    if FList[i] > 340:
        print("f1:", H[i])
        break

for i in range(len(FList)):
    if FList[i] > 850:
        print("f2:", H[i])
        break
"""
        