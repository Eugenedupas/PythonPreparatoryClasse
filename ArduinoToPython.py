#pip install pyserial
import serial

try:
    arduino=serial.Serial('/dev/cu.usbmodem142101',timeout=1)#rentrer le port
except:
    print("erreur")


rawdata=[] #liste voulue
compt=0

while compt<1000:# entre le nombre de valeurs voulue
    rawdata.append(str(arduino.readline()))
    compt+=1

def nettoie2(L):#nettoie la chaîne de caractères pour avoir une liste de valeurs
    A=[]
    for i in range(2,len(L)-2):
        A.append(int(L[i][7:13]))

    return A
clean2=nettoie2(rawdata)#la liste de valeurs


from PIL import Image

image = Image.open("../../_static/pillow.png")
image = image.convert('L')

image.show()
image.save('gray-pillow.jpeg', 'jpeg')


