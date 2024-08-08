from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget,QApplication, QLabel
from PyQt6.QtGui import QPixmap, QFont
import sys

class Window(QWidget):

  def __init__(self):
    super().__init__()

    self.setWindowTitle("My First PyQT window")
    self.setGeometry(0,0,400,400)

    with open('00 - Python exercises/13 - Used PYQT6/car.png'):
      image_label = QLabel(self)
      pixmap = QPixmap('00 - Python exercises/13 - Used PYQT6/car.png')
      image_label.setPixmap(pixmap)
      image_label.move(50,0)

    #Car name
    name_label= QLabel(self)
    name_label.setText("My car")
    name_label.setFont(QFont("Arial",20))
    name_label.move(170,170)

    #Engine specs
    engine_label= QLabel(self)
    engine_label.setText("Engine Capacity: 4L TFSI")
    engine_label.setFont(QFont("Arial",16))
    engine_label.move(20,210)

    #Features
    features_label= QLabel(self)
    features_label.setText("Features: ABS, EBD, ADAS")
    features_label.setFont(QFont("Arial",16))
    features_label.move(20,240)

    #Model of the car
    model_label= QLabel(self)
    model_label.setText("Models: 2.2 Petrol, 1.8 Diesel")
    model_label.setFont(QFont("Arial",16))
    model_label.move(20,270)

    #Price
    price_label= QLabel(self)
    price_label.setText("$80,000")
    price_label.setFont(QFont("Arial",20))
    price_label.move(20,300)


app = QApplication(sys.argv)
Window = Window()

Window.show()

sys.exit(app.exec())

