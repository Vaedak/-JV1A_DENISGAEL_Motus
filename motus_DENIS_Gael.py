import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import random
mots=["cent","cant","cint","eant","tiant"]
mot_choisi=random.choice(mots)
chosen=mot_choisi
comparant=""
essais= 8
parcours_mot_choisi=""
parcours_comparant=""
final_comparant=""
last_round_1=""
last_round_2=""
last_round_3=""
last_round_4=""
last_round_5=""
last_round_6=""
last_round_7=""




##liste de mots 1 ["involve","take","grab","food","sea","night","machine","level","environnement","living"]##
##list de mots 2 "crahs-test" ["cent","cant","cint","eant","tiant"]
##Ce test permet de print et la lettre à l'emplacement i et sa position##
##test = "Cent"
##lettre = ""##
##test_lettre = ""##

##for i in range(len(test)):##
##    lettre = i##
##    test_lettre = test[i]##
##print(lettre)##
##print(test_lettre)##


if essais  != 0 :
    print("Enter a first word . You have 8 tries in total .")
    comparant=input()
    essais = essais-1
    for i in range(len(comparant)):
        parcours_comparant =comparant[i]
        for i in range(len(mot_choisi)):
            parcours_mot_choisi=mot_choisi[i]
            if parcours_mot_choisi == parcours_comparant :
                final_comparant= final_comparant + (Fore.RED + parcours_comparant)
            elif parcours_comparant != parcours_mot_choisi :
                if parcours_comparant in mot_choisi :
                    final_comparant = final_comparant + (Fore.YELLOW + parcours_comparant)
                elif parcours_comparant not in mot_choisi :
                    final_comparant= final_comparant + (Fore.BLUE + parcours_comparant)
else :
    print("You ran out of lifes.")

##fonction de défaite ##

if comparant == mot_choisi:
    print("Victory you found the word !")


##fonction d'affichage des essais précédents##
if essais == 7 :
    print(final_comparant)
elif essais == 6 :
    print(last_round_1)
    print(final_comparant)
elif essais == 5 :
    print(last_round_2)
    print(last_round_1)
    print(final_comparant)
elif essais == 4 :
    print(last_round_3)
    print(last_round_2)
    print(last_round_1)
    print(final_comparant)
elif essais == 3 :
    print(last_round_4)
    print(last_round_3)
    print(last_round_2)
    print(last_round_1)
    print(final_comparant)
elif essais == 2 :
    print(last_round_5)
    print(last_round_4)
    print(last_round_3)
    print(last_round_2)
    print(last_round_1)
    print(final_comparant)
elif essais == 1 :
    print(last_round_6)
    print(last_round_5)
    print(last_round_4)
    print(last_round_3)
    print(last_round_2)
    print(last_round_1)
    print(final_comparant)
elif essais == 0 :
    print(last_round_7)
    print(last_round_6)
    print(last_round_5)
    print(last_round_4)
    print(last_round_3)
    print(last_round_2)
    print(last_round_1)
    print(final_comparant)



##une sauvegarde pour plus tard##
##print(str(Fore.GREEN + parcours_comparant))##
##print(str(Fore.RED + parcours_comparant))##
                
