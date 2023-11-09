from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QComboBox

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana")
        self.label = QLabel("Duende",self)
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Duende")
        self.comboBox.addItem("Real")
        self.comboBox.addItem("Video")
        self.comboBox.setFixedSize(70,30)
        self.label.setFixedSize(50,30)
        self.label.move(70,0)
        self.comboBox.activated.connect(self.modificarLabel)
    
    def modificarLabel(self):
        self.label.setText(self.comboBox.currentText())
       

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
    
