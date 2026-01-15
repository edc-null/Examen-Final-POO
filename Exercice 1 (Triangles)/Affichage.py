from Triangle import Triangle

class Affichage:

    def saisie_utilisateur(self):
        # Boucle de saisie qui va s'assurer d'avoir un nombre entier n comme input
        while True:
            try:
                n = int(input("Veuillez saisir un nombre entier: "))
                if n >= 0:
                    return n
                else:
                    print("Erreur: le nombre doit être positif.")
            except ValueError:
                print("Erreur. Veuillez saisir un nombre entier.")


    def print_triangles(self):

        n = self.saisie_utilisateur()

        triangle_gauche = Triangle(n, True)
        triangle_droite = Triangle(n, False)

        lignes_gauche = triangle_gauche.return_lines()
        lignes_droite = triangle_droite.return_lines()

        print() #Skip une ligne
        for i in range(n):
            print(lignes_gauche[i] + "  " + lignes_droite[i])





