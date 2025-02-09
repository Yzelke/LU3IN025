import tme1 
import time
import matplotlib.pyplot as plt

prefEtu = tme1.lecture_matrice("PrefEtu.txt") # Execution de la methode lectureFichier du fichier exemple.
prefSpe = tme1.lecture_matriceSpe("PrefSpe.txt") # Execution de la methode lectureFichier du fichier exemple.
capacite = tme1.capacite("PrefSpe.txt")


def cap(n):
    base = n // 9
    reste = n % 9
    capacite = [base] * 9
    for i in range(reste):
        capacite[i] += 1
    return capacite

#paire = tme1.paire_instable(dict2, matrice_ce, matrice_cp)
#print(paire)

time_moyE = []
time_moyP = []
for i in range(200,2001,200):
    SumE =0
    SumP =0
    matrice_ce = tme1.matrice_CE(i)
    matrice_cp = tme1.matrice_CP(i)
    c = cap(i)

    for j in range(10):
        start = time.perf_counter()
        dict1 = tme1.algoGS(matrice_ce, matrice_cp, c)
        end = time.perf_counter()
        SumE += (end-start)
        #print("Temps pour algoGS côté étudiant :", end-start)
        
        #tme1.paire_instable(dict1, matrice_ce, matrice_cp)
        start = time.perf_counter()
        dict2 = tme1.algoGS_parcours(matrice_ce, matrice_cp, c)
        end = time.perf_counter()
        SumP += (end-start)
        #print("Temps pour algoGS côté parcours :", end-start)

    time_moyE.append(SumE/10)
    time_moyP.append(SumP/10)
    
print(time_moyE)
print(time_moyP)
l = [200,400,600,800,1000,1200,1400,1600,1800,2000]
plt.title("Temps moyen en fonction du nombre d'étudiants")
plt.plot(l, time_moyE, label="Moyenne de temps Étudiant")  
plt.plot(l, time_moyP, label="Moyenne de temps Parcours") 
plt.xlabel("Nombre d'étudiants")
plt.ylabel("Temps (en secondes)")
plt.legend()
plt.show()
