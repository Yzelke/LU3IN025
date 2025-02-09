from collections import deque
import random
from random import sample
import copy
import heapq

def lectureFichier(s): # Definition d'une fonction, avec un parametre (s). Ne pas oublier les ":"
    monFichier = open(s, "r") # Ouverture en lecture. Indentation par rapport a la ligne d'avant (<-> bloc).
    contenu = monFichier.readlines() # Contenu contient une liste de chainces de caracteres, chaque chaine correspond a une ligne       
    monFichier.close() #Fermeture du fichier
    contenu[0]=contenu[0].split()     # ligne.split() renvoie une liste de toutes les chaines contenues dans la chaine ligne (separateur=espace)
    contenu[1]=contenu[1].split()
    return contenu
    # Commandes utiles:
    # n=int(s) transforme la chaine s en entier.
    # s=str(n) l'inverse
    # Quelques methodes sur les listes:
    # l.append(t) ajoute t a la fin de la liste l
    # l.index(t) renvoie la position de t dans l (s'assurer que t est dans l)
    # for s in l: s vaut successivement chacun des elements de l (pas les indices, les elements)

def lecture_matrice(s) : 
    monFichier = open(s, "r") # Ouverture en lecture. Indentation par rapport a la ligne d'avant (<-> bloc).
    contenu = monFichier.readlines() # Contenu contient une liste de chainces de caracteres, chaque chaine correspond a une ligne       
    monFichier.close() #Fermeture du fichier
    nbEtu = int(contenu[0])
    for i in range(nbEtu+1):
        contenu[i] = contenu[i].split()
    
    matrice = []            
    for i in range(nbEtu):
        a = []
        for j in range(11):
            if(j>=2) : 
                a.append(int(contenu[i+1][j]))
        matrice.append(a)    
                

    return matrice

def lecture_matriceSpe(s) : 
    monFichier = open(s, "r") # Ouverture en lecture. Indentation par rapport a la ligne d'avant (<-> bloc).
    contenu = monFichier.readlines() # Contenu contient une liste de chainces de caracteres, chaque chaine correspond a une ligne       
    monFichier.close() #Fermeture du fichier
    nbSpe = 9
    for i in range(nbSpe+2):
        contenu[i] = contenu[i].split()

    
    nbEtu = int(contenu[0][1])
    matrice = []           
    for i in range(nbSpe):
        a = []
        for j in range(13):
            if(j>=2) : 
                a.append(int(contenu[i+2][j]))
        matrice.append(a)    
                

    return matrice


#Question 3

def capacite(s):
    monFichier = open(s, "r") # Ouverture en lecture. Indentation par rapport a la ligne d'avant (<-> bloc).
    contenu = monFichier.readlines() # Contenu contient une liste de chainces de caracteres, chaque chaine correspond a une ligne       
    monFichier.close() #Fermeture du fichier
    capacite=contenu[1].split()
    capacite=capacite[1:]
    cap = []
    for i in range(len(capacite)):
        cap.append(int(capacite[i]))
    #print(cap)
    return cap

def algoGS(prefEtu1, prefSpe1, cap1):
    prefEtu = copy.copy(prefEtu1)  
    prefSpe = copy.copy(prefSpe1)
    cap = copy.copy(cap1)
    
    #Tas contenant les etudiants libres
    etu_libre = list(range(len(prefEtu)))
    heapq.heapify(etu_libre)
    
    affectation = [None] * len(prefEtu)
    
    #Liste de dictionnaires pour les indices de preferences de spe
    prefSpeIndices = [{etu: idx for idx, etu in enumerate(prefs)} for prefs in prefSpe]
    
    #Liste de tas permettant de recuperer rapidement le pire étudiant
    spe_tas = [[] for i in range(len(prefSpe))]
    
    while etu_libre:#Tant qu'il y  a un etudiant libre
        etu_actuel = heapq.heappop(etu_libre)# on recupere l'etudiant en tete de etu_libre
        list_pref_de_etu = deque(prefEtu[etu_actuel])# ainsi que sa liste de preferences
        
        if list_pref_de_etu:#s'il n'est pas vide
            spe = list_pref_de_etu.popleft()# On recupere la specialite en tete
            
            if cap[spe] > 0:#s'il y a de la place
                #on affecte directement
                affectation[etu_actuel] = spe
                cap[spe] -= 1
                #et on ajoute dans spe_tas 
                heapq.heappush(spe_tas[spe], (-prefSpeIndices[spe][etu_actuel], etu_actuel))
                
            else: #s'il n'y a plus de place
                #On recupere le pire etudiant
                _, last_etu = spe_tas[spe][0]
                #on compare les indices
                if prefSpeIndices[spe][etu_actuel] < prefSpeIndices[spe][last_etu]:
                    #Si l'etu_actuel est prefere
                    heapq.heappop(spe_tas[spe])#on rtire l'etudiant
                    affectation[last_etu] = None
                    affectation[etu_actuel] = spe
                    #on ajoute etu_actuel dans le tas de la spe avec sa priorité 
                    heapq.heappush(spe_tas[spe], (-prefSpeIndices[spe][etu_actuel], etu_actuel))
                    heapq.heappush(etu_libre, last_etu)
                else:#s'il n'est pas prefere on le remets dan etu_libre et met à jour sa liste de preference
                    heapq.heappush(etu_libre, etu_actuel)
                    prefEtu[etu_actuel] = list(list_pref_de_etu)
                    
    return affectation

