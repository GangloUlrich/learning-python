###Écrire un un programme Python qui  permet d'afficher si un nombre  entier saisi au  clavier est pair ou impair.

entrie = input('Saisir un nombre entier:')

a = int(entrie)

if a%2 == 0:
    print(f"{a} est un nombre pair")
else:
    print(f"{a} est un nombre impair")
