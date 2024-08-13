from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QHBoxLayout,QVBoxLayout,QWidget,QApplication, QLabel, QPushButton,QLineEdit,QCheckBox
from PyQt6.QtGui import QPixmap, QFont
import sys

class Window(QWidget):

  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    
    self.setWindowTitle("My First PyQT window")
    self.setGeometry(0,0,400,150)

    label1=QLabel("Label 1")
    label2=QLabel("Label 2")
    label3=QLabel("Label 3")

    button1= QPushButton("Button 1")
    button2= QPushButton("Button 2")
    button3= QPushButton("Button 3")

    layout= QGridLayout()
    self.setLayout(layout)

    layout.addWidget(label1,0,0)
    layout.addWidget(label2,0,1)
    layout.addWidget(label3,0,2)

    layout.addWidget(button1,1,0)
    layout.addWidget(button2,1,1)
    layout.addWidget(button3,1,2)




app = QApplication(sys.argv)
Window = Window()
Window.show()

sys.exit(app.exec())