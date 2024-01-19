import os
from signal import signal
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon, QPixmap


class Empresa(QWidget):
    double_click = Signal(str)
    def __init__(self, data:str, parent=None):
        super().__init__()
        self.data = data
        layout = QHBoxLayout()
        vertical_layout = QVBoxLayout()
        self.icon = QLabel(self)
        self.icon.setPixmap(QPixmap(self.data["img"]))
        self.icon.setFixedSize(200,200)
        self.nameLabel = QLabel(self.data["name"], self)
        self.addressLabel = QLabel(self.data["address"], self)
        
        
        layout.addWidget(self.icon)
        vertical_layout.addWidget(self.nameLabel)
        vertical_layout.addWidget(self.addressLabel)
        layout.addLayout(vertical_layout)
        self.setLayout(layout)
        
    def mouseDoubleClickEvent(self, e):
        self.double_click.emit(f'{self.data["name"]}, {self.data["address"]}')
        
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.data = {
            "img": os.path.join(os.path.dirname (__file__), "knergil.jpg"),
            "name": "Knergil S.A",
            "address": "Calle Falsa, 1"
            }
        self.empresa = Empresa(self.data)
        self.setLayout(layout)
        layout.addWidget(self.empresa)
        self.setCentralWidget(self.empresa)
        self.empresa.double_click.connect(self.detectEvent)
        
    def detectEvent(self, args):
        print(args)
        
        
        
if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
        
        
        
        




