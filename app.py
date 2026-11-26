from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
# Стартовое окно приложения, которое запускает первый экран (Screen1) и устанавливает иконку приложения и стили.
from screen_1 import Screen1
import sys
# сооздаем обьект приложения
app = QApplication([])
app.setWindowIcon(QIcon("images.png"))
# Читаем стили из файла style.css и применяем их к приложению
with open("style.css", "r", encoding="utf-8") as file:
    app.setStyleSheet(file.read())
# Создаем и показываем стартовое окно приложения (Screen1)
window = Screen1()
window.show()
# Запускаем цикл обработки событий и завершаем приложение при закрытии окна
sys.exit(app.exec_())










