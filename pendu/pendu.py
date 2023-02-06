import random

niveau = input("Choisis un niveau de difficulté (Tranquille, Reflechis, Extrême, English Impossible) : ")
if niveau == "Tranquille":
    fichier = "mots1.txt"
if niveau == "Reflechis":
    fichier = "mots2.txt"
if niveau == "Extrême":
    fichier = "mots3.txt"
if niveau == "English Impossible":
    fichier = "mots4.txt"
    
mots = []
with open(fichier) as dico:
    for l in dico:
        mots.append(l.rstrip("\n"))
mot = random.choice(mots)

lettres = []
faux = 0
trouve = False
corps_plein = ["0", "/", "|", "\\", "/", "\\"]
corp = [" ", " ", " ", " ", " ", " "]

while not trouve:
    trouve = True
    print(" +---+")
    print(" |   |")
    print(" |   {}".format(corp[0]))
    print(" |  {}{}{}".format(corp[1], corp[2], corp[3]))   
    print(" |  {} {}".format(corp[4], corp[5]))
    print("_|_")
    print('"| |"\n')  
            
    
    for x in mot:
        if x in lettres:
            print(x, end="")
        else:
            trouve = False
            print("_", end=" ")
    print()
    print("\nLettres utilisées : \n", end="")
    for x in lettres:
        print(x, end=" - ")
    print()
    
    if faux > 5:
        print("Raté")
        print("Le mot était {}".format(mot))
        break
    
    if trouve:
        print("Bien joué, mot trouvé !")
        break
    
    lettre = input("Entrez une lettre: ")
    lettres.append(lettre)
    
    if lettre not in mot: 
        corp[faux] = corps_plein[faux]      
        faux += 1      
    

