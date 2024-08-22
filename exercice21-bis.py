"""
Écrire un programme Python qui permet d'afficher la table de multiplication des nombres entiers de 0 à 9
"""

N = 0

while N <= 9:
    for x in range(13):
        print(f"{N} x {x} = ", N*x)
    print("\n")
    N = N + 1

