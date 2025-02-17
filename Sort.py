import random
from time import perf_counter
import numpy as np
import matplotlib.pyplot as plt

def triabulle(T):
    for i in range(len(T)-1,0,-1):

        for j in range(0,i):
            if T[j+1]<T[j]:
                T[j],T[j+1]=T[j+1],T[j]
    return T

def listealeatoire(n,mini,maxi):
    L=[]
    for  i in range(n):
        L.append(random.randint(mini,maxi))
    return L

## Tri rapide - quicksort - en place

# Fonction de partitionnement de la liste
def partition(L,i_debut,i_fin,i_pivot):
    # 1ère étape : on échange le pivot avec le dernier élément
    L[i_fin], L[i_pivot] = L[i_pivot], L[i_fin]
    # 2ème étape : partitionnement
    ip = i_debut
    for i in range(i_debut,i_fin):
        if L[i] < L[i_fin]:
            L[i], L[ip] = L[ip], L[i]
            ip += 1
        # print("partition ", ", i=", i, ", ip=",ip)
    # 3ème étape : on replace le pivot au bon endroit
    L[ip], L[i_fin] = L[i_fin], L[ip]
    # 4ème étape : on renvoie l'indice du pivot
    # print("i_pivot=", ip, L[ip])
    return(ip)

def tri_rapide(L, i_debut, i_fin):
    # print("i_debut=",i_debut,", i_fin=", i_fin)
    # On ne trie que s'il y a quelque chose à trier
    if i_debut < i_fin:
        i_pivot = (i_fin + i_debut)//2
        i_pivot = partition(L,i_debut,i_fin,i_pivot)
        tri_rapide(L,i_debut,i_pivot-1)
        tri_rapide(L,i_pivot+1,i_fin)

def appeltrirapide(L):
    tri_rapide(L,0,len(L)-1)

def tempsmoyen(fcttri,n,nombretest):
    s=0.0
    for i in range(nombretest):
        L=listealeatoire(n,0,1000000)
        tdebut=perf_counter()
        fcttri(L)
        tfin=perf_counter()
        s+=tfin-tdebut
    return s/nombretest


