from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana")
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Enero")
        self.comboBox.addItem("Febrero")
        self.comboBox.addItem("Marzo")
        self.comboBox.addItem("Abril")
        self.comboBox.addItem("Mayo")
        self.comboBox.addItem("Junio")
        self.comboBox.addItem("Julio")
        self.comboBox.addItem("Agosto")
        self.comboBox.addItem("Septiembre")
        self.comboBox.addItem("Octubre")
        self.comboBox.addItem("Noviembre")
        self.comboBox.addItem("Diciembre")
        self.comboBox.setFixedSize(100,30)
        self.comboBox.activated.connect(self.imprimir)
    
    def imprimir(self):
        print(f'{self.comboBox.currentText()} es el mes número {self.comboBox.currentIndex() + 1}')
       

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
