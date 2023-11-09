from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QLineEdit

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana")
        self.label = QLabel(self)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setMaxLength(5)
        self.lineEdit.setFixedSize(50,30)
        self.label.setFixedSize(50,30)
        self.label.move(50,0)
        self.lineEdit.textChanged.connect(self.modificarLabel)
    
    def modificarLabel(self):
        self.label.setText(self.lineEdit.text())
       

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
    



