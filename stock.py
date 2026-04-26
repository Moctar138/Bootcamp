
list_produit = []
"""
la liste contient des dictionnaire de produit sous la forme

{
    "nom" : [string],
    "quantite" : [int],
    "prix" : [float]
}

"""

def menu() -> None :
    print("1. Ajouter un produit")
    print("2. Afficher le stock")
    print("3. Mettre à jour la quantité")
    print("4. quitter")

def maj_quantite(numero_produit : int, nouvelle_quantite : int) -> None:
    anciene_quant : int = list_produit[numero_produit]["quantite"]
    list_produit[numero_produit]["quantite"] = nouvelle_quantite
    print(f"la quantite de {list_produit[numero_produit]["nom"]} passe de {anciene_quant} a {list_produit[numero_produit]["quantite"]}")


def main():
    while 1:
        menu()
        user_input = int(input("> "))
        if user_input == 1:
            ajouter_produit()
        elif user_input == 2:
            afficher_stock()
        elif user_input == 3:
            maj_quantite()
        elif user_input == 4:
            exit()
        else :
            print("entrer un choix valide")


main()