from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from screen_1 import Screen1
import sys

app = QApplication([])
app.setWindowIcon(QIcon("images.png"))

with open("style.css", "r", encoding="utf-8") as file:
    app.setStyleSheet(file.read())

window = Screen1()
window.show()

sys.exit(app.exec_())










