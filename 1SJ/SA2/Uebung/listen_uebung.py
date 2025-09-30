from operator import index
from string import digits
from traceback import print_tb

schlumpf_daten = """
Name,Alter,Beruf/Eigenschaft
Papa Schlumpf,542,Anführer
Schlumpfine,100,Blumenzüchterin
Schlaubi,150,Wissenschafter
Hefty,120,Sportler
Clumsy,135,Tollpatsch
Gargamel,unknown,Bösewicht
Handy,110,Erfinder
Bäcker,130,Bäcker
Schlafmütz,90,Schläfer
Maler,115,Künstler
Bauer,125,Bauer
Musiker,85,Musiker
Jokey,95,Scherzkeks
Baby Schlumpf,5,Baby
Großmaul,105,Koch
Toulous,75,Koch
"""
def count_smurf(schlumpf_liste):
    return len(schlumpf_liste)




def convert_to_list(csv:str):
    liste = csv.split("\n")
    liste.pop(0) # Leerzeile entfernen
    liste.pop(0) # Überschriften entfernen
    liste.pop(-1) # letztes Element löschen entfernen
    return [elem.split(",") for elem in liste]

schlumpf = convert_to_list(schlumpf_daten)
print(schlumpf)
def count_smurfs(liste:list):
    return max(x for x in range(len(liste)))

print(count_smurfs(schlumpf))

def get_average_age(liste:list):
    alter, anzahl = 0, 0
    for item in liste:
        try:
            alter += int(item[1])
            anzahl += 1
        except ValueError:
            continue
    return round(alter / anzahl)

print(get_average_age(schlumpf))

def unique_jobs(liste:list):
    final_liste =[]
    [final_liste.append(x[2]) for x in liste if x[2] not in final_liste]
    return final_liste

print(unique_jobs(schlumpf))

def find_smurf(name, liste):
    return [x for x in liste if x[0] == name][0]
    # for liste_in_der_liste in liste:
    #     if name == liste_in_der_liste[0]:
    #         return liste[i]
    #
    # return " ".join(*a)



print(find_smurf("Schlaubi", schlumpf))
