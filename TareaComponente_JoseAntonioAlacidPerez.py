import os
from typing import Optional
import PySide6.QtCore
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QWidget, QLineEdit, QApplication, QMainWindow, QVBoxLayout

class Password(QLineEdit):
    def __init__(self):
        super().__init__()
        self.rutas = {
            "visible": os.path.join(os.path.dirname (__file__), "visible.png"),
            "hidden": os.path.join(os.path.dirname (__file__), "hidden.png"),
            }
        self.setFixedSize(120,30)
        self.setEchoMode(QLineEdit.Password)
        self.accion = (QAction(QIcon(self.rutas["visible"]), "", self))
        self.accion.triggered.connect(self.cambiarVisibilidad)
        self.addAction(self.accion, QLineEdit.TrailingPosition)
        
    def cambiarVisibilidad(self):
        if self.echoMode()==QLineEdit.Password:
            self.setEchoMode(QLineEdit.Normal)
            self.accion.setIcon(QIcon(self.rutas["hidden"]))
        else:
            self.setEchoMode(QLineEdit.Password)
            self.accion.setIcon(QIcon(self.rutas["visible"]))
            
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.password = Password()
        self.setLayout(layout)
        layout.addWidget(self.password)
        self.setCentralWidget(self.password)
        
            

            
if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()