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
    
    self.current_input="0"

    layout = QGridLayout()
    self.setLayout(layout)

    self.display = QLabel("0")
    self.display.setAlignment(Qt.AlignmentFlag.AlignRight)

    layout.addWidget(self.display,0,0,1,4)

    buttons=[QPushButton(str(i)) for i in range(10)]

    operators = ["+","-","*","/"]
    operator_buttons = [QPushButton(op) for op in operators]
    equals_button= QPushButton("=")
    clear_button= QPushButton("C")

    for i,button in enumerate(buttons):
      if (i==0):
        layout.addWidget(button, 4,1)
      else:
        row, col = divmod(i-1,3)

        layout.addWidget(button, row+1,col)

    # Adding event handling method to buttons
    for button in buttons:
      button.clicked.connect(self.number_button_clicked)
    

    for i, op_button in enumerate(operator_buttons):
      layout.addWidget(op_button,i+1,3)

    layout.addWidget(equals_button,4,2)
    layout.addWidget(clear_button,4,0)


  # Creating a method to handle number buttons clicked
  def number_button_clicked (self):
    digit= self.sender().text()

    if self.current_input=="0":
      self.current_input=digit
    else:
      self.current_input+=digit
    self.display.setText(self.current_input)
    


app = QApplication(sys.argv)
Window = Window()
Window.show()

sys.exit(app.exec())