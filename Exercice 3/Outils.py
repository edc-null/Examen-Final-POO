class Outils:
    def __init__(self):
        self.entiers = []

    def saisie(self):
        # Demande à l'utilisateur de saisir 10 entiers un a la suite de l'autre, et les ajoute à une liste
        self.entiers = []
        for i in range(10):
            while True:
                try:
                    entier = int(input("Entrer l'entier #" + str(i+1) + ": "))
                    self.entiers.append(entier)
                    break
                except ValueError:
                    print("Veuillez entrer un entier valide.")

