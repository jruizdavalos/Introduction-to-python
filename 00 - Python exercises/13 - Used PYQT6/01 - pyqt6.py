from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget,QApplication

class Window(QWidget):

  def __init__(self):
    super().__init__()

    self.setWindowTitle("My First PyQT window")
    self.setGeometry(0,0,400,300)

app = QApplication(sys.argv)
Window = Window()

Window.show()