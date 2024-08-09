from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget,QApplication, QLabel, QPushButton
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
    button = QPushButton(self)
    button.setText("Click here")
    button.move(100,200)
    button.clicked.connect(self.buttonClicked)

    #adding label to display count
    self.label= QLabel(self)
    self.label.setText(f"Number: {self.count}")
    self.label.move(100,150)

  def buttonClicked(self):
    print("Button is clicked")
    self.count+=1
    self.label.setText(f"Number: {str(self.count)}")
    self.label.adjustSize()


app = QApplication(sys.argv)
Window = Window()

Window.show()

sys.exit(app.exec())
