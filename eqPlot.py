# McCabe-Thile equilibrium diagram

import math
import matplotlib.pyplot as plt

# Reference 

def eqCalc(a, b, c, l, cp, pm, pt):

    tI = (c[0] + b[0] / (math.log(pt, 10) - a[0])) * (-1)
    tF = (c[1] + b[1] / (math.log(pt, 10) - a[1])) * (-1)
    dT = (tF - tI) / 1000
    i = tI
    pA = []
    pB = []
    xA = []
    yA = []
    hL = []
    hV = []
    t = []
    alpha = []
    
    sum1 = 0        # x
    sum2 = 0        # x²
    sum3 = 0        # x³
    sum4 = 0        # x⁴
    sum5 = 0        # X⁵
    sum6 = 0        # X⁶
    sum7 = 0        # X⁷
    sum8 = 0        # x⁸
    sum9 = 0        # x⁹
    sum10 = 0       # x¹⁰
    sum11 = 0       # x¹¹
    sum12 = 0       # x¹²
    sum13 = 0       # y
    sum14 = 0       # xy
    sum15 = 0       # x²y
    sum16 = 0       # x³y
    sum17 = 0       # x⁴y
    sum18 = 0       # x⁵y
    sum19 = 0       # x⁶y    
    
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
        tmp4 = (cp[0] * tmp2 + cp[1] * (1 - tmp2)) * i  # h = cpm dt
        hL.append(tmp4)
        tmp5 = (cp[0] * tmp3 + cp[1] * (1 - tmp3)) * i + l[0] * tmp3 + l[1] * (1 - tmp3)
        hV.append(tmp5)
        alpha.append(tmp0 / tmp1)
        i += dT
        
        # FITTING SUMS

        sum1 += tmp2
        sum2 += tmp2 ** 2
        sum3 += tmp2 ** 3
        sum4 += tmp2 ** 4
        sum5 += tmp2 ** 5
        sum6 += tmp2 ** 6
        sum7 += tmp2 ** 7
        sum8 += tmp2 ** 8
        sum9 += tmp2 ** 9
        sum10 += tmp2 ** 10
        sum11 += tmp2 ** 11
        sum12 += tmp2 ** 12
        sum13 += tmp3
        sum14 += tmp2 * tmp3
        sum15 += tmp3 * (tmp2 ** 2)
        sum16 += tmp3 * (tmp2 ** 3)
        sum17 += tmp3 * (tmp2 ** 4)
        sum18 += tmp3 * (tmp2 ** 5)
        sum19 += tmp3 * (tmp2 ** 6)
    
    # Fitting equilibrium curve to a sixth grade polynomium
    
    sum0 = len(xA)
    # eqn1Sums = [sum0, sum1, sum2, sum3, sum4, sum5, sum6, sum13]
    # eqn2Sums = [sum1, sum2, sum3, sum4, sum5, sum6, sum7, sum14]
    # eqn3Sums = [sum2, sum3, sum4, sum5, sum6, sum7, sum8, sum15]
    # eqn4Sums = [sum3, sum4, sum5, sum6, sum7, sum8, sum9, sum16]
    # eqn5Sums = [sum4, sum5, sum6, sum7, sum8, sum9, sum10, sum17]
    # eqn6Sums = [sum5, sum6, sum7, sum8, sum9, sum10, sum11, sum18]
    # eqn7Sums = [sum6, sum7, sum8, sum9, sum10, sum11, sum12, sum19]

    # KRAMMER

    d = sum0 * sum2 * sum4 * sum6 * sum8 * sum10 * sum12 + sum1 * sum3 * sum5 * sum7 * sum9 * sum11 * sum6 + sum2 * sum4 * sum6 * sum8 * sum10 * sum5 * sum7 + sum3 * sum5 * sum7 * sum9 * sum4 * sum6 * sum8 + sum4 * sum6 * sum8 * sum3 * sum5 * sum7 * sum9 + sum5 * sum7 * sum2 * sum4 * sum6 * sum8 * sum10 + sum6 * sum1 * sum3 * sum5 * sum7 * sum9 * sum11 - sum6 ** 7 - (sum7 ** 6) * sum0 - (sum8 ** 5) * (sum1 ** 2) - (sum9 ** 4) * (sum2 ** 3) - (sum10 ** 3) * (sum3 ** 4) - (sum11 ** 2) * (sum4 ** 5) - sum12 * (sum5 ** 6)

    da0 = sum13 * sum2 * sum4 * sum6 * sum8 * sum10 * sum12 + sum1 * sum3 * sum5 * sum7 * sum9 * sum11 * sum19 + sum2 * sum4 * sum6 * sum8 * sum10 * sum18 * sum7 + sum3 * sum5 * sum7 * sum9 * sum17 * sum6 * sum8 + sum4 * sum6 * sum8 * sum16 * sum5 * sum7 * sum9 + sum5 * sum7 * sum15 * sum4 * sum6 * sum8 * sum10 + sum16 * sum14 * sum3 * sum5 * sum7 * sum9 * sum11 - (sum6 ** 6) * (sum19) - (sum7 ** 6) * sum13 - (sum8 ** 5) * sum1 * sum14 - (sum9 ** 4) * (sum2 ** 2) * (sum15) - (sum10 ** 3) * (sum3 ** 3) * sum16 - (sum11 ** 2) * (sum4 ** 4) * sum17 - sum12 * (sum5 ** 5) * sum18

    a0 = da0 / d

    da1 = sum0 * sum14 * sum4 * sum6 * sum8 * sum10 * sum12 + sum13 * sum3 * sum5 * sum7 * sum9 * sum11 * sum6 + sum2 * sum4 * sum6 * sum8 * sum10 * sum5 * sum19 + sum3 * sum5 * sum7 * sum9 * sum4 * sum18 * sum8 + sum4 * sum6 * sum8 * sum3 * sum17 * sum7 * sum9 + sum5 * sum7 * sum2 * sum16 * sum6 * sum8 * sum10 + sum6 * sum1 * sum15 * sum5 * sum7 * sum9 * sum11 - (sum6 ** 6) * sum18 - sum19 * (sum7 ** 5) * sum0 - (sum8 ** 5) * sum1 * sum13 - (sum9 ** 4) * (sum2 ** 2) * sum14 - (sum10 ** 3) * (sum3 ** 3) * sum15 - (sum11 ** 2) * sum16 * (sum4 ** 4) - sum12 * (sum5 ** 5) * sum17

    print(a0, a1)       # FOR TESTING

    print(f'Amount of points: {sum8}')

    del tmp0, tmp1, tmp2, tmp3, tmp4, tmp5, i
        
        

    return [t, pA, pB, xA, yA, alpha, hL, hV]

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

def hPlot (hL, hV, xA, yA):

    plt.plot(xA, hL, label = 'Liquid phase')
    plt.plot(yA, hV, label = 'Vapor phase')
    plt.show()

