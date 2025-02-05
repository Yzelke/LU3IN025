import tme1 
import time
import matplotlib.pyplot as plt

prefEtu = tme1.lecture_matrice("PrefEtu.txt") # Execution de la methode lectureFichier du fichier exemple.
prefSpe = tme1.lecture_matriceSpe("PrefSpe.txt") # Execution de la methode lectureFichier du fichier exemple.
capacite = tme1.capacite("PrefSpe.txt")

def cap(n) :
    return [int(n*0.15)] + [int(n*0.1)]*7 + [int(n*0.15)]


#paire = tme1.paire_instable(dict2, matrice_ce, matrice_cp)
#print(paire)

time_moyE = []
time_moyP = []
for i in range(200,2001,200):
    print(i)
    SumE =0
    SumP =0
    matrice_ce = tme1.matrice_CE(i)
    matrice_cp = tme1.matrice_CP(i)
    c = cap(i)

    for j in range(10):
        print(j)
        start = time.time()
        dict1 = tme1.algoGS(matrice_ce, matrice_cp, c)
        end = time.time()
        SumE += (end-start)
        #print("Temps pour algoGS côté étudiant :", end-start)

        start = time.time()
        dict2 = tme1.algoGS_parcours(matrice_ce, matrice_cp, c)
        end = time.time()
        SumP += (end-start)
        #print("Temps pour algoGS côté parcours :", end-start)

    time_moyE.append(SumE/10)
    time_moyP.append(SumP/10)
    
print(time_moyE)
l = [200,400,600,800,1000,1200,1400,1600,1800,2000]
plt.plot(l,time_moyE)
plt.plot(l,time_moyP)
plt.show()

#fghj
