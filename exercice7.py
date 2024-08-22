# Écrire un programme Python qui demande deux nombres m et n à l’utilisateur et
# l’informe ensuite si le produit de ces deux nombres est positif ou négatif.*
# On inclut dans le programme le cas où le produit peut être nul.

m = float(input("Entrer m \n"))
n = float(input("Entrer n \n"))
produit = n * m

if produit == 0 :
    print("Le produit est nul")

if produit > 0 :
    print("Le produit est positif")

if produit < 0 :
    print("Le produit est négatif")

