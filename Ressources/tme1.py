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

def pire_etudiant(spe, affectation, list_pref) : #retourne l'étudiant le moins aimé dans la liste d'affectation du parcours
    # l = liste de preference de le Spe
    # s = spé
    # affectation = liste d'affectation 
    
    etu_affect = (i for i in range(len(affectation)) if affectation[i] == spe)
    
    if not etu_affect : #si vide
        return None
    
    return max(etu_affect, key=lambda etu: list_pref.index(etu))


def algoGS(prefEtu, prefSpe, cap):
    prefEtu = copy.deepcopy(prefEtu)  
    prefSpe = copy.deepcopy(prefSpe)
    cap = copy.deepcopy(cap)
    
    etu_libre = [ i for i in range(len(prefEtu))]
    heapq.heapify(etu_libre)
    affectation = [None for i in range(len(prefEtu))]

    while(etu_libre):
        etu_actuel = heapq.heappop(etu_libre)
        list_pref_de_etu = deque(prefEtu[etu_actuel]) #on prend ses preferences

        if(list_pref_de_etu) : #si la liste n'est pas vide
            spe = list_pref_de_etu.popleft() # on récupere la spé préférée dans la liste

            if(cap[spe] != 0): #si la capacite n'a pas atteint 0
                affectation[etu_actuel] = spe
                cap[spe] -= 1

            else:
                list_pref_de_spe = deque(prefSpe[spe]) #preference de la spe
                last_etu = pire_etudiant(spe,affectation,list_pref_de_spe) #etudiant le moins aimé affecter
                if(last_etu is not None) :
                    id_etu_actuel = list_pref_de_spe.index(etu_actuel) #indice de l'etudiant actuel
                    id_last_etu = list_pref_de_spe.index(last_etu) #indice du pire etudiant

                if(id_etu_actuel < id_last_etu): #on compare
                    affectation[last_etu] = None
                    affectation[etu_actuel] = spe
                    heapq.heappush(etu_libre,last_etu)

                
                else:
                    heapq.heappush(etu_libre, etu_actuel)
                    prefEtu[etu_actuel] = list(list_pref_de_etu)
                
    return affectation


#Question 4

def recupere_cle(dict, valeur) :

    for key in dict.keys() :
        if valeur in dict[key] :  
            return key

    print("N'existe pas")

def algoGS_parcours(prefEtu,prefSpe,cap) :
    prefEtu = copy.deepcopy(prefEtu)  
    prefSpe = copy.deepcopy(prefSpe)
    cap = copy.deepcopy(cap)
    
    spe_libre = [ i for i in range(len(prefSpe))]
    heapq.heapify(spe_libre)
    affectation = [None for i in range(len(prefEtu))]

    while(spe_libre):
        spe = heapq.heappop(spe_libre)
        pref_de_spe = deque(prefSpe[spe])

        if(pref_de_spe) : #si la liste n'est pas vide
            etu = pref_de_spe.popleft() #on prend le premier etudiant de la liste des spé pref
            if affectation[etu] is None : #s'il est libre on l'affecte au parcours
                affectation[etu] = spe
                cap[spe] -= 1 #diminue la capacité

                if(cap[spe] > 0) : #si la capacité n'est pas atteinte on reajoute la spe dans spe_libre
                    heapq.heappush(spe_libre, spe)
                
            else : #si l'etudiant n'est pas libre on doit comparer
                pref_de_etu = prefEtu[etu] #on récupère les préférences de l'étudiant
                spe_curr = affectation[etu]
                
                id_spe = pref_de_etu.index(spe)
                id_spe_curr = pref_de_etu.index(spe_curr)

                if id_spe < id_spe_curr : #on compare les indices
                    affectation[etu] = spe
                    cap[spe_curr] += 1
                    cap[spe] -= 1
                    
                    heapq.heappush(spe_libre,spe_curr)
                    if(cap[spe] > 0) :
                        heapq.heappush(spe_libre,spe)
                
                else :
                    heapq.heappush(spe_libre,spe)
                    prefSpe[spe] = list(pref_de_spe)

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

def algoGS_parcours2(prefEtu,prefSpe,cap) :
    prefEtu = copy.deepcopy(prefEtu)  
    prefSpe = copy.deepcopy(prefSpe)
    cap = copy.deepcopy(cap)

    spe_libre = list(range(len(prefSpe)))
    heapq.heapify(spe_libre) #tas pour les étudiants libres
    preferenceSpe = [deque(prefs) for prefs in prefSpe] #liste de deque des preferences
    prefSpeIndices = [{spe : idx for idx,spe in enumerate(prefs)} for prefs in prefEtu] #liste de dictionnaire pour les preferences

    affectation = [None for i in range(len(prefEtu))]

    while(spe_libre) : 
        #print(affectation)
        spe_actuel = heapq.heappop(spe_libre)
        pref_de_spe = preferenceSpe[spe_actuel]

        if(pref_de_spe):
            etu = pref_de_spe.popleft()
            #print(etu)
            if (affectation[etu] is None):
                cap[spe_actuel] -= 1
                affectation[etu] = spe_actuel

                if(cap[spe_actuel] > 0) :
                    heapq.heappush(spe_libre, spe_actuel)

            else :
                #print(affectation[spe_actuel])
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

def algoGS4(prefEtu, prefSpe, cap):
    prefEtu = copy.deepcopy(prefEtu)  
    prefSpe = copy.deepcopy(prefSpe)
    cap = copy.deepcopy(cap)
    etu_libre = [i for i in range(len(prefEtu))]
    heapq.heapify(etu_libre)  # Tas de priorité pour les étudiants libres
    affectation = [None] * len(prefEtu)
    
    # Pré-calculer les positions des étudiants dans les préférences des spécialités
    # pour accélérer la recherche de l'indice de l'étudiant dans la liste de préférences
    prefEtuIndices = [{etu: idx for idx, etu in enumerate(prefs)} for prefs in prefSpe]#liste de dictionnaires pour les préférences
    while etu_libre:
        etu_actuel = heapq.heappop(etu_libre)  # Etudiant libre à traiter
        list_pref_de_etu = deque(prefEtu[etu_actuel])  # Liste de ses préférences

        if list_pref_de_etu:
            spe = list_pref_de_etu.popleft()  # On prend la spé préférée de l'étudiant

            if cap[spe] > 0:  # Si la spécialité a encore des places disponibles
                affectation[etu_actuel] = spe
                cap[spe] -= 1
            else:
                # Trouver l'étudiant le moins préféré dans la spécialité
                list_pref_de_spe = prefSpe[spe]
                last_etu = pire_etudiant1(spe, affectation, list_pref_de_spe)

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

def pire_etudiant1(spe, affectation, pref_spe):
    # Recherche de l'étudiant avec le plus faible rang dans les préférences de la spécialité
    for etu in pref_spe:
        if affectation[etu] == spe:
            return etu
    return None    