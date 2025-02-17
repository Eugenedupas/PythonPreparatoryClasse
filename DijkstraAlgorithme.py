LLA=[[(1,85),(2,217),(4,173)],[(0,85),(5,80)],[(0,217),(6,186),(7,103)],[(7,183)],[(0,173),(9,502)],[(1,80),(8,250)],[(2,186)],[(2,103),(3,183),(9,167)],[(5,250),(9,84)],[(8,84),(7,167),(4,502)]]

def indicepoidsfaible(Poids,Fixe):
    s=9000
    q=0
    for i in range(len(Poids)):
        if Fixe[i]==False and Poids[i]<s:
            s=Poids[i]
            q=i
    return q

def dijkstra(LLA,dep):
    nbrefixe=0
    Fixe=[False for i in range(len(LLA))]
    Poids=[9000 for i in range(len(LLA))]
    Poids[dep]=0
    Preced=[-1 for i in range(len(LLA))]
    while nbrefixe<len(LLA):
        l=indicepoidsfaible(Poids,Fixe)
        Fixe[l]=True
        for i in range(len(LLA[l])):
            if Fixe[LLA[l][i][0]]==False:
                s=Poids[l]+LLA[l][i][1]
                if Poids[LLA[l][i][0]]>s:
                    Poids[LLA[l][i][0]]=s
                    Preced[LLA[l][i][0]]=l
        nbrefixe+=1
    return [Poids, Preced]
##pb pour indice 3(D) prced 7 et poids 458
chemin='/Users/eugenedupas/Desktop/dijkstraData.txt'
flux=open(chemin)
L = flux.readlines()
flux.close()
LLB=[]
for text in L:
    liste=text.split()
    liste2=[]
    for t in liste[1:]:
        np=t.split(",")
        liste2.append((int(np[0])-1,int(np[1])))
    LLB.append(liste2)
def pluscourt(poids,preced,dep,arr):
    L=[]
    l=arr
    while l != dep:
        L.append(l)
        l=preced[l]
    L.append(dep)
    return L.reverse(), poids[arr]
