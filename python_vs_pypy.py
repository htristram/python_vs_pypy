import string
import random
import pandas as pd 
import os, timeit, sys
from time import perf_counter


t_global_start = perf_counter()

nombre_de_mots_dans_liste = 10000
nombre_appels_construire_liste_mot = 500
nom_fichier_csv = "dataframe.csv"

if len(sys.argv)==2:
    nombre_ligne_datamart = int(sys.argv[1])
else:    
    nombre_ligne_datamart = 1000

def construire_liste_mot(nombre_mots_attendus):
    str = string.ascii_lowercase + string.ascii_uppercase
    liste_mots = []
    for m in range(nombre_mots_attendus):
        min = random.randint(3,10)
        max = random.randint(11,25)
        mot = "".join(random.choice(str) for i in range(min, max))
        liste_mots.append(mot)
    return liste_mots

if os.path.exists(nom_fichier_csv):
    os.remove(nom_fichier_csv)

# Petit benchmark de la fonction générant la liste de mot.
# on la lance <nombre_appels_construire_liste_mot> pour avoir une mesure de temps comparable
stmt = "construire_liste_mot("  + str(nombre_de_mots_dans_liste) + ")"
print(nombre_appels_construire_liste_mot, "exécution de la fonction construire_liste_mot(", nombre_de_mots_dans_liste, ")")
tps = timeit.timeit(stmt,  setup="from __main__ import construire_liste_mot", number=nombre_appels_construire_liste_mot)
print("    Temps nécessaire : ", round(tps,3), " secondes" )

# On la lance une fois de plus pour conserver le résultat.
liste_mots = construire_liste_mot(nombre_de_mots_dans_liste)

# Création du dictionnaire qui alimentera le data frame.
print("Création du dictionnaire de ",nombre_ligne_datamart," enregistrements.")
t_build_dict_start = perf_counter()
mot1=[]
mot2=[]
mot3=[]
nombre1=[]
nombre2=[]
nombre3=[]
bool1=[]
bool2=[]
bool3=[]

for i in range(nombre_ligne_datamart):
    mot1.append(random.choice(liste_mots))
    mot2.append(random.choice(liste_mots))
    mot3.append(random.choice(liste_mots))
    nombre1.append(random.randint(1,10000))
    nombre2.append(random.randint(1,10000))
    nombre3.append(random.randint(1,10000))
    bool1.append(random.choice([True,False,None]))
    bool2.append(random.choice([True,False,None]))
    bool3.append(random.choice([True,False,None]))
    
t_build_dict_end = perf_counter()
print("    Temps nécessaire : ", t_build_dict_end - t_build_dict_start)

# On utilise le dictionnaire pour créer le data frame
print("Création du data frame à partir du dictionnaire")
t_start = perf_counter()
dict = {'mot1': mot1, 'mot2': mot2, 'mot3': mot3, 
        'nombre1': nombre1, 'nombre2': nombre2, 'nombre3': nombre3, 
        'bool1': bool1, 'bool2': bool2, 'bool3': bool3 } 

df = pd.DataFrame(dict)
t_finish = perf_counter()
print("    Temps nécessaire : ", t_finish - t_start)
del dict

# Création d'un fichier CSV à partir du data frame 
print("Création du fichier csv")
t_start = perf_counter()
df.to_csv(nom_fichier_csv ,header=True, sep=";", index=False)
t_finish = perf_counter()
print("    Temps nécessaire :", t_finish - t_start)
del df

# On rechargre maintenant ls CSV dans un data frame
print("Lecture du fichier csv dans un data frame")
t_start = perf_counter()
df = pd.read_csv(nom_fichier_csv, header=0, sep=";")
t_finish = perf_counter()
print("    Temps nécessaire :", t_finish - t_start)

# Trie sur mot1
print("tri du datamart sur mot1")
t_start = perf_counter()
df.sort_values(by=['mot1'])
t_finish = perf_counter()
print("    Temps nécessaire :", t_finish - t_start)

# Trie sur nombre1
print("tri du datamart sur nombre1")
t_start = perf_counter()
df.sort_values(by=['nombre1'])
t_finish = perf_counter()
print("    Temps nécessaire :", t_finish - t_start)

# Trie sur mot2 et mot3
print("tri du datamart sur mot2 et mot3")
t_start = perf_counter()
df.sort_values(by=['mot2', 'mot3'])
t_finish = perf_counter()
print("    Temps nécessaire :", t_finish - t_start)

# toupper sur mot1
print("ToUpper sur mot1")
t_start = perf_counter()
df['mot1'] = df['mot1'].str.upper()
t_finish = perf_counter()
print("    Temps nécessaire :", t_finish - t_start)

t_global_end = perf_counter()
print("")
print("Temps total : ", t_global_end - t_global_start)