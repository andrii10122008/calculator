from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QHBoxLayout





class Screen1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.set_win
        self.set_signals()

    def set_win(self):
        self.resize(700, 600)
        self.setWindowTitle("Калькулятор ІМТ - Крок 1")

    def initUi(self):
        self.btn_next = QPushButton("Далі")

        self.label_name = QLabel("Введіть ваше ім'я:")
        self.in_name = QLineEdit()


        self.label_age = QLabel("Введіть ваш вік:")
        self.in_age = QLineEdit()

    def set_signals(self):
        self.btn_next.clicked.connect(self.next_screen)

    def next_screen(self):
        self.name = self.in_name.text()
        self.age = self.in_age.text()

        if self.name and self.age.isdigit():
            self.close()
        else:
            print("Будь ласка, введіть коректні дані.")

        




 