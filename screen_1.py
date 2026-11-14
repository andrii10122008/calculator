from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QHBoxLayout, QMessageBox
from screen_2 import Screen2  

class Screen1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.set_win()
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

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_name)
        self.layout.addWidget(self.in_name)
        self.layout.addWidget(self.label_age)
        self.layout.addWidget(self.in_age)
        self.layout.addWidget(self.btn_next)
        
        self.setLayout(self.layout)

    def set_signals(self):
        self.btn_next.clicked.connect(self.next_screen)

    def next_screen(self):
        self.name = self.in_name.text()
        self.age = self.in_age.text()

        if self.name and self.age.isdigit():
            self.sw = Screen2(self.name, int(self.age))
            self.sw.show()
            self.close()
        else:
            error_msg = QMessageBox(self)
            error_msg.setWindowTitle("Помилка")
            error_msg.setText("Будь ласка, введіть коректні дані.")
            error_msg.setIcon(QMessageBox.Warning)
            error_msg.setStandardButtons(QMessageBox.Ok)
            error_msg.exec_()


        




 