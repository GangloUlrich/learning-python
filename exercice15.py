"""
Écrire un programme Python permettant de calculer la somme S= 1+2+3+...+ 10. Utilisant la boucle while.
"""

i = 1
sum = 0

while i<=10:
    sum = sum + i
    i = i + 1

print("la somme de 1 à 10 est: ", sum)