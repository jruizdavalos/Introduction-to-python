from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QHBoxLayout,QVBoxLayout,QWidget,QApplication, QLabel, QPushButton,QLineEdit,QCheckBox
from PyQt6.QtCore import Qt
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
    display.setAlignment(Qt.AlignmentFlag.AlignRight)

    layout.addWidget(display,0,0,1,4)

    buttons=[QPushButton(str(i)) for i in range(10)]

    operators = ["+","-","*","/"]
    operator_buttons = [QPushButton(op) for op in operators]

    for i,button in enumerate(buttons):
      row, col = divmod(i,3)
      layout.addWidget(button, row+1,col)
    

    for i, op_button in enumerate(operator_buttons):
      layout.addWidget(op_button,i+1,3)


app = QApplication(sys.argv)
Window = Window()
Window.show()

sys.exit(app.exec())