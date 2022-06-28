# main

from PyQt5.QtWidgets import QApplication, QLabel
from eqPlot import *

app = QApplication([])

a = [4.02023, 4.05075]  # base 10
b = [1263.909, 1356.36]
c = [216.432, 209.635]
l = [7593, 8224]        # kcal/kmol
cp = [53.8074, 60.7544] # kcal/mol °C
pm = [100.2, 114.2]     
pt = 1.013              # bar

eq = eqCalc(a, b, c, l, cp, pm, pt)
mcPlot(eq[3], eq[4])
txPlot(eq[0], eq[3], eq[4])

