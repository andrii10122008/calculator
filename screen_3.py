from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from screen_2 import Screen2

class Screen3(QWidget):
    def __init__(self, name, age, weight, height):
        super().__init__()
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        
        self.initUI()
        self.set_win()
        
    def set_win(self):
        self.resize(700, 600)
        self.setWindowTitle("Калькулятор ІМТ - Результат")
        
    def initUI(self):
        height_m = self.height / 100
        self.bmi = self.weight / (height_m ** 2)
        

        if self.bmi < 18.5:
            result_text = "Дефіцит маси тіла (недостатня вага)"
        elif 18.5 <= self.bmi < 25:
            result_text = "Нормальна маса тіла"
        elif 25 <= self.bmi < 30:
            result_text = "Надмірна маса тіла"
        else:
            result_text = "Ожиріння"
            

        self.label_name = QLabel(f"Ім'я: {self.name}")
        self.label_age = QLabel(f"Вік: {self.age} років")
        self.label_bmi = QLabel(f"Ваш індекс маси тіла (ІМТ): {self.bmi:.2f}")
        self.label_result = QLabel(f"Категорія: {result_text}")
        
        self.btn_exit = QPushButton("Вийти")
        
   
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_name)
        self.layout.addWidget(self.label_age)
        self.layout.addWidget(self.label_bmi)
        self.layout.addWidget(self.label_result)
        self.layout.addWidget(self.btn_exit)
        
        self.setLayout(self.layout)
        
 
        self.btn_exit.clicked.connect(self.close)

