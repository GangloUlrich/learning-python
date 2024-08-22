"""
Écrire un programme Python permettant d’afficher le mois en lettre selon le numéro saisi au clavier.
 (  Si l’utilisateur tape 1 le programme affiche janvier,  si 2  affiche  février , si 3 affiche mars... )
"""

months = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre",
          "Decembre"]


month = int(input("Entrer le mois de votre choix: "))

while month < 1 or month > 12:
    month = int(input("Entrer le mois de votre choix: "))


print("Le mois demandé est: ", months[month - 1])