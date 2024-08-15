from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QHBoxLayout,QVBoxLayout,QWidget,QApplication, QLabel, QPushButton,QLineEdit,QCheckBox
from PyQt6.QtGui import QPixmap, QFont
import sys

class Window(QWidget):

  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    
    self.setWindowTitle("Calculator")
    
    layout = QGridLayout()
    self.setLayout(layout)

    display = QLabel("0")

    layout.addWidget(display,0,0,1,4)

    buttons=[QPushButton(str(i)) for i in range(10)]

    for i,button in enumerate(buttons):
      row, col = divmod(i,3)
      layout.addWidget(button, row+1,col)
    




app = QApplication(sys.argv)
Window = Window()
Window.show()

sys.exit(app.exec())