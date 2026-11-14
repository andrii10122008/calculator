from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox 
from screen_3 import Screen3

class Screen2(QWidget):
    def __init__(self, name, age):
        super().__init__()
        # Принимаем имя и возраст, которые пришли из первого окна
        self.name = name
        self.age = age
        
        self.initUI()
        self.set_win()
        self.set_signals()
        
    def set_win(self):
        self.resize(700, 600)
        self.setWindowTitle("Калькулятор ІМТ - Крок 2")
        
    def initUI(self):
        self.label_weight = QLabel("Введіть вашу вагу (кг):")
        self.in_weight = QLineEdit()
        
        self.label_height = QLabel("Введіть ваш ріст (см):")
        self.in_height = QLineEdit()
        
        self.btn_next = QPushButton("Розрахувати")
        
        # Размещаем всё в вертикальный макет
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_weight)
        self.layout.addWidget(self.in_weight)
        self.layout.addWidget(self.label_height)
        self.layout.addWidget(self.in_height)
        self.layout.addWidget(self.btn_next)
        
        self.setLayout(self.layout)
        
    def set_signals(self):
        # Подключаем кнопку к методу перехода
        self.btn_next.clicked.connect(self.next_screen)
        
    def next_screen(self):
        # Считываем текст из полей
        weight_text = self.in_weight.text()
        height_text = self.in_height.text()
        
        # Проверяем, что введены цифры
        if weight_text.isdigit() and height_text.isdigit():
            self.weight = float(weight_text)
            self.height = float(height_text)
            
            # Открываем третье окно и передаем ВСЕ собранные данные: имя, возраст, вес, рост
            self.sw = Screen3(self.name, self.age, self.weight, self.height)
            self.sw.show()
            self.close()
        else:
            error_msg = QMessageBox(self)
            error_msg.setWindowTitle("Помилка")
            error_msg.setText("Будь ласка, введіть числові значення для ваги та росту.")
            error_msg.setIcon(QMessageBox.Warning)
            error_msg.setStandardButtons(QMessageBox.Ok)
            error_msg.exec_()



