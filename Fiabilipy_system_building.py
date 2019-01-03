import fiabilipy
from fiabilipy import Component
from sympy import Symbol
t = Symbol('t', positive=True)
comp = Component('C0', 1e-4)
print(comp.reliability(100))
print(comp.reliability(t=33))
print(comp.mttf)
from fiabilipy import System
power = Component('P0', 1e-6)
motor = Component('M0', 1e-3)
print(power)
S = System()
S['E'] = [power]
S[power] = [motor]
S[motor] = 'S'
print(S.reliability(t))
print(S.mttf)
print(float(S.mttf))
a, b, c, d, e, f, g = [Component('C%i' % i, 1e-4) for i in range(7)]
S = System()
S['E'] = [a, b, c, g]
S[a] = S[g] = S[e] = S[d] = 'S'
S[b] = S[c] = [f]
S[f] = [e, d]
print(a)
print(S.mttf)
print(float(S.mttf))
print(S.reliability(t))
import pylab as p
a, b = Component('a', 1e-5), Component('b', 1e-7)
S = System()
S['E'] = [a, b]
S[a] = S[b] = 'S'
timerange = range(0, 20000, 100)
reliability = [S.reliability(t) for t in timerange]
p.plot(timerange, reliability)
p.show()