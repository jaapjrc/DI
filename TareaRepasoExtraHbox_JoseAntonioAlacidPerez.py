from tkinter import messagebox
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QMainWindow, QComboBox, QVBoxLayout, QWidget, QLineEdit, QPushButton

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conversor de Temperaturas")
        layout_vertical = QVBoxLayout()
        layout_horizontal = QHBoxLayout()
        componente_principal = QWidget()
        componente_principal.setLayout(layout_vertical)
        self.setCentralWidget(componente_principal)
        self.label = QLabel("Resultado: ",self)
        elementos = ["Celsius", "Fahrenheit"]
        self.comboBox = QComboBox(self)
        self.comboBox.addItems(elementos)
        self.comboBox2 = QComboBox(self)
        self.comboBox2.addItems(elementos)
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("Ingrese temperatura")
        a = QLabel("a", self)
        convertir = QPushButton("Convertir")
        layout_horizontal.addWidget(self.comboBox)
        layout_horizontal.addWidget(a)
        layout_horizontal.addWidget(self.comboBox2)
        layout_vertical.addLayout(layout_horizontal)
        layout_vertical.addWidget(self.lineEdit)
        layout_vertical.addWidget(convertir)
        layout_vertical.addWidget(self.label)
        convertir.clicked.connect(self.convertir_temperatura)
        
    
    def convertir_temperatura(self):
        try:
            if self.comboBox.currentText() == "Celsius":
                if self.comboBox2.currentText() == "Celsius":
                    resultado = float(self.lineEdit.text())
                    self.label.setText(f"Resultado: {resultado:.2f} Celsius")
                else:
                    resultado = ((float(self.lineEdit.text()) * 9/5) + 32)
                    self.label.setText(f"Resultado: {resultado:.2f} Fahrenheit")
            else:
                if self.comboBox2.currentText() == "Fahrenheit":
                    resultado = float(self.lineEdit.text())
                    self.label.setText(f"Resultado: {resultado:.2f} Fahrenheit")
                else:
                    resultado = ((float(self.lineEdit.text()) - 32) * 5/9)
                    self.label.setText(f"Resultado: {resultado:.2f} Celsius")
        except:
            messagebox.showerror("Error", "Introduce un valor númerico")
            
if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()