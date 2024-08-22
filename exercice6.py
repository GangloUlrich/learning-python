"""
Écrire un programme Python  qui permet d'évaluer une note saisi au  clavier
(si la note est supérieur à 10 alors il affiche validé sinon non validé  (NB : la note comprise entre 0 et 20 ).
"""

global note_saisie

note_saisie = int(input("Entrer la note d'un apprenant \n"))

while 0 <= note_saisie and note_saisie >= 20 :
    note_saisie = int(input("Entrer une note valide \n"))

if note_saisie > 10 :
     print("Validé")

if note_saisie < 10 :
     print("Non validé")

