import random

def vraagAantalSpelers():
    aantalSpelers = int(input("hoeveel spelers zijn er? 1 of 2? \n"))               #vraagt welke versie van het spel je wilt spelen 1 speler of 2 speler
    return aantalSpelers
def vraagBordSize():
    bordSizeGevonden= False                                                 #vraagt hoe groot het bord moet zijn
    while bordSizeGevonden == False:
        bordGroote = int(input('hoe lang moet de zijkant van je spelbord zijn \n'))
        if bordGroote > 10 or bordGroote < 5:
            print("tussen 1 en 11")
        else:
            bordSizeGevonden = True
    return bordGroote
def genereerBord(bordGroote):                                                  #genereert het bord  
    bordGroote += 2
    spelbord = []
    for y in range(bordGroote):
        spelbord.append([])
        for x in range(bordGroote):                                           #als het een hoek coordinaat is plaatst het een X 
            if y == 0 or y == bordGroote-1:
                if x ==0 or x == bordGroote-1:
                    spelbord[y].append("X ")                                    #als het de bovenste of onderste rij is plaatst het letters a tot hoe groot het bord is
                else:
                    spelbord[y].append(chr(x+64)) 
            else:
                if x == 0 and y != 10:                                          #checkt of het een linker of rechter rand is
                    spelbord[y].append(" "+str(y))
                elif x == bordGroote-1 and y != 10:
                    spelbord[y].append(y)
                elif y == 10 and x == 0 or x == bordGroote-1:                   #als y 10 is haalt hij een spatie weg zodat het niet scheef staat 
                    spelbord[y].append(y)
                else:
                    spelbord[y].append('-')
    return spelbord

def printBord():
    for rij in range(len(spelbordSpeler)):                                      #print het bord
        for kolom in range(len(spelbordSpeler[1])):
            print(spelbordSpeler[rij][kolom],end=" ")
        print()


def printBord2speler(beurt):
    if beurt == 1:
        for rij in range(len(spelbordSpeler)):                                      #print het bord
            for kolom in range(len(spelbordSpeler[1])):
                print(spelbordSpeler[rij][kolom],end=" ")
            print()
        print("speler 1 bord")
    else:
        for rij in range(len(spelbordSpeler2)):                                      #print het bord
            for kolom in range(len(spelbordSpeler2[1])):
                print(spelbordSpeler2[rij][kolom],end=" ")
            print()
        print("speler 2 bord")

def kleineBotenNeerzetten(bordGroote):
    spelbordVolledig[random.randint(1,len(spelbordSpeler[1])-2)][random.randint(1,len(spelbordSpeler)-2)] = "S" #pakt een random getal dat op het bord zit
    bootTeller = 1                                                             #telt het aantal boten op het bord 
    if bordGroote > 7 :                                                     
        bordGroote = round(bordGroote/2,0)                         #om te bepalen hoeveel boten er op het bod geplaatst moeten worden delen we de grote van het bord door 2 en ronden we het af
    while bootTeller < bordGroote:
        rij = random.randint(1,len(spelbordVolledig[1])-2)          #plaatst de boten
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

    coordinaatGekozen = False                                   #bepaalt waar de grote boten geplaatst kunnen worden
    while coordinaatGekozen == False:
        richting = random.randint(0,1)                          #pakt een random getal die de richting bepaalt
        if richting == 0:
            x = random.randint(1, bordGroote)                   #zorgt ervoor dat de grote boot niet van het bord af gaat
            y = random.randint(2, bordGroote-1)

            botenInOmgeving = 0
            for i1 in range(y-2,y+3):
                for i2 in range(x-1,x+2):
                    if spelbordVolledig[i1][i2] == "S":
                        botenInOmgeving +=1
            if botenInOmgeving == 0:
                coordinaatGekozen = True
        else:
            x = random.randint(2, bordGroote-1)
            y = random.randint(1, bordGroote)

            botenInOmgeving = 0
            for i1 in range(y-1,y+2):
                for i2 in range(x-2,x+3):
                    if spelbordVolledig[i1][i2] == "S":
                        botenInOmgeving +=1
            if botenInOmgeving == 0:
                coordinaatGekozen = True
   
    return x,y,richting

