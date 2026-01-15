class Animal:
    def __init__(self, nom):
        self.nom = nom

    def bruit(self):
        print("L'animal fait un bruit.")

class Chien(Animal):
    def bruit(self):
        print(self.nom + " fait WOUF.")

class Chat(Animal):
    def bruit(self):
        print(self.nom + " fait MIAOU.")


animal = Animal("Robert")
chien = Chien("Leopold")
chat = Chat("Sophie")

animal.bruit()
chien.bruit()
chat.bruit()

"""
o	Que veut dire le polymorphisme en python

Le polymorphisme en python fait référence au fait que des objets peuvent utiliser la
même méthode, mais que le résultat peut varier si le "type" d'objet est différent. C'est
plus facile à expliquer avec l'exemple ci-dessus. Un chat et un chien sont tout deux des
animaux. Ils ont certaines propriétés en commun, comme la capacité à faire un bruit.
Par contre, la capacité à faire un bruit peut "prendre PLUSIEURS FORMES" dépendamment de
l'animal (produire un son différent).






"""