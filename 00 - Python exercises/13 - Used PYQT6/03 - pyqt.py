from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget,QApplication, QLabel, QPushButton,QLineEdit

from PyQt6.QtGui import QPixmap, QFont
import sys

class Window(QWidget):

  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.count =0
    self.setWindowTitle("My First PyQT window")
    self.setGeometry(0,0,400,400)

    #Creatted button

    name_label=QLabel(self)
    name_label.setText("Enter yout name")
    name_label.move(60,10)

    self.name = QLineEdit(self)
    self.name.resize(200,20)
    self.name.move(60,50)

    button =QPushButton(self)
    button.setText("Add")
    button.move(200,80)
    button.clicked.connect(self.buttonClicked)
    
    self.result_label= QLabel(self)
    self.result_label.setFixedSize(150, 200)
    self.result_label.move(60, 120)


  def buttonClicked(self):
    print("Button clicked")
    print("YOur name is: " + self.name.text())
    self.result_label.setText("YOur name is: " + self.name.text())
    #self.result_label.adjustSize()

app = QApplication(sys.argv)
Window = Window()

Window.show()

sys.exit(app.exec())
