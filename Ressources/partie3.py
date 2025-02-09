
def score_de_Borda_etu(prefEtu, prefSpe) :
    
    nbEtu = len(prefEtu)
    nbSpe = len(prefSpe)
    score = []
    
    for etu,pref in enumerate(prefEtu):
        score_etu = {}
        for rang, spe in enumerate(pref) :
            score_etu[spe] = nbSpe - rang-1
            
        score.append(score_etu) 
            
    return score

def score_de_Borda_spe(prefEtu, prefSpe) :
    
    nbEtu = len(prefEtu)
    nbSpe = len(prefSpe)
    score = []
    
    for spe,pref in enumerate(prefSpe):
        score_spe = {}
        for rang, etu in enumerate(pref) :
            score_spe[etu] = nbEtu - rang-1
            
        score.append(score_spe) 
            
    return score



#Question 11
def genere_fichier_lp(nomFichier, k, prefEtu, prefSpe, capacite) :
    #score = score_de_Borda(prefEtu, prefSpe)
    nbEtu = len(prefEtu)
    nbSpe = len(prefSpe)
    nbContraintes =  1
    fichier = open(nomFichier, "w")
    fichier.write("Maximize\n")
    fichier.write("obj :")
    for i in range(nbEtu) :
        pref = prefEtu[i]
        for j in range(k) :
            #fichier.write(str(score[i][j])+" x"+str(i)+"_"+str(pref[j]))
            fichier.write("x"+str(i)+"_"+str(pref[j])) 
            if (i<nbEtu-1 or j<k -1 ): 
                fichier.write(" + ")
            else:
                fichier.write("\n")
                
    fichier.write("Subject To\n")
    for i in range(nbEtu) :
        fichier.write("c"+str(nbContraintes)+": ")
        pref = prefEtu[i]
        for j in range(k) :
            fichier.write("x"+str(i)+"_"+str(pref[j])) 
            if (j<k-1): 
                fichier.write(" + ")
            else:
                fichier.write(" = 1\n")
        nbContraintes += 1
    
    for j in range(nbSpe) :           
        fichier.write("c"+str(nbContraintes)+": ")
        for i in range(nbEtu) :
            fichier.write("x"+str(i)+"_"+str(j)) 
            if(i<nbEtu-1) : 
                fichier.write(" + ")
            else:
                fichier.write(" <= "+str(capacite[j])+"\n")
        nbContraintes += 1
                
    fichier.write("Binary\n")
    for i in range(nbEtu):
        pref = prefEtu[i]
        for j in range(k) : 
            fichier.write("x"+str(i)+"_"+str(pref[j])+" ")
    fichier.write("\n")
    fichier.write("End")
    fichier.close()
    

    
#Question13
        
def genere_fichier_lp_q13(nomFichier, k, prefEtu, prefSpe, capacite) :
    score_etu = score_de_Borda_etu(prefEtu, prefSpe)
    score_spe = score_de_Borda_spe(prefEtu, prefSpe)
    nbEtu = len(prefEtu)
    nbSpe = len(prefSpe)
    nbContraintes =  1
    fichier = open(nomFichier, "w")
    fichier.write("Maximize\n")
    fichier.write("obj : z \n")
    
    fichier.write("Subject To\n")
    for i in range(nbEtu) :
        pref = prefEtu[i]
        fichier.write("c"+str(nbContraintes)+": ")
        for j in range(k) :
            fichier.write(str(score_etu[i][pref[j]])+" x"+str(i)+"_"+str(pref[j]))
            if(j<k-1) :
                fichier.write(" + ")
            else : 
                fichier.write(" -z >= 0 \n")
        nbContraintes += 1
                
    for i in range(nbEtu) :
        pref = prefEtu[i]
        fichier.write("c"+str(nbContraintes)+": ")
        for j in range(k) :
            fichier.write("x"+str(i)+"_"+str(pref[j]))
            if(j<k-1) :
                fichier.write(" + ")
            else : 
                fichier.write(" = 1\n")
        nbContraintes += 1
        
    for j in range(nbSpe) :    
        fichier.write("c"+str(nbContraintes)+": ")
        for i in range(nbEtu) :
            fichier.write("x"+str(i)+"_"+str(j))
            if(i<nbEtu-1) :
                fichier.write(" + ")
            else : 
                fichier.write(" <= " +str(capacite[j])+"\n")
        nbContraintes += 1
        
    fichier.write("Bounds\n")
    fichier.write("0 <= z\n")
        
    fichier.write("Binary\n")
    for i in range(nbEtu):
        pref = prefEtu[i]
        for j in range(nbSpe) : 
            fichier.write("x"+str(i)+"_"+str(j)+" ")
    fichier.write("\n")
    fichier.write("End")
    fichier.close()
            
    