def groteBotenNeerzetten(bordGroote):                   #plaatst de grote boten 
    aantalBoten = 0
    while aantalBoten < 3:
        rawCoordinaat = groteBootCoordinaat(bordGroote) #plaatst 3 grote boten
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
    coordinaatGekozen = False                   #vraagt de speler om een coordinaat
    while coordinaatGekozen == False:    
        coordinaat = input("waar wil je schieten b.v.b.:a1 of c5\n")
        coordinaat = coordinaat.upper()
        if coordinaat[0].isalpha() == True and coordinaat[1].isalpha() == False:    #zorgt ervoor dat coordinaat 10 gegeven mag worden
            if coordinaat[1] == "1" and len(coordinaat)>2:
                getal = 10
            else:                                                                   #geeft de speler restricties zodat hij niet coordinaten geeft die niet bestaan
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

    x = int(ord(coordinaat[0]))-64          #checkt of het een legitieme gok is 
    if len(coordinaat)==2:    
        y = int(coordinaat[1])
    else:
        y = 10
    if spelbordVolledig[y][x] == "S":           #checkt of er een boot zit op de gok
        print(random.choice(ComplimentenLijst))
        spelbordVolledig[y][x] = "G"
        spelbordSpeler[y][x] = "X"
        return True
    else:
        spelbordSpeler[y][x] = "O"
        return False
def tip():
    for rij in range(len(spelbordSpeler)-2):            #geeft de speler tips waar boten zijn door de kolommen te checkken 
        for kolom in range (len(spelbordSpeler)-2):     # en deze waarde te geven
            if spelbordVolledig[rij][kolom] == 'S':
                kolomSchip = kolom
    print("onze radars pikken iets op in kolom" , chr(kolomSchip+64))

def schieten2Speler(beurten):                                     
    ComplimentenLijst = ["goedzo", "Raak!!!", "Lekker Bezig!"]
    coordinaat = vraagCooridinaat()
    if beurt == 1:
        x = int(ord(coordinaat[0]))-64          #checkt of het een legitieme gok is 
        if len(coordinaat)==2:    
            y = int(coordinaat[1])
        else:
            y = 10
        if spelbordVolledig[y][x] == "S":           #checkt of er een boot zit op de gok
            print(random.choice(ComplimentenLijst))
            spelbordVolledig[y][x] = "G"
            spelbordSpeler[y][x] = "X"
            return True
        else:
            spelbordSpeler[y][x] = "O"
            return False
    else:
        x = int(ord(coordinaat[0]))-64          #checkt of het een legitieme gok is 
        if len(coordinaat)==2:    
            y = int(coordinaat[1])
        else:
            y = 10
        if spelbordVolledig2[y][x] == "S":           #checkt of er een boot zit op de gok
            print(random.choice(ComplimentenLijst))
            spelbordVolledig2[y][x] = "G"
            spelbordSpeler2[y][x] = "X"
            return True
        else:
            spelbordSpeler2[y][x] = "O"
            return False
        
def botenTeller (): 
    botenTeller = 0
    for rij in range(len(spelbordVolledig)):                #telt de boten door kolommen en rijen door te lopen op zoek naar de letter 'S'
        for kolom in range(len(spelbordVolledig[1])):
           if spelbordVolledig[rij][kolom] == "S" :    
                botenTeller += 1
    return botenTeller

def opslaanProgressie(spelbordSpeler , spelbordVolledig , bordGroote):
    opslagFile = open("save.txt" , "w")                   #opent een txt bestand en slaat spelbordSpeler, spelbordVolledig en beurten teller op
    opslagFile.write(str(bordGroote))
    opslagFile.write("\n")
    for i in range(len(spelbordSpeler[0])):
        for i2 in range(len(spelbordSpeler[0])):
            opslagFile.write(str(spelbordSpeler[i][i2]))
            opslagFile.write(",")
        opslagFile.write("\n")
    for i in range(len(spelbordVolledig[0])):
        for i2 in range(len(spelbordVolledig[0])):
            opslagFile.write(str(spelbordVolledig[i][i2]))
            opslagFile.write(",")
        opslagFile.write("\n")
    opslagFile.write(str(beurtenTeller))
    opslagFile.close()

