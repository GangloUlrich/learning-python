"""
Écrire un programme Python qui permet d'afficher la table de multiplication d’un entier saisie
par l’utilisateur,  Utilisant la boucle for.
"""

n = int(input("Entrer un nombre entier \t"))

for x in range(13):
    print(f"{n} x {x} = ", n*x)
