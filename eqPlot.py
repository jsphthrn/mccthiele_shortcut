# McCabe-Thile equilibrium diagram

import math
import matplotlib.pyplot as plt

# Reference 

def eqCalc(a, b, c, l, cp, pm, pt):

    tI = (c[0] + b[0] / (math.log(pt, 10) - a[0])) * (-1)
    tF = (c[1] + b[1] / (math.log(pt, 10) - a[1])) * (-1)
    dT = (tF - tI) / 10
    i = 0
    if i == 0:
        i = tI
        pA = []
        pB = []
        xA = []
        yA = []
        t = []
        alpha = []
    
    while tI <= i <= tF:        # Build a table
        
        tmp0 = 10 ** (a[0] - b[0] / (i + c[0]))
        pA.append(tmp0)
        tmp1 = 10 ** (a[1] - b[1] / (i + c[1]))
        pB.append(tmp1)
        tmp2 = (pt - tmp1) / (tmp0 - tmp1)
        xA.append(tmp2)
        tmp3 = tmp0 * tmp2 / pt
        yA.append(tmp3)
        t.append(i)
        alpha.append(tmp0 / tmp1)
        i += dT
            
    del tmp0, tmp1, tmp2, tmp3, i
    return [t, pA, pB, xA, yA, alpha]

def mcPlot(xA, yA):
    
    x = (0, 1)
    y = (0, 1)
    ref = (x,y)     # Reference line
    plt.plot(ref[0],ref[1], label='Reference')   # Print reference
    plt.plot(xA, yA, label = 'equilibrium') 
    plt.show()   

def txPlot(t, xA, yA):

    plt.plot(xA, t, label = 'Liquid phase')
    plt.plot(yA, t, label = 'Vapor phase')
    plt.show()

