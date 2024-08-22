"""
Écrire un programme Python qui demande l'âge d'un enfant et permet d'informer de sa catégorie sachant que les catégories sont les suivantes:
"poussin de 6 a 7 ans"
"pupille de 8 a 9 ans "
"minime de 10 a 11 ans "
" cadet après 12 ans ".
"""

age = int(input('Entrer votre age \t'))

while age < 6 :
    print("Entrer un age valide, au minimum 6 ans")
    age = int(input('Entrer votre age \t'))


if age == 6 or age == 7:
    print("poussin ")
elif age == 8 or age == 9:
    print("pupille")
elif age == 10 or age == 11:
    print("minime")
else:
    print(" cadet")