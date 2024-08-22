"""
Une boutique propose à ces clients, une réduction de 15% pour les montants d’achat supérieurs à 200 dh.
 Écrire un programme Python permettant de saisir le prix total HT et
 de calculer le  montant TTC en prenant en compte la réduction et la TVA=20%.
"""

reduction = lambda a: (a * 15) / 100

tva = lambda a: (a * 20) / 100


def calculate_amount_ht(a):
    amount_ht = a - reduction(a)
    return amount_ht


def calculate_amount_ttc(amount_ht):
    amount_ttc = amount_ht + tva(amount_ht)
    return print("Le montant TTC est", amount_ttc)


amount = float(input("Entrer le montant \n"))

if amount > 200:
    montant_ht = calculate_amount_ht(amount)
    calculate_amount_ttc(montant_ht)
else:
    calculate_amount_ttc(amount)