#Question14

def genere_lp_sommeU(nomFichier, prefEtu, prefSpe, capacite) :
    score_etu = score_de_Borda_etu(prefEtu, prefSpe)
    score_spe = score_de_Borda_spe(prefEtu, prefSpe)
    nbEtu = len(prefEtu)
    nbSpe = len(prefSpe)
    nbContraintes =  1
    fichier = open(nomFichier, "w")
    fichier.write("Maximize\n")
    fichier.write("obj :")
    for i in range(nbEtu) :
        for j in range(nbSpe) :
            fichier.write(str(score_etu[i][j])+" x"+str(i)+"_"+str(j))
            #fichier.write("x"+str(i)+"_"+str(pref[j])) 
            fichier.write(" + ")
            
    for j in range(nbSpe) :            
        for i in range(nbEtu) :
            fichier.write(str(score_spe[j][i])+" x"+str(i)+"_"+str(j))
            #fichier.write("x"+str(i)+"_"+str(pref[j])) 
            if (i<nbEtu-1 or j<nbSpe -1 ): 
                fichier.write(" + ")
            else:
                fichier.write("\n")
                
    fichier.write("Subject To\n")
    for i in range(nbEtu) :
        fichier.write("c"+str(nbContraintes)+": ")
        for j in range(nbSpe) :
            fichier.write("x"+str(i)+"_"+str(j)) 
            if (j<nbSpe-1): 
                fichier.write(" + ")
            else:
                fichier.write(" = 1\n")
        nbContraintes += 1
    
    for j in range(nbSpe) :           
        fichier.write("c"+str(nbContraintes)+": ")
        for i in range(nbEtu) :
            fichier.write("x"+str(i)+"_"+str(j)) 
            if(i<nbEtu-1) : 
                fichier.write(" + ")
            else:
                fichier.write(" <= "+str(capacite[j])+"\n")
        nbContraintes += 1
                
    fichier.write("Binary\n")
    for i in range(nbEtu):
        for j in range(nbSpe) : 
            fichier.write("x"+str(i)+"_"+str(j)+" ")
    fichier.write("\n")
    fichier.write("End")
    fichier.close()
    
def genere_lp_q14_umin(nomFichier, prefEtu, prefSpe, capacite) :
    score_etu = score_de_Borda_etu(prefEtu, prefSpe)
    score_spe = score_de_Borda_spe(prefEtu, prefSpe)
    nbEtu = len(prefEtu)
    nbSpe = len(prefSpe)
    nbContraintes =  1
    fichier = open(nomFichier, "w")
    fichier.write("Maximize\n")
    fichier.write("obj : z \n")
    
    fichier.write("Subject To\n")
    for i in range(nbEtu) :
        fichier.write("c"+str(nbContraintes)+": ")
        for j in range(nbSpe) :
            fichier.write(str(score_etu[i][j])+" x"+str(i)+"_"+str(j))
            if(j<nbSpe-1) :
                fichier.write(" + ")
            else : 
                fichier.write(" -z >= 0 \n")
        nbContraintes += 1
        
    for j in range(nbSpe) :  
        fichier.write("c"+str(nbContraintes)+": ")          
        for i in range(nbEtu) :
            fichier.write(str(score_spe[j][i])+" x"+str(i)+"_"+str(j)) 
            if (i<nbEtu-1): 
                fichier.write(" + ")
            else:
                fichier.write(" -z >= 0 \n")
        nbContraintes += 1
                
    for i in range(nbEtu) :
        fichier.write("c"+str(nbContraintes)+": ")
        for j in range(nbSpe) :
            fichier.write("x"+str(i)+"_"+str(j))
            if(j<nbSpe-1) :
                fichier.write(" + ")
            else : 
                fichier.write(" = 1\n")
        nbContraintes += 1
        
    for j in range(nbSpe) :    
        fichier.write("c"+str(nbContraintes)+": ")
        for i in range(nbEtu) :
            fichier.write("x"+str(i)+"_"+str(j))
            if(i<nbEtu-1) :
                fichier.write(" + ")
            else : 
                fichier.write(" <= " +str(capacite[j])+"\n")
        nbContraintes += 1
        
    fichier.write("Bounds\n")
    fichier.write("0 <= z\n")
        
    fichier.write("Binary\n")
    for i in range(nbEtu):
        pref = prefEtu[i]
        for j in range(nbSpe) : 
            fichier.write("x"+str(i)+"_"+str(j)+" ")
    fichier.write("\n")
    fichier.write("End")
    fichier.close()
    

