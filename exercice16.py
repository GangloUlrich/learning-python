"""
Écrire un programme Python permettant de  calculer la somme   S=1+2+3+...+ N,  où N saisi par l’utilisateur.  Utilisant la  boucle while.
"""

i = 1
sum = 0

N = int(input("Entrer N: "))


while i <= N:
    sum = sum + i
    i = i + 1

print(f"la somme de 1 à {N}  est: ", sum)