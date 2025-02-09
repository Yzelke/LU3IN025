import exemple # Pour pouvoir utiliser les methodes de exemple.py
import tme1
import time

print("bonjour")
maListe=tme1.lecture_matrice("PrefEtu.txt") # Execution de la methode lectureFichier du fichier exemple.
print(maListe)
maListe2=tme1.lecture_matriceSpe("PrefSpe.txt")
print(maListe2)
#print(len(maListe)) #Longueur de la liste.
#exemple.createFichierLP(maListe[0][0],int(maListe[1][0])) #Methode int(): transforme la chaine de caracteres en entier

prefEtu = tme1.lecture_matrice("PrefEtu.txt") # Execution de la methode lectureFichier du fichier exemple.
prefSpe = tme1.lecture_matriceSpe("PrefSpe.txt") # Execution de la methode lectureFichier du fichier exemple.
capacite = tme1.capacite("PrefSpe.txt")

affectation = tme1.algoGS(prefEtu, prefSpe, capacite)
print(affectation)
affectation2 = tme1.algoGS_parcours(prefEtu, prefSpe, capacite)
print(affectation2)

tme1.paire_instable(affectation, maListe, maListe2)
tme1.paire_instable([8,5,8,6,1,0,7,0,2,3,4], maListe, maListe2)
