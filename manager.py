#!/usr/bin/python
#-*- coding: <UTF-8> -*-

#Les salaires sont variables d un employe a l autre et sont payes en argent liquide dans une enveloppe.
#Votre application demandera pour chaque employe (max 10) le nom et le montant du salaire (le salaire doit etre un nombre reel positif et plafonne a 5000 ).
#Une fois toutes les donnees memorisees, votre programme calculera pour chaque employe les nombres de chaque billet et piece (200eu, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.20, 0.10, 0.05, 0.02 et 0.01) necessaires a la liquidation de son salaire.
#Enfin, toutes les donnees et resultats de calculs etant memorises dans des structures adequates (listes, dictionnaires, tuples, etc...), il ne restera plus qu a afficher l ensemble des donnees et resultats de calculs dans un format lisible, pour la plus grande joie de Mr Debrikedbrok, debarrasse de cette tache fastidieuse et repetitive.

#Perdaens Laurent, Ma1 Ba 2018-2019
import os
from math import ceil #juste pour montrer que je sais utiliser

tabValue=[200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

def calcul_billet(nom_employe, salaire_employe):
    tab_billet=[0, 0, 0, 0 , 0 ,0 , 0 ,0 ,0 ,0 ,0 ,0 ,0, 0]
    reste=salaire_employe
    acc=0
    while reste>0 and acc < 14:
        tab_billet[acc] = int( reste // tabValue[acc] )
        reste = reste % tabValue[acc]
        if tab_billet[acc]!=0:
            print( "Il faudra "+str(tab_billet[acc])+" billets de "
                    +str(tabValue[acc])+" pour remunerer "+nom_employe+
                    " dont le salaire est de "+str(salaire_employe))
        acc+=1
    return tab_billet


def total(resultat_total, tableau_temporaire):
    u=0
    while u<len(resultat_total):
        resultat_total[u]+=tableau_temporaire[u]
        u+=1
    return resultat_total

def last(resultat_total):
    x=0
    while x<len(resultat_total):
        if resultat_total[x]!=0:
            print ("Au total, il faudra aller chercher : "+str(resultat_total[x])
            +" billets ou pieces de "+ str(tabValue[x]))
        x+=1

def hasNumber(nom_employe):
    y=len(nom_employe)-1
    while y>0:
        if nom_employe[y].isdigit():
            return 1
        else:
            y-=1
    return 0

def main():
    resultat_total=[0, 0, 0, 0 , 0 ,0 , 0 ,0 ,0 ,0 ,0 ,0 ,0, 0]
    error = 1
    while error == 1:
        nb_employe=input("Bonjour Monsieur Debrikedbrok, combien d'employes "+
        "devez-vous remunerer aujourdhui? : ")
        try:
            nb_employe=int(nb_employe)
            assert nb_employe < 11
            assert nb_employe > 0
            error = 0
        except AssertionError:
            print("Erreur du nombre d employe, min :1 , maximum 10")
            continue
        except ValueError:
            print("Vous n avez pas saisi un nombre")
            continue

    while nb_employe>0:
        nom_employe=input("Saisissez le nom de l employe : ")
        check_name=hasNumber(nom_employe)
        if check_name == 1:
            print("Le nom d un employe ne peut contenir de chiffres")
            continue
        salaire_employe=input("Saisissez le montant de son salaire : ")
        salaire_employe=salaire_employe.replace(',' , '.')
        try:
            salaire_employe=float(salaire_employe)
            assert salaire_employe<5001
            assert salaire_employe>0
        except AssertionError:
            print("Erreur salaire min:0, max:5000")
            continue
        except ValueError:
            print("Vous n avez pas saisi un nombre pour le salaire")
            continue
        tableau_temporaire=[]
        tableau_temporaire=calcul_billet(nom_employe, salaire_employe)
        total(resultat_total, tableau_temporaire)
        nb_employe-=1


    conclusion=last(resultat_total)



if __name__=="__main__":main()
