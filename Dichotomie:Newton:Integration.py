def zero_dicho(f,a,b,epsilon):
    while abs(b-a)>epsilon:
        if (f(a)*f((a+b)/2))>0:
            a=(a+b)/2
        else:
            b=(a+b)/2
    return (a+b)/2

def dichotomie(f,eps,a,b):
    while abs(f(a)-f(b))>eps:
        t=(a+b)/2
        if f(a)*f(t)>0:
            a=t
        else:
            b=t
    return t

def newton(f,g,a,eps):
    while abs(f(a))>eps:
        a=-f(a)/g(a)+a
    return a

def f():
    return x**3

def integraion(f,a,b,eps):
    q=0
    t=a
    while t-b<0:
        q+=f(t)*eps
        t+=eps
    return q
