#Question 4

def algoGS_parcours(prefEtu1,prefSpe1,cap1) :
    prefEtu = copy.copy(prefEtu1)  
    prefSpe = copy.copy(prefSpe1)
    cap = copy.copy(cap1)

    spe_libre = list(range(len(prefSpe)))
    heapq.heapify(spe_libre) #tas pour les étudiants libres
    preferenceSpe = [deque(prefs) for prefs in prefSpe] #liste de deque des preferences
    prefSpeIndices = [{spe : idx for idx,spe in enumerate(prefs)} for prefs in prefEtu] #liste de dictionnaire pour les preferences

    affectation = [None for i in range(len(prefEtu))]

    while(spe_libre) : 
        spe_actuel = heapq.heappop(spe_libre)
        pref_de_spe = preferenceSpe[spe_actuel]

        if(pref_de_spe):
            etu = pref_de_spe.popleft()
            if (affectation[etu] is None):
                cap[spe_actuel] -= 1
                affectation[etu] = spe_actuel

                if(cap[spe_actuel] > 0) :
                    heapq.heappush(spe_libre, spe_actuel)

            else :
                spe_curr = affectation[etu]

                if (prefSpeIndices[etu][spe_actuel] < prefSpeIndices[etu][spe_curr]) :
                    affectation[etu] = spe_actuel
                    cap[spe_curr] += 1
                    cap[spe_actuel] -= 1

                    heapq.heappush(spe_libre, spe_curr)
                    if (cap[spe_actuel] > 0) :
                        heapq.heappush(spe_libre,spe_actuel)

                else :
                    heapq.heappush(spe_libre,spe_actuel)

    return affectation


#Question 6

def paire_instable(affect, prefEtu, prefSpe) :
    prefEtu = copy.deepcopy(prefEtu)  
    prefSpe = copy.deepcopy(prefSpe)
    affect = copy.deepcopy(affect)
    
    list_instable = []
    
    for spe in affect :
        etu_affect = [i for i in range(len(affect)) if affect[i] == spe]
        for etu in etu_affect :#etu affecté à la spe
            spe_pref = prefEtu[etu] #les spe prefs de etu
            ind_spe = spe_pref.index(spe) #le placement de la spe pour etu

            if ind_spe > 0 : #si classé première on passe à la prochaine itération
                spes_meilleures = spe_pref[:ind_spe] #on récupère les spes préférées à celle à laquelle il est affecté
                
                for s in spes_meilleures : #on les parcourt
                    etu_pref = prefSpe[s] #on récupère la liste d'étudiant prefs de s
                    etu_affect2 = [i for i in range(len(affect)) if affect[i] == s] #les etudiants préféré 
                    
                    for e in etu_affect2 : 
                        if etu_pref.index(etu) < etu_pref.index(e) and (s,etu) not in list_instable:
                            list_instable.append((s,etu))
            else : 
                continue
                
    return list_instable

#PARTIE 2
#Question 7
def matrice_CE(n) :
    nbParcours = 9
    matrice = []
    for i in range(n) :
        matrice.append(random.sample(range(0,nbParcours), nbParcours))
        
    return matrice

def matrice_CP(n) :
    nbParcours = 9 
    matrice = []
    for i in range(nbParcours) :
        matrice.append(random.sample(range(0,n),n))
        
    return matrice