def importerenOpslagfile(teller):
    opslagFile = open("save.txt" , "r")
    spelbordSpeler = []
    spelbordVolledig = []

    if teller == 0:
        bordGroote = int(opslagFile.readline())                         
        return bordGroote
    elif teller == 1:                                   #importeert de gegevens uit de opslag file met behulp van .pop()
        bordGroote = int(opslagFile.readline())
        for i in range(bordGroote+2):
            bordRegel = opslagFile.readline()
            bordRegel = bordRegel.split(",")
            bordRegel.pop()
            spelbordSpeler.append(bordRegel)
        return spelbordSpeler
    elif teller == 2:
        bordGroote = int(opslagFile.readline())
        print(bordGroote)
        for i in range(bordGroote+2):
            a = opslagFile.readline()
        for i in range(bordGroote+2):
            bordRegel = opslagFile.readline()
            bordRegel = bordRegel.split(",")
            bordRegel.pop()
            spelbordVolledig.append(bordRegel)
        return spelbordVolledig
    elif teller == 3:
        bordGroote = int(opslagFile.readline())
        for i in range((bordGroote+2)*2):
            a = opslagFile.readline()
        beurtenTeller = int(opslagFile.readline())
        return beurtenTeller


def vragenVerdergaan():
    verdergaan = str(input("wil je verdergaan? ja of nee?\n"))
    if verdergaan == "ja":                  #vraagt gebruiker de vraag of hij/zij verder wilt gaan.
        return True                         # zo bepalen wij of we de save file moeten importeren
    else:
        return False

############################################################################
#####################HOOFDPROGRAMMA
############################################################################

if vraagAantalSpelers() == 1:
    if vragenVerdergaan() == False:
        beurtenTeller = 0
        bordGroote = vraagBordSize()
        spelbordVolledig = genereerBord(bordGroote)
        spelbordSpeler = genereerBord(bordGroote)
        if bordGroote < 7:
            spelbordVolledig = kleineBotenNeerzetten(bordGroote)
        else:
            spelbordVolledig = groteBotenNeerzetten(bordGroote)
            spelbordVolledig = kleineBotenNeerzetten(bordGroote)

    else:
        for i in range (4):
            if i == 0:
                bordGroote = importerenOpslagfile(i)
            elif i == 1:
                spelbordSpeler = importerenOpslagfile(i)
            elif i == 2:
                spelbordVolledig = importerenOpslagfile(i)
            else:
                beurtenTeller = importerenOpslagfile(i)
        

    
    while botenTeller()>0:
        printBord()
        opslaanProgressie(spelbordSpeler , spelbordVolledig, bordGroote)
        if schieten() == False:
            tip()
        beurtenTeller += 1

    print("het koste je", beurtenTeller, " beurten")

else:
    beurt = 0
    beurtenTeller = 0
    bordGroote = vraagBordSize()
    spelbordVolledig = genereerBord(bordGroote)
    spelbordSpeler = genereerBord(bordGroote)
    spelbordSpeler2 = genereerBord(bordGroote)
    spelbordVolledig2 = genereerBord(bordGroote)
    if bordGroote < 7:
        spelbordVolledig = kleineBotenNeerzetten(bordGroote)
        spelbordVolledig2 = kleineBotenNeerzetten(bordGroote)
    else:
        spelbordVolledig = groteBotenNeerzetten(bordGroote)
        spelbordVolledig = kleineBotenNeerzetten(bordGroote)
        spelbordVolledig2 = groteBotenNeerzetten(bordGroote)
        spelbordVolledig2 = kleineBotenNeerzetten(bordGroote)
    while botenTeller()>0:
        beurt = (beurt + 1) % 2
        print(beurt)
        if beurt == 1:
            printBord2speler(beurt)
            print("speler 1 is nu aan de beurt")
        else:
            printBord2speler(beurt)
            print("speler 2 is nu aan de beurt")
        if schieten2Speler(beurt) == False:
            tip()
        beurtenTeller += 1

    print("het koste je", beurtenTeller, " beurten")