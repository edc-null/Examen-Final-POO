
class Triangle:
    def __init__(self, n, left: bool):
        self.n = n
        self.left = left

    def return_lines(self):
        lines = []

        # Je crée deux sortes de caractère, les étoiles et les espaces. Ensuite, pour chaque
        # ligne, dépendamment de si le triangle est celui de gauche ou de droite, je les append
        # dans un ordre inversé. Par exemple, pour la 3ième ligne, si n=5, on a 3 étoiles,
        # et (5-3) espaces. À gauche on append espaces suivi d'étoiles, et l'inverse à droite.

        for i in range(1, self.n + 1):
            etoiles = "*" * i
            espaces = " " * (self.n - i)

            if self.left:
                lines.append(espaces + etoiles)
            else:
                lines.append(etoiles + espaces)

        return lines




# PLANNING

# Pour bel et bien avoir 2 objets triangles distincts (et non une pyramide),
# je vais créer une méthode qui retourne une liste de strings, et selon la variable
# gauche (true or false), la liste contiendra les strings représentant le triangle
# de gauche ou de droite, et, dans la classe Affichage, je vais append les strings
# ensemble pour former la design final.

#   *  *
#  **  **
# ***  ***