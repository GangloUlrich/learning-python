### Écrire un programme Python  qui permet d'afficher le plus grand de trois entiers saisis  au clavier.

entries_1 = int(input("Entrer le premier nombre \n"))
entries_2 = int(input("Entrer le deuxieme nombre \n"))
entries_3 = int(input("Entrer le troisieme nombre \n"))

greater = entries_1

if entries_2 > greater : greater = entries_2

if entries_3 > greater: greater = entries_3

print('Le plus grand nombre est',greater)
    