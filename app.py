from PyQt5.QtWidgets import QApplication
from screen_1 import Screen1
import sys

app = QApplication([])

window = Screen1()
window.show()

sys.exit(app.exec_())










