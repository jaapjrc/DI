import os
from signal import signal
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QMainWindow, QScrollArea, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon, QPixmap
from TareaComponente2_JoseAntonioAlacidPerez import Empresa


class Empresas(QScrollArea):
    def __init__(self, empresaList:Empresa, parent=None):
        super().__init__()
        self.widget = QWidget(self)
        layout = QVBoxLayout()
        for i in empresaList:
            layout.addWidget(i)
        self.widget.setLayout(layout)
        self.setWidget(self.widget)
        
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.data = {
            "img": os.path.join(os.path.dirname (__file__), "knergil.jpg"),
            "name": "Knergil S.A",
            "address": "Calle Falsa, 1"
            }
        empresa = Empresa(self.data)
        empresa1 = Empresa(self.data)
        empresa2 = Empresa(self.data)
        empresasList = [empresa, empresa1, empresa2]
        empresas = Empresas(empresasList)
        self.setCentralWidget(empresas)
        
if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()