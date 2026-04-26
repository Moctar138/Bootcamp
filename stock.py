
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