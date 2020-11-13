import random

spelbordVolledig = 0 
spelbordSpeler = 0
def vraagBordSize():
    bordSizeGevonden= False
    while bordSizeGevonden == False:
        bordGroote = int(input('hoe lang moet de zijkant van je spelbord zijn '))
        if bordGroote > 10:
            print("het grootste is 10")
        else:
            bordSizeGevonden = True
    return bordGroote
def genereerBord(bordGroote):        
    bordGroote += 2
    spelbord = []
    for y in range(bordGroote):
        spelbord.append([])
        for x in range(bordGroote):
            if y == 0 or y == bordGroote-1:
                if x ==0 or x == bordGroote-1:
                    spelbord[y].append("X ")
                else:
                    spelbord[y].append(chr(x+64)) 
            else:
                if x == 0 and y != 10:
                    spelbord[y].append(" "+str(y))
                elif x == bordGroote-1 and y != 10:
                    spelbord[y].append(y)
                elif y == 10 and x == 0 or x == bordGroote-1:
                    spelbord[y].append(y)
                else:
                    spelbord[y].append('-')
    return spelbord

def printBord():
    for rij in range(len(spelbordSpeler)):
        for kolom in range(len(spelbordSpeler[1])):
            print(spelbordSpeler[rij][kolom],end=" ")
        print()

def botenNeerzetten(bordGroote):
    spelbordVolledig[random.randint(1,len(spelbordSpeler[1])-2)][random.randint(1,len(spelbordSpeler)-2)] = "S"
    bootTeller = 1
    while bootTeller < 3:
        rij = random.randint(1,len(spelbordVolledig[1])-2)
        kolom = random.randint(1,len(spelbordVolledig[1])-2)
        botenInOmgeving= 0
        for i1 in range(rij-1,rij+2):
            for i2 in range(kolom-1,kolom+2):
                if spelbordVolledig[i1][i2] == "S":
                    botenInOmgeving +=1
        if botenInOmgeving >0:
            bootTeller = bootTeller
        else:
            bootTeller += 1
            spelbordVolledig[rij][kolom] = "S"
    return spelbordVolledig
    

def vraagCooridinaat():
    coordinaatGekozen = False
    while coordinaatGekozen == False:    
        coordinaat = input("captain, waar gaan we schieten? ")
        coordinaat = coordinaat.upper()
        if len(coordinaat) != 2:
            print("je moet 2 dingen zeggen, captain")
        elif coordinaat[0] not in spelbordVolledig[0]:      
            print("dat is geen correct coördinaat, captain")
        elif coordinaat[1].isdigit() == False:
            print("dat is geen correct coördinaat, captain")
        elif int(coordinaat[1]) > len(spelbordSpeler)-2:
            print("dat is geen correct coördinaat, captain")
        elif spelbordSpeler[int(coordinaat[1])][ord(coordinaat[0])-64] !="-":
            print("die hadden we al, captain")
        else:
            coordinaatGekozen = True
    return coordinaat

def schieten():
    ComplimentenLijst = ["goedzo", "Raak!!!", "Lekker Bezig!"]
    coordinaat = vraagCooridinaat()
    x = int(ord(coordinaat[0]))-64
    y = int(coordinaat[1])
    if spelbordVolledig[y][x] == "S":
        print(random.choice(ComplimentenLijst))
        spelbordVolledig[y][x] = "G"
        spelbordSpeler[y][x] = "X"
    else:
        print("mis.....")
        spelbordSpeler[y][x] = "O"

def botenTeller (): 
    botenTeller = 0
    for rij in range(len(spelbordVolledig)):
        for kolom in range(len(spelbordVolledig[1])):
           if spelbordVolledig[rij][kolom] == "S" :    
                botenTeller += 1
    return botenTeller


beurtenTeller = 0
bordGroote = vraagBordSize()
spelbordVolledig = genereerBord(bordGroote)
spelbordSpeler = genereerBord(bordGroote)
spelbordVolledig = botenNeerzetten(bordGroote)
while botenTeller() > 0:
    printBord()
    schieten()
    beurtenTeller += 1
print("het koste je maar",beurtenTeller,"schoten")
   
