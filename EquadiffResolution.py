import math
import numpy as np
import matplotlib.pyplot as plt
g=9.81 #m.s**-2
C=0.20 #kg.m-1
m=  90 #kg
H=8000 #m
t0=0 #s
z0=39376 #m

def saut(tf,N):
    z=[z0] #liste des positions
    zp=[0] #liste des dérives premieres
    t=[t0]
    h=(tf-t0)/N
    for n in range(N):
        z.append(z[n]+h*zp[n])
        zp.append(zp[n]+h*((C/m)*math.exp(-z[n]/H)*zp[n]**2-g))
        t.append(t[n]+h)
    y1=np.array(z)
    yp1=np.array(zp)
    t1=np.array(t)
    plt.plot(t,yp1)
    plt.show()

#######
#exo8
def proiepreddateur(x0,y0,a,b,c,d,dt,N):
    x=[x0]
    y=[y0]
    t=[0]
    for i in range(N):
        x.append(x[i]+dt*x[i]*(a-b*y[i]))
        y.append(y[i]-dt*y[i]*(c-d*x[i]))
        t.append(t[i]+dt)
    plt.plot(t,x)
    plt.plot(t,y)
    plt.show()
#    return x,y,t
#exo9
#12 d_proies=Yn[0]*(alpha-beta*Yn[1])
#13 d_predateurs=Yn[1](gamma-delta*Yn[0])

#exo10
def parachute(tf,N):
    dt=(tf-t0)/N
    z=[z0]
    dz=[0]
    t=[0]
    for n in range(N):
        dz.append(dz[n]+dt*(C/m)*math.exp(-z[n]/H)*dz[n]**2-g)
        z.append(z[n]+dt*dz[n])
        t.append(t[n]+dt)
    plt.plot(t,dz)
    plt.show()









































