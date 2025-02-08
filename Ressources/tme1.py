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
    #tas contenant les etudiants libres
    etu_libre = [i for i in range(len(prefEtu))]
    heapq.heapify(etu_libre)  # Tas de priorité pour les étudiants libres

    #initialisation d'affectation
    affectation = [None] * len(prefEtu)
    
    prefEtuIndices = [{etu: idx for idx, etu in enumerate(prefs)} for prefs in prefSpe]#liste de dictionnaires pour les préférences
    prefSpeIndices = [{etu: idx for idx, etu in enumerate(prefs)} for prefs in prefSpe]
    #tant qu'il y a un etudiant libre dans le tas
    while etu_libre:
        #print(affectation)
        etu_actuel = heapq.heappop(etu_libre)#on prend le premier
        list_pref_de_etu = deque(prefEtu[etu_actuel])#on recupere sa liste de preference

        if list_pref_de_etu:#tant qu'il y a encore des spe dans la liste
            spe = list_pref_de_etu.popleft()# on prend la spe en tete

            if cap[spe] > 0:  #si la spe a encore de la place
                affectation[etu_actuel] = spe #on affecte directement
                cap[spe] -= 1 #et on decremente de 1
            else:#sinon
                #on recupere le pire etudiant affecte a la spe
                #last_etu = pire_etudiant1(spe, affectation, list_pref_de_spe)
                last_etu = pire_etudiant1(spe, affectation, prefSpeIndices[spe])
                if last_etu is not None:
                    id_etu_actuel = prefEtuIndices[spe][etu_actuel]
                    id_last_etu = prefEtuIndices[spe][last_etu]

                    if id_etu_actuel < id_last_etu:  # Si l'étudiant actuel est préféré à l'ancien
                        affectation[last_etu] = None
                        affectation[etu_actuel] = spe
                        heapq.heappush(etu_libre, last_etu)  # Le dernier étudiant est à nouveau libre
                    else:
                        heapq.heappush(etu_libre, etu_actuel)
                        prefEtu[etu_actuel] = list(list_pref_de_etu)  # Mise à jour de ses préférences

    return affectation

def pire_etudiant1(spe, affectation, pref_spe_indices):
    # Trouve les étudiants affectés à cette spécialité
    etudiants_affectes = [etu for etu in pref_spe_indices.keys() if affectation[etu] == spe]
    
    if not etudiants_affectes:
        return None

    # Trouve l'étudiant avec le plus mauvais rang
    return max(etudiants_affectes, key=lambda etu: pref_spe_indices[etu])

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
                        if etu_pref.index(etu) < etu_pref.index(e) :
                            print("ajoute")
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

