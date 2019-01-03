import fiabilipy
import time
from fiabilipy import Component
from fiabilipy import Component, Markovprocess
A0, A1 , A2  = [Component('A{}'.format(i), 700, 200 ,300 ) for i in range(3)]
M0, M1 , M2 = [Component('M{}'.format(i), 650, 450, 330 ) for i in range(3)]
A3=Component('A3',120)
M3=Component('M3',110)
compA=(A0,A1,A2,A3)
compM=(M0,M1,M2,M3)
components = (A0,A1,A2,A3,M0,M1,M2,M3)
initstates = {0: 0.6, 1:0.40}
process = Markovprocess(components, initstates)
def normal(x):
 return all(x)
def available1(x):
    for i in compA:
        return (x[0]or x[i] or x[i+1])
def available2(x):
    for j in compM:
        return (x[0] or x[j] or x[j+1])

def available(x):
    return (available1) and (available2)
def damaged(x):
 return available(x) and not(normal(x))
def faulty(x):
 return not available(x)
print(process.value(100, available))
print(process.value(100,damaged))
import matplotlib
matplotlib.use('TkAgg')
import pylab as plt
states = {u'normal': normal,
          u'available': available,
          u'damaged': damaged,
          u'faulty': faulty,
         }
timerange = range(0, 60000, 10000)
for (name, func) in states.items():
     proba = [process.value(t, func) for t in timerange]
     plt.plot(timerange, proba, label=name)

plt.legend()
plt.gca().set_aspect('auto')
plt.show()

