class Animal:
    def __init__(self, nom, poids):
        self.nom = nom

    def bruit(self):
        print("L'animal fait un bruit.")

class Chien(Animal):
    def bruit(self):
        print(self.nom + "fait WOUF.")

class Chat(Animal):
    def bruit(self):
        print(self.nom + "fait MIAOU.")


