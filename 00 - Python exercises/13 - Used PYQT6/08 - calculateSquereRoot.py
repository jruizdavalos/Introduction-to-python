from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox,QMainWindow,QWidget,QApplication, QLabel, QPushButton,QLineEdit,QCheckBox
from PyQt6.QtGui import QPixmap, QFont
import sys, math

class Window(QMainWindow):

  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    
    self.setWindowTitle("My First PyQT window")
    self.setGeometry(0,0,400,150)

    number_label= QLabel("Enter a number: ", self)
    number_label.move(20,20)

    self.number_input= QLineEdit(self)
    self.number_input.move(200,20)

    calculat_button= QPushButton("Find Root", self)
    calculat_button.move(200,60)

    self.result_label= QLabel("Result : ",self)
    self.result_label.move(20,100)

    calculat_button.clicked.connect(self.calculate_square_root)

  def calculate_square_root(self):
    try:
      number= float(self.number_input.text())
      square_root= math.sqrt(number)
      if square_root.is_integer():
        self.result_label.setText(f"Square Root: {square_root}")
      else:
        msg= QMessageBox.warning(self,"Not a perfect square", "The number is not perfect square")
    except ValueError:
      QMessageBox.warning(self,"Invalid input", "Please enter a valid")

app = QApplication(sys.argv)
Window = Window()
Window.show()

sys.exit(app.exec())