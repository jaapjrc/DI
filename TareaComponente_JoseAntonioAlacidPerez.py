import os
from typing import Optional
import PySide6.QtCore
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QWidget, QLineEdit, QApplication, QMainWindow, QVBoxLayout

class Password(QLineEdit):
    def __init__(self):
        super().__init__()
        rutas = {
            "visible": os.path.join(os.path.dirname (__file__), "visible.png"),
            "hidden": os.path.join(os.path.dirname (__file__), "hidden.png"),
            }
        self.setEchoMode(QLineEdit.Password)
        self.accion = (QAction(QIcon(rutas["visible"]), "", self))
        self.accion.triggered.connect(self.cambiarVisibilidad)
        self.addAction(self.accion)
        
    def cambiarVisibilidad(self):
        rutas = {
            "visible": os.path.join(os.path.dirname (__file__), "visible.png"),
            "hidden": os.path.join(os.path.dirname (__file__), "hidden.png"),
            }
        self.setEchoMode(QLineEdit.Normal)
        self.accion.setIcon(QIcon(rutas["hidden"]))
            
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