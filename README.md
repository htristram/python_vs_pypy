# python_vs_pypy

Un petit comparatif de performances entre Python 3.10.9 et PyPy 7.3.12 qui lui utilise la version 3.10.12 de Python.

La machine de test est plus que modeste : 
- Os de test : Linux Mint 21.1
- CPU : Intel(R) Celeron(R) N5105 @ 2.00GHz
- Mémoire : 16 Go DDR4/2933 MHz
- Disque : M2 SSD - Sata3

# Les objectifs

L'objectif est de réaliser des premiers relevés qui permettront de se faire une idée rapide de pypy si on l'utilise sans aucune optimisation et sur une machine modeste.

On ne cherche pas à savoir si c'est un bon ou un mauvais logiciel, la quesiton n'est pas là, nous cherchons simplement à savoir si il peut être un bon choix dans un contexte d'etl dans lequel nous avons entre 20 et 30 millions d'enregistrements à traiter de façon très régulière.

# Round 1 

## Test avec 500 000 enregistrements
| Actions                                                  |  Python   | Pypy      |
| :------------------------------------------------------- | :-------: | :-------- |
| 500 exécution de la fonction construire_liste_mot(10000) |  41.328   | 5.774     |
| Création du dictionnaire de 500 000  enregistrements.    |   3.156   | 5.123     |
| Création du data frame à partir du dictionnaire          |   0.822   | 7.603     |
| Création du fichier csv                                  |   2.07    | 5.858     |
| Lecture du fichier csv dans un data frame.               |  8.29e-7  | 1.403e-6  |
| Tri sur mot1                                             |   0.979   | 2.995     |
| Tri sur nombre1                                          |   0.297   | 0.333     |
| Tri sur mot1 et mot2                                     |   0.561   | 1.464     |
| Toupper sur mot1                                         |   0.184   | 2.477     |
| **TEMPS TOTAL**                                          | **51.62** | **32.29** |

Le pic de mémoire est de 499Mo en utilisant Python. Celui de pypy est de 1.1Go.

## Test avec 1 000 000 enregistrements
| Actions                                                  |  Python   | Pypy       |
| :------------------------------------------------------- | :-------: | :--------- |
| 500 exécution de la fonction construire_liste_mot(10000) |  40.424   | 5.603      |
| Création du dictionnaire de 500 000  enregistrements.    |   6.36    | 6.895      |
| Création du data frame à partir du dictionnaire          |   1.532   | 13.580     |
| Création du fichier csv                                  |   4.054   | 10.686     |
| Lecture du fichier csv dans un data frame.               |   1.303   | 3.992      |
| Tri sur mot1                                             |   2.419   | 5.559      |
| Tri sur nombre1                                          |   0.881   | 1.384      |
| Tri sur mot1 et mot2                                     |   1.385   | 2.923      |
| Toupper sur mot1                                         |   0.344   | 4.869      |
| **TEMPS TOTAL**                                          | **58.88** | **55.688** |

Le pic de mémoire est de 774Mo en utilisant Python. Celui de pypy est de 1.9Go !!

## Test avec 2 500 000 enregistrements
| Actions                                                  |  Python   | Pypy       |
| :------------------------------------------------------- | :-------: | :--------- |
| 500 exécution de la fonction construire_liste_mot(10000) |  41.535   | 5.909      |
| Création du dictionnaire de 500 000  enregistrements.    |  16.535   | 10.944     |
| Création du data frame à partir du dictionnaire          |   4.01    | 36.231     |
| Création du fichier csv                                  |   10.06   | 28.272     |
| Lecture du fichier csv dans un data frame.               |   3.267   | 9.783      |
| Tri sur mot1                                             |   7.869   | 17.394     |
| Tri sur nombre1                                          |   2.898   | 3.892      |
| Tri sur mot1 et mot2                                     |   4.499   | 5.818      |
| Toupper sur mot1                                         |   0.913   | 12.981     |
| **TEMPS TOTAL**                                          | **91.73** | **131.35** |

Le pic de mémoire est de 1.2Go en utilisant Python. Celui de pypy est de 4.2Go !!

## Test avec 5 000 000 enregistrements
| Actions                                                  |   Python    | Pypy       |
| :------------------------------------------------------- | :---------: | :--------- |
| 500 exécution de la fonction construire_liste_mot(10000) |   40.988    | 5.864      |
| Création du dictionnaire de 500 000  enregistrements.    |   32.487    | 16.412     |
| Création du data frame à partir du dictionnaire          |    8.07     | 72.735     |
| Création du fichier csv                                  |   20.768    | 57.183     |
| Lecture du fichier csv dans un data frame.               |    6.657    | 19.228     |
| Tri sur mot1                                             |   18.339    | 41.562     |
| Tri sur nombre1                                          |    6.227    | 8.556      |
| Tri sur mot1 et mot2                                     |   10.540    | 13.077     |
| Toupper sur mot1                                         |    1.787    | 23.641     |
| **TEMPS TOTAL**                                          | **146.087** | **258.35** |

Le pic de mémoire est de 2.4Go en utilisant Python. Celui de pypy est de 9.1Go !!

## Conclusion du premier round

Avec Python, on multiplie le temps de traitement par 2.84 pour passer de 500 000 à 5 000 000. La consommation mémoire, quant à elle, fait fois 5.

Avec Pypy, le facteur de temps est de 8 et celui de mémoire est de presque 10.

On constate que les performances de PyPy chute plus rapidement que celle de Python.

Pypy est beaucoup plus performant sur les 500 executions de la fonction. Ce qui est normal car cette fonction ne contient que du code Python.
