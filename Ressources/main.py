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
start = time.time()
affectation = tme1.algoGS_E("PrefEtu.txt", "PrefSpe.txt")
end = time.time()
print("Temps :", end-start)
#tme1.algoGS_S("PrefEtu.txt", "PrefSpe.txt")

tme1.paire_instable(affectation, maListe, maListe2)

# QUESTON 8

#for i in range(200,2001,200):
tme1.capacite_parcours(200)
tme1.prefEtu(11)
tme1.prefSpe(11)