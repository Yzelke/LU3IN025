import partie3
import tme1

prefEtu = tme1.lecture_matrice("PrefEtu.txt")
prefSpe = tme1.lecture_matriceSpe("PrefSpe.txt")
capacite = tme1.capacite("PrefSpe.txt")

partie3.genere_fichier_lp("fichier_k.lp", 3, prefEtu, prefSpe, capacite) #question11/12/13
partie3.genere_fichier_lp_q13("q13.lp", 5, prefEtu, prefSpe, capacite) #question13 max utilité min
partie3.genere_lp_sommeU("q14_somme.lp",prefEtu, prefSpe, capacite) #question14 somme
partie3.genere_lp_q14_umin("q14_umin.lp",  prefEtu, prefSpe, capacite) #question14 utilité minimale
partie3.genere_lp_sommeU_k("q15_somme.lp", 5, prefEtu, prefSpe, capacite) #question15
partie3.genere_lp_q15_umin("q15_umin.lp", 5, prefEtu, prefSpe, capacite) #question15 utilté minimale

#Question16
q13 = [5,6,8,7,1,4,2,0,8,3,0]
paire13 = tme1.paire_instable(q13, prefEtu, prefSpe)
print(paire13)

q14 = [8,5,8,6,1,0,7,0,3,2,4]
paire14 = tme1.paire_instable(q14, prefEtu, prefSpe)
print(paire14)

q15 = [8,5,8,6,1,0,7,0,2,3,4]
paire15 = tme1.paire_instable(q15, prefEtu, prefSpe)
print(paire15)
