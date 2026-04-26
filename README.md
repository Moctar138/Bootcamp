
Structure attendue
gestion-stock/
├── .gitignore├── stock.py        ← fichier principal

└── README.md

Règles Git de l'équipe

main est la branche stable — on n'y code pas directement
Chaque feature = une branche = un membre
On merge uniquement via Pull Request sur GitHub
Un autre membre doit valider la PR avant le merge


Fonctionnalité 0 — Structure de base
Branche : main (commit initial, fait ensemble)
Le chef de projet initialise le fichier stock.py avec :

Une liste vide produits
Un menu() qui affiche les options numérotées
Un main() avec une boucle qui lit le choix et appelle la bonne fonction
Une option 0 pour quitter


Fonctionnalité 1 — Ajouter un produit
Branche : feature/ajout-produit | Membre : dev 1
Entrées :

Nom du produit (string)
Quantité en stock (entier)
Prix unitaire (flottant)

Sorties :

Message de confirmation avec le nom du produit
Le produit apparaît dans la liste avec : nom, quantité, prix

Contraintes :

La quantité ne peut pas être négative
Le prix ne peut pas être nul ou négatif
Si une valeur invalide est saisie : afficher une erreur et redemander


Fonctionnalité 2 — Afficher le stock
Branche : feature/affichage | Membre : dev 2
Entrées :

Aucune

Sorties :

Liste numérotée de tous les produits avec : nom, quantité, prix unitaire
Si le stock est vide : message explicite
En bas : valeur totale du stock (somme de quantité × prix pour chaque produit)

Contraintes :

Si quantité = 0 pour un produit : afficher [RUPTURE] à côté de son nom


Fonctionnalité 3 — Mettre à jour la quantité
Branche : feature/mise-a-jour | Membre : dev 3
Entrées :

Numéro du produit (depuis la liste affichée)
Nouvelle quantité (entier)

Sorties :

Message confirmant la mise à jour avec l'ancienne et la nouvelle quantité
La liste affiche la quantité mise à jour

Contraintes :

Si le numéro saisi n'existe pas : message d'erreur
La nouvelle quantité ne peut pas être négative
Gérer les entrées non numériques avec un try/except
