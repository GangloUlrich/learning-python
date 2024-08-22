"""
Écrire un programme Python qui permet de  calculer  la somme  S=1+2+3+...+ 10. Utilisant la boucle for.
"""

sum = 0
for x in range(1,11):
    sum = sum + x

print("la somme  S=1+2+3+...+ 10 est égale à", sum)