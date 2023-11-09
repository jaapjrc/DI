from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QComboBox, QVBoxLayout, QWidget, QLineEdit, QPushButton

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conversor de Temperaturas")
        layout_vertical = QVBoxLayout()
        componente_principal = QWidget()
        componente_principal.setLayout(layout_vertical)
        self.setCentralWidget(componente_principal)
        self.label = QLabel(self)
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Celsius")
        self.comboBox.addItem("Fahrenheit")
        self.comboBox2 = QComboBox(self)
        self.comboBox2.addItem("Celsius")
        self.comboBox2.addItem("Fahrenheit")
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("Ingrese temperatura")
        a = QLabel("a", self)
        convertir = QPushButton("Convertir")
        layout_vertical.addWidget(self.comboBox)
        layout_vertical.addWidget(a)
        layout_vertical.addWidget(self.comboBox2)
        layout_vertical.addWidget(self.lineEdit)
        layout_vertical.addWidget(convertir)
        layout_vertical.addWidget(self.label)
        convertir.clicked.connect(self.convertir_temperatura)
        
    
    def convertir_temperatura(self):
        if self.comboBox.currentText() == "Celsius":
            if self.comboBox2.currentText == "Celsius":
                self.label.setText(f"Resultado: {self.lineEdit.text} Celsius")
            else:
                resultado = ((float(self.lineEdit.text) * 9/5) + 32)
                self.label.setText(f"Resultado: {resultado} Fahrenheit")
        else:
            if self.comboBox2.currentText == "Fahrenheit":
                self.label.setText(f"Resultado: {self.lineEdit.text} Fahrenheit")
            else:
                resultado = ((float(self.lineEdit.text) - 32) * 5/9)
                self.label.setText(f"Resultado: {resultado} Celsius")

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()