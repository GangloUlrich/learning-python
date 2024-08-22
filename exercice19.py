"""
Écrire un programme Python qui permet de calculer la somme   S=1+2+3+4+….+ N. où N saisi au clavier par l'utilisateur.Utilisant la boucle for.
"""

N = int(input("ENtrer le nombre N: "))

sum = 0
for x in range(1,N):
    sum = sum + x

print("la somme  S=1+2+3+...+ N est égale à", sum)