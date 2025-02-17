import math

def phase(x):
    Q=2.5
    if x>1:
        phi=math.atan(x/Q)-math.atan(x/(Q*(1-x**2)))-math.pi
    elif 0<=x<1 :
        phi=math.atan(x/Q)-math.atan(x/(Q*(1-x**2)))
    else:
        return "error"
    return phi

import numpy
import matplotlib.pyplot


def tracer():
    x1=[]
    y1=[]
    t= 0.1
    for i in range(100):
        y1.append(phase(t))
        x1.append(t)
        t+=0.1
    x=numpy.array(x1)
    y=numpy.array(y1)
    matplotlib.pyplot.plot(x,y)
    matplotlib.pyplot.title("diagramme de phase")
    matplotlib.pyplot.xlabel("x")
    matplotlib.pyplot.ylabel("déphasage(en radian)")

    matplotlib.pyplot.grid(which="both",linestyle='--')
    matplotlib.pyplot.xscale('log')
    matplotlib.pyplot.show()

#x=[1,2,3]
#yn=xn**2
#y=[i**2 for i in x]


