"""
Le centre de photocopie facture 0,25 DH  pour les 10 premières photocopies,
0,20 DH les vingt suivantes et
0,10 DH pour plus de vingt.
Ecrire un programme Python qui demande à l’utilisateur de saisir le nombre de photocopies effectuées
et qui affiche la facture correspondante.
"""

nbr_photocopie = int(input("Entrer le nombre de photocopie: "))

def display_amount(a):
    print("vous devez payer: ", a)

if nbr_photocopie <= 10:
    amount = 0.25 * nbr_photocopie
    display_amount(amount)

elif nbr_photocopie > 10 and nbr_photocopie <= 20:
    amount = 0.20 * nbr_photocopie
    display_amount(amount)
else:
    amount = 0.10 * nbr_photocopie
    display_amount(amount)

