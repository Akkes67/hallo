import random

def vraagAantalSpelers():
    aantalSpelers = int(input("hoeveel spelers zijn er?"))
    return aantalSpelers
def vraagBordSize():
    bordSizeGevonden= False
    while bordSizeGevonden == False:
        bordGroote = int(input('hoe lang moet de zijkant van je spelbord zijn '))
        if bordGroote > 10 or bordGroote < 5:
            print("tussen 1 en 11")
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

def kleineBotenNeerzetten(bordGroote):
    spelbordVolledig[random.randint(1,len(spelbordSpeler[1])-2)][random.randint(1,len(spelbordSpeler)-2)] = "S"
    bootTeller = 1
    if bordGroote > 7 :
        bordGroote = round(bordGroote/2,0)
    while bootTeller < bordGroote:
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
    
def groteBootCoordinaat(bordGroote):
    print("61")
    coordinaatGekozen = False
    while coordinaatGekozen == False:
        richting = random.randint(0,1)
        if richting == 0:
            x = random.randint(1, bordGroote)
            y = random.randint(2, bordGroote-1)
            print(x,y)
            botenInOmgeving = 0
            for i1 in range(y-2,y+3):
                for i2 in range(x-1,x+2):
                    if spelbordVolledig[i1][i2] == "S":
                        botenInOmgeving +=1
                        print("er is een boot")
            if botenInOmgeving == 0:
                coordinaatGekozen = True
        else:
            x = random.randint(2, bordGroote-1)
            y = random.randint(1, bordGroote)
            print(x,y)
            botenInOmgeving = 0
            for i1 in range(y-1,y+2):
                for i2 in range(x-2,x+3):
                    if spelbordVolledig[i1][i2] == "S":
                        botenInOmgeving +=1
                        print("er is een boot")
            if botenInOmgeving == 0:
                coordinaatGekozen = True
    print("85")
   
    return x,y,richting

def groteBotenNeerzetten(bordGroote):
    aantalBoten = 0
    while aantalBoten < 3:
        rawCoordinaat = groteBootCoordinaat(bordGroote)
        print(rawCoordinaat)
        x = rawCoordinaat[0]
        y = rawCoordinaat[1]
        richting = rawCoordinaat[2]
        if richting == 0:
            for i1 in range(y-1,y+2):
                spelbordVolledig[i1][x] = "S"
        else:
            for i1 in range(x-1,x+2):
                spelbordVolledig[y][i1] = "S" 
        aantalBoten+=1
    return spelbordVolledig
def vraagCooridinaat():
    coordinaatGekozen = False
    while coordinaatGekozen == False:    
        coordinaat = input("waar wil je schieten b.v.b.:a1 of c5\n")
        coordinaat = coordinaat.upper()
        if coordinaat[0].isalpha() == True and coordinaat[1].isalpha() == False:
            if coordinaat[1] == "1" and len(coordinaat)>2:
                getal = 10
            else:
                getal = coordinaat[1]
                getal = int(getal)
            if coordinaat[0] not in spelbordVolledig[0]:
                coordinaatGekozen = False
                print("dat is geen goede letter")
            elif getal > len(spelbordSpeler)-2:
                coordinaatGekozen = False
                print("dat is geen goed getal")
            elif spelbordSpeler[getal][ord(coordinaat[0])-64] =="O":
                print("die had je al domme oeleh")
                coordinaatGekozen = False
            else:
                coordinaatGekozen = True
        else:
            print("je moet een letter en een getal kiezen")
    return coordinaat
def schieten():
    ComplimentenLijst = ["goedzo", "Raak!!!", "Lekker Bezig!"]
    coordinaat = vraagCooridinaat()

    x = int(ord(coordinaat[0]))-64
    if len(coordinaat)==2:    
        y = int(coordinaat[1])
    else:
        y = 10
    if spelbordVolledig[y][x] == "S":
        print(random.choice(ComplimentenLijst))
        spelbordVolledig[y][x] = "G"
        spelbordSpeler[y][x] = "X"
        return True
    else:
        spelbordSpeler[y][x] = "O"
        return False
def tip():
    for rij in range(len(spelbordSpeler)-2):
        for kolom in range (len(spelbordSpeler)-2):
            if spelbordVolledig[rij][kolom] == 'S':
                kolomSchip = kolom
    print("onze radars pikken iets op in kolom" , chr(kolomSchip+64))
        
        
def botenTeller (): 
    botenTeller = 0
    for rij in range(len(spelbordVolledig)):
        for kolom in range(len(spelbordVolledig[1])):
           if spelbordVolledig[rij][kolom] == "S" :    
                botenTeller += 1
    return botenTeller

def opslaanProgressie(spelbordVolledig , spelbordSpeler):
    opslagFile = open("save.txt" , "w")
    opslagFile.write(str(spelbordVolledig))
    opslagFile.write("\n")
    opslagFile.write(str(spelbordSpeler))
    opslagFile.close()

if vraagAantalSpelers() == 1:
    beurtenTeller = 0
    bordGroote = vraagBordSize()
    spelbordVolledig = genereerBord(bordGroote)
    spelbordSpeler = genereerBord(bordGroote)
    if bordGroote < 7:
        spelbordVolledig = kleineBotenNeerzetten(bordGroote)
    else:
        spelbordVolledig = groteBotenNeerzetten(bordGroote)
    while botenTeller()>0:
        printBord()
        opslaanProgressie(spelbordSpeler , spelbordVolledig)
        if schieten() == True:
            tip()
        beurtenTeller += 1
    print("het koste je", beurtenTeller, " beurten")


