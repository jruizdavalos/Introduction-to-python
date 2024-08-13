from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout,QMessageBox,QMainWindow,QWidget,QApplication, QLabel, QPushButton,QLineEdit,QCheckBox
from PyQt6.QtGui import QPixmap, QFont
import sys

class Window(QWidget):

  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    
    self.setWindowTitle("My First PyQT window")
    self.setGeometry(0,0,400,150)

    label = QLabel("Name")
    name= QLineEdit()
    button= QPushButton("Add")

    layout=QHBoxLayout()
    layout.addWidget(label)
    layout.addWidget(name)
    layout.addWidget(button)

    self.setLayout(layout)

app = QApplication(sys.argv)
Window = Window()
Window.show()

sys.exit(app.exec())