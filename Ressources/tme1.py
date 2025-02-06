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

def algoGS_parcours2(prefEtu, prefSpe, cap):

    spe_libre = [i for i in range(len(prefSpe)) if cap[i] > 0]  # Only add spe with available capacity
    heapq.heapify(spe_libre)
    
    affectation = [None] * len(prefEtu)  # Initialize student assignments

    while spe_libre:
        spe = heapq.heappop(spe_libre)
        pref_de_spe = deque(prefSpe[spe])  # Create a queue from the preference list of the current specialization

        if pref_de_spe:
            etu = pref_de_spe.popleft()  # Pop the first student from the specialization's preference list

            if affectation[etu] is None:  # If the student is not assigned to any specialization
                affectation[etu] = spe
                cap[spe] -= 1  # Decrease the capacity of the specialization

                if cap[spe] > 0:  # If capacity is not exhausted, push back to heap
                    heapq.heappush(spe_libre, spe)

            else:  # If the student is already assigned
                pref_de_etu = prefEtu[etu]  # Get the student's preferences
                spe_curr = affectation[etu]  # Get the student's current specialization

                id_spe = pref_de_etu.index(spe)
                id_spe_curr = pref_de_etu.index(spe_curr)

                if id_spe < id_spe_curr:  # If the student prefers the new specialization more
                    affectation[etu] = spe
                    cap[spe_curr] += 1  # Free up the current specialization's slot
                    cap[spe] -= 1  # Decrease the capacity of the new specialization

                    if cap[spe_curr] > 0:  # If the old specialization still has space, push it back to the heap
                        heapq.heappush(spe_libre, spe_curr)

                    if cap[spe] > 0:  # If the new specialization still has space, push it back to the heap
                        heapq.heappush(spe_libre, spe)

    return affectation

def algoGS3(prefEtu, prefSpe, cap):
    #Tas pour les etudiants libres
    etu_libre = list(range(len(prefEtu)))
    heapq.heapify(etu_libre)
    #Dequifier les matrices
    preferenceEtu = [deque(prefs) for prefs in prefEtu]
    #liste de dictionnaires pour les préférences
    prefEtuIndices = [{etu: idx for idx, etu in enumerate(prefs)} for prefs in prefSpe]
    #liste de tas pour les affectations
    affectation = [[] for i in range(9)]

    while(etu_libre):
        etu_actuel = heapq.heappop(etu_libre)
        list_pref_de_etu = preferenceEtu[etu_actuel]

        if(list_pref_de_etu):
            spe = list_pref_de_etu.popleft() # on récupere la spé préférée dans la liste
            if cap[spe] > 0:
                cap[spe]-=1
                heapq.heappush(affectation[spe], etu_actuel)
            
            else:
                #tas min, le pire doit etre a l'indice 0
                the_worst = affectation[spe][0]
                if prefEtuIndices[spe][etu_actuel] < prefEtuIndices[spe][the_worst]:
                    affectation[spe].remove(the_worst)
                    heapq.heappush(affectation[spe], etu_actuel)

                    # Remettre l'étudiant rejeté dans la liste des libres
                    heapq.heappush(etu_libre, the_worst)
                else:
                    # Remettre l'étudiant actuel dans la liste des libres
                    heapq.heappush(etu_libre, etu_actuel)

    #print(affectation)
    return affectation