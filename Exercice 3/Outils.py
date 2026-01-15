class Outils:
    def __init__(self):
        self.entiers = []

    # Demande à l'utilisateur de saisir 10 entiers un a la suite de l'autre, et les ajoute à une liste
    def saisie(self):
        self.entiers = []
        for i in range(10):
            while True:
                try:
                    entier = int(input("Entrer l'entier #" + str(i+1) + ": "))
                    self.entiers.append(entier)
                    break
                except ValueError:
                    print("Veuillez entrer un entier valide.")

    # Détermine le plus petit des entiers entrés
    def min(self):
        min = self.entiers[0]
        for n in self.entiers:
            if n < min:
                min = n
        return min

    # Détermine le plus grand des entiers entrés
    def max(self):
        max = self.entiers[0]
        for n in self.entiers:
            if n > max:
                max = n
        return max

    # Calcule la somme des entiers entrés
    def somme(self):
        total = 0
        for n in self.entiers:
            total += n
        return total

    # Calcule la moyenne des entiers entrés
    def moyenne(self):
        moy = self.somme() / len(self.entiers)
        return moy

