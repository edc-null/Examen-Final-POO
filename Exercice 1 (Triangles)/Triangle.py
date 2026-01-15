
class Triangle:
    def __init__(self, n, left: bool):
        self.n = n
        self.left = left

    def return_lines(self):



# PLANNING

# Pour bel et bien avoir 2 objets triangles distincts (et non une pyramide),
# je vais créer une méthode qui retourne une liste de strings, et selon la variable
# gauche (true or false), la liste contiendra les strings représentant le triangle
# de gauche ou de droite, et, dans la classe Affichage, je vais append les strings
# ensemble pour former la design final.

#   *  *
#  **  **
# ***  ***