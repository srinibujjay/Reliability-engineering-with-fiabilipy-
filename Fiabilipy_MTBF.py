import fiabilipy
from fiabilipy import Component, Markovprocess
A0, A1 , A2 = [Component('A{}'.format(i), 1e-4, 1.1e-3 ,1.1e-3) for i in range(3)]
M0, M1 , M2 = [Component('M{}'.format(i), 1e-3, 1.2e-2, 1.2e-3) for i in range(3)]
compA=(A0,A1,A2)
compM=(M0,M1,M2)
components = (compA+compM)
initstates = {0: 0.9, 1:0.1}
process = Markovprocess(components, initstates)
def normal(x):
 return all(x)
def available(x):
 return (x[0] or x[1]or x[2]) and (x[3] or x[4] or x[5])
def damaged(x):
 return available(x) and not(normal(x))
def faulty(x):
 return not available(x)
print(process.value(150, available))
print(process.value(100,damaged))
import matplotlib
matplotlib.use('TkAgg')
import pylab
states = {u'normal': normal,
          u'available': available,
          u'damaged': damaged,
          u'faulty': faulty,
         }
timerange = range(0, 6000, 10)
for (name, func) in states.items():
     proba = [process.value(t, func) for t in timerange]
     pylab.plot(timerange, proba, label=name)
pylab.legend()
pylab.show()
pylab.gca().set_aspect('auto')
pylab.gcf().clear()

