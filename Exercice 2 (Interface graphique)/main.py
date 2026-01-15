import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout

fichier = "resultats.txt"

def main():
    app = QApplication(sys.argv)

    fen = QWidget()
    #fen.setGeometry(50, 50, 400, 400)

    grid = QGridLayout()
    fen.setLayout(grid)

    # Créer et ajouter les autres widgets

    # Labels
    grid.addWidget(QLabel("Entrer la valeur de N"), 0, 0)
    grid.addWidget(QLabel("Voici le double:"), 1, 0)

    # LineEdit
    entier = QLineEdit()
    double = QLineEdit()
    double.setReadOnly(True)
    grid.addWidget(entier, 0, 1)
    grid.addWidget(double, 1, 1)

    # Boutons
    btn_valider = QPushButton("Valider l'opération")
    grid.addWidget(btn_valider, 2, 1)
    btn_valider.clicked.connect(action_valider)

    btn_sauvegarder = QPushButton("Sauvegarder")
    grid.addWidget(btn_sauvegarder, 3, 1)
    btn_sauvegarder.clicked.connect(action_save)

    btn_charger = QPushButton("Charger")
    grid.addWidget(btn_charger, 3, 0)
    btn_charger.clicked.connect(action_charger)


    fen.show()
    app.exec()
def action_charger():
    pass

def action_save():
    pass

def action_valider():
    pass


if __name__ == "__main__":
    main()





# Planning

# Les widgets/objets dont j'aurai besoin sont une application, une fenêtre, des labels,
# des champs (QLineEdit), etc....

# PAS LE TEMPS DE PLANIFIER!

