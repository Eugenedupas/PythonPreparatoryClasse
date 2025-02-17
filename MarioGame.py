characters = [
    {
        "Name": "Mario",
        "Human": True,
        "Gender": "Male",
        "Profession": "Plumber",
        "Color": "Red"
    },
    {
        "Name": "Luigi",
        "Human": True,
        "Gender": "Male",
        "Profession": "Plumber",
        "Color": "Green"
    },
    {
        "Name": "Peach",
        "Human": True,
        "Gender": "Female",
        "Profession": "Princess",
        "Color": "Pink"
    },
    {
        "Name": "Yoshi",
        "Human": False,
        "Gender": "Undefined",
        "Profession": "Dinosaur",
        "Color": "Green"
    },
    {
        "Name": "Bowser",
        "Human": False,
        "Gender": "Male",
        "Profession": "Villain",
        "Color": "Green"
    },
    {
        "Name": "Toadette",
        "Human": False,
        "Gender": "Female",
        "Profession": "Mushroom",
        "Color": "Pink"
    }
]

def Q1():
    R=[]
    L=[]
    for i in characters:
        if i["Human"] not in R:
            R.append(i["Human"])
    for j in range(len(R)):
        print("Your character is a Human is", R[j])
        Question3 = input()
        if Question3 == "Yes":
            for u in range(len(characters)):
                if characters[u]["Human"]==R[j]:
                    L.append(characters[u]["Name"])
            return L
def Q2():
    R=[]
    L=[]
    for i in characters:
        if i["Gender"] not in R:
            R.append(i["Gender"])
    for j in range(len(R)):
        print("Is your character a", R[j])
        Question3 = input()
        if Question3 == "Yes":
            for u in range(len(characters)):
                if characters[u]["Gender"]==R[j]:
                    L.append(characters[u]["Name"])
            return L


def Q3():
    R=[]
    L=[]
    for i in characters:
        if i["Profession"] not in R:
            R.append(i["Profession"])
    for j in range(len(R)):
        print("Is your character a", R[j])
        Question3 = input()
        if Question3 == "Yes":
            for u in range(len(characters)):
                if characters[u]["Profession"]==R[j]:
                    L.append(characters[u]["Name"])
            return L
def Q4():
    R=[]
    L=[]
    for i in characters:
        if i["Color"] not in R:
            R.append(i["Color"])
    for j in range(len(R)):
        print("Is your character", R[j])
        Question3 = input()
        if Question3 == "Yes":
            for u in range(len(characters)):
                if characters[u]["Color"]==R[j]:
                    L.append(characters[u]["Name"])
            return L

def game():
    L = set(Q1()) & set(Q2()) & set(Q3()) & set(Q4())
    return L
