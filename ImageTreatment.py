import imageio
import numpy as np
import matplotlib.pyplot as plt
photo=imageio.imread("/Users/eugenedupas/Downloads/Photos/rocket.jpg")
#plt.imshow(photo,cmap='gray')
#plt.show()
F_lissage=1/9*np.array([[1,1,1],[1,1,1],[1,1,1]])
F_contraste=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
F_repoussage=np.array([[-2,-1,0],[-1,1,1],[0,1,2]])
gradientx=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
gradienty=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
def coeffproduitcovolution(m,f,i,j):
    return f[0][0]*m[i-1][j-1]+f[0][1]*m[i-1][j]+f[0][2]*m[i-1][j+1]+f[1][0]*m[i][j-1]+f[1][1]*m[i][j]+f[1][2]*m[i][j+1]+f[2][0]*m[i+1][j-1]+f[2][1]*m[i+1][j]+f[2][2]*m[i+1][j+1]

def convolutiongris(m,f):
    L=[]
    for i in range(1,len(m)-1):#utiliser shape pour avoir les dimensions
        Q=[]
        for j in range(1,len(m[1])-1):
            #r=f[0][0]*m[i-1][j-1]+f[0][1]*m[i-1][j]+f[0][2]*m[i-1][j+1]+f[1][0]*m[i][j-1]+f[1][1]*m[i][j]+f[1][2]*m[i][j+1]+f[2][0]*m[i+1][j-1]+f[2][1]*m[i+1][j]+f[2][2]*m[i+1][j+1]
            r=coeffproduitcovolution(m,f,i,j)
            if r<0:
                Q.append(0)
            elif r>255:
                Q.append(255)
            else:
                Q.append(s)
            #Q.append(r)
        L.append(Q)
    return np.array(L,dtype='uint8')
#plt.imshow(convolutiongris(photo,F_repoussage),cmap='gray')
#plt.show()
def gradientcarregris(m):
    L=[]
    for i in range(1,len(m)-1):
        Q=[]
        for j in range(1,len(m[1])-1):
            r=coeffproduitcovolution(m,gradientx,i,j)**2+coeffproduitcovolution(m,gradienty,i,j)**2
            Q.append(r)
        L.append(Q)
    return np.array(L)

def contourgris(m,seuil):
    L=[]
    for i in range(1,len(m)-1):
        Q=[]
        for j in range(1,plen(m[1])-1):
            p=(coeffproduitcovolution(m,gradientx,i,j)**2+coeffproduitcovolution(m,gradienty,i,j)**2)**(1/2)#(gradientcarregris(m))*1/2
            if p<seuil:
                Q.append(0)
            else:
                 Q.append(255)
        L.append(Q)
    return np.array(L)
def convolution(m,f):
    n,p,z=m.shape
    L=[]
    for i in range(1,n-1):
        Q=[]
        for j in range(1,p-1):
            r=f[0][0]*m[i-1][j-1][0]+f[0][1]*m[i-1][j][0]+f[0][2]*m[i-1][j+1][0]+f[1][0]*m[i][j-1][0]+f[1][1]*m[i][j][0]+f[1][2]*m[i][j+1][0]+f[2][0]*m[i+1][j-1][0]+f[2][1]*m[i+1][j][0]+f[2][2]*m[i+1][j+1][0]
            v=f[0][0]*m[i-1][j-1][1]+f[0][1]*m[i-1][j][1]+f[0][2]*m[i-1][j+1][1]+f[1][0]*m[i][j-1][1]+f[1][1]*m[i][j][1]+f[1][2]*m[i][j+1][1]+f[2][0]*m[i+1][j-1][1]+f[2][1]*m[i+1][j][1]+f[2][2]*m[i+1][j+1][1]
            b=f[0][0]*m[i-1][j-1][2]+f[0][1]*m[i-1][j][2]+f[0][2]*m[i-1][j+1][2]+f[1][0]*m[i][j-1][2]+f[1][1]*m[i][j][2]+f[1][2]*m[i][j+1][2]+f[2][0]*m[i+1][j-1][2]+f[2][1]*m[i+1][j][2]+f[2][2]*m[i+1][j+1][2]
            P=[]
            if r<0:
                P.append(0)
            elif r>255:
                P.append(255)
            else:
                P.append(r)
            if v<0:
                P.append(0)
            elif v>255:
                P.append(255)
            else:
                P.append(v)
            if b<0:
                P.append(0)
            elif b>255:
                P.append(255)
            else:
                P.append(b)
            Q.append(P)
        L.append(Q)
    return np.array(L)


plt.imshow(convolution(photo,F_repoussage))
plt.show()






