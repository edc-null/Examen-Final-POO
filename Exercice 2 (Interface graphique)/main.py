import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout

fichier = "resultats.txt"

def main():
    app = QApplication(sys.argv)

    fen = QWidget()
    fen.setGeometry(50, 50, 400, 400)

    grid = QGridLayout()
    fen.setLayout(grid)
    fen.setStyleSheet("background-color:#99ccff;font-family:\"Times New Roman\"")

    # Créer et ajouter les autres widgets

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

