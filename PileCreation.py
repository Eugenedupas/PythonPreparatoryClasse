N=1000


def creerpile():
    return  [0]*(N+1)


def empiler(p,e):
    s=p[0]
    p[s+1]=e
    p[0]+=1

def depiler(p):
    s=p[0]
    p[0]-=1
    return p[s]

def pilevide(p):
    return p[0]==0

mapile=creerpile()
empiler(mapile,7)
empiler(mapile,8)
empiler(mapile,9)

def inverse_sommet(p):
    a=depiler(p)
    b=depiler(p)
    empiler(p,a)
    empiler(p,b) #p est modifié par effet de bord



def copi_pile(p):
    p_2=creerpile()
    p_resu=creerpile()
    while pilevide(p)==False:
        empiler(p_2,depiler(p))
    while not pilevide(p_2):
        e=depiler(p_2)
        empiler(p,e)
        empiler(p_resu,e)
    return p_resu
#####################

def creerpile2():
    return 1000*[0]

def empiler2(p,e):
    p[0]+=1
    p[p[0]]=e

def depiler2(p):
    p[0]-=1
    return p[p[0]+1]

def pilevide2(p):
    return p[0]==0

def inversesommet2(p):
    a=depiler2(p)
    b=depiler2(p)
    empiler2(p,a)
    empiler2(p,b)

def copiepile2(p):
    L=[]
    q=creerpile2()
    while pilevide2(p)==False:
        L.append(depiler(p))
    for i in range(len(L)):
        empiler(p,L[len(L)-i-1])
        empiler(q,L[len(L)-i-1])
    return q

def renverse2(p):
    L=[]
    q=creerpile2()
    while pilevide2(p)==False:
        L.append(depiler(p))
    for i in range(len(L)):
        empiler(p,L[i])
        empiler(q,L[i])
    return q

def taillepile2(p):
    g=0
    L=[]
    while pilevide2(p)==False:
        L.append(depiler2(p))
        g+=1
    for i in range(len(L)):
        empiler2(p,L[len(L)-i-1])
    return g

def parenthesage2(p):
    q=copiepile2(p)
    q1=creerpile2()
    q2=creerpile2()
    while pilevide2(q)==False: #on crée une liste avec les fermantes et une avec les ouvrantes
        r=depiler2(q)
        if r=='(' or r=='[' or r=='{':
            empiler2(q1,r)
        if r==')' or r==']' or r=='}':
            empiler2(q2,r)
    print(q1)
    print(q2)
    while pilevide2(q1)==False and pilevide2(q2)==False:# on compare les parenthese deux a deux
        r1=depiler2(q1)
        r2=depiler2(q2)
        if (r1=='(' and r2!=')') or (r1=='[' and r2!=']') or (r1=='{' and r2!='}'):
            return 'parenthese de type diferents'
#on regarde si il y a des parentheses seules
    if pilevide2(q1)==False:
        return 'manque fermante'
    if pilevide2(q2)==False:
        r=depiler2(q2)
        return 'manque ouvrante'

