#Question15

def genere_lp_sommeU_k(nomFichier, k, prefEtu, prefSpe, capacite) :
    score_etu = score_de_Borda_etu(prefEtu, prefSpe)
    score_spe = score_de_Borda_spe(prefEtu, prefSpe)
    nbEtu = len(prefEtu)
    nbSpe = len(prefSpe)
    nbContraintes =  1
    fichier = open(nomFichier, "w")
    fichier.write("Maximize\n")
    fichier.write("obj :")
    for i in range(nbEtu) :
        pref = prefEtu[i]
        for j in range(k) :
            fichier.write(str(score_etu[i][pref[j]] + score_spe[pref[j]][i])+" x"+str(i)+"_"+str(pref[j]))  
            if (i<nbEtu-1 or j<k -1 ): 
                fichier.write(" + ")
            else:
                fichier.write("\n")
            
                  
    fichier.write("Subject To\n")
    for i in range(nbEtu) :
        pref = prefEtu[i]
        fichier.write("c"+str(nbContraintes)+": ")
        for j in range(k) :
            fichier.write("x"+str(i)+"_"+str(pref[j])) 
            if (j<k-1): 
                fichier.write(" + ")
            else:
                fichier.write(" = 1\n")
        nbContraintes += 1
    
    for j in range(nbSpe) :           
        fichier.write("c"+str(nbContraintes)+": ")
        for i in range(nbEtu) :
            fichier.write("x"+str(i)+"_"+str(j)) 
            if(i<nbEtu-1) : 
                fichier.write(" + ")
            else:
                fichier.write(" <= "+str(capacite[j])+"\n")
        nbContraintes += 1
                
    fichier.write("Binary\n")
    for i in range(nbEtu):
        for j in range(nbSpe) : 
            fichier.write("x"+str(i)+"_"+str(j)+" ")
    fichier.write("\n")
    fichier.write("End")
    fichier.close()
    
def genere_lp_q15_umin(nomFichier, k, prefEtu, prefSpe, capacite) :
    score_etu = score_de_Borda_etu(prefEtu, prefSpe)
    score_spe = score_de_Borda_spe(prefEtu, prefSpe)
    nbEtu = len(prefEtu)
    nbSpe = len(prefSpe)
    nbContraintes =  1
    fichier = open(nomFichier, "w")
    fichier.write("Maximize\n")
    fichier.write("obj : z\n")
    
    fichier.write("Subject To\n")
    for i in range(nbEtu) :
        pref = prefEtu[i]
        fichier.write("c"+str(nbContraintes)+": ")
        for j in range(k) :
            fichier.write(str(score_etu[i][pref[j]])+" x"+str(i)+"_"+str(pref[j]))  
            if (j<k -1 ): 
                fichier.write(" + ")
            else:
                fichier.write(" -z >= 0\n")
        nbContraintes += 1
    
    for j in range(k) :    
        fichier.write("c"+str(nbContraintes)+": ")
        for i in range(nbEtu) :
            pref = prefEtu[i]
            fichier.write(str(score_spe[j][i])+" x"+str(i)+"_"+str(j))  
            if (i<nbEtu -1 ): 
                fichier.write(" + ")
            else:
                fichier.write(" -z >= 0\n")
        nbContraintes += 1
                          
    for i in range(nbEtu) :
        pref = prefEtu[i]
        fichier.write("c"+str(nbContraintes)+": ")
        for j in range(k) :
            fichier.write("x"+str(i)+"_"+str(pref[j])) 
            if (j<k-1): 
                fichier.write(" + ")
            else:
                fichier.write(" = 1\n")
        nbContraintes += 1
    
    for j in range(nbSpe) :           
        fichier.write("c"+str(nbContraintes)+": ")
        for i in range(nbEtu) :
            fichier.write("x"+str(i)+"_"+str(j)) 
            if(i<nbEtu-1) : 
                fichier.write(" + ")
            else:
                fichier.write(" <= "+str(capacite[j])+"\n")
        nbContraintes += 1
                
    fichier.write("Binary\n")
    for i in range(nbEtu):
        for j in range(nbSpe) : 
            fichier.write("x"+str(i)+"_"+str(j)+" ")
    fichier.write("\n")
    fichier.write("End")
    fichier.close()
    

    