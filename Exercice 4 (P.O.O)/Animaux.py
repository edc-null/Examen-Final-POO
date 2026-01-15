class Animal:
    def __init__(self, nom):
        self.nom = nom

    def bruit(self):
        print("L'animal fait un bruit.")

class Chien(Animal):
    def bruit(self):
        print(self.nom + "fait WOUF.")

class Chat(Animal):
    def bruit(self):
        print(self.nom + "fait MIAOU.")


animal = Animal("Robert")
chien = Chien("Leopold")
chat = Chat("Sophie")

animal.bruit()
chien.bruit()
chat.bruit()

