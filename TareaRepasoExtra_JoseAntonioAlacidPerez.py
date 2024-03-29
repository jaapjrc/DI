﻿from tkinter import messagebox
from PySide6.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QComboBox, QWidget, QLineEdit, QPushButton

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conversor de Temperaturas")
        layout = QGridLayout()
        componente_principal = QWidget()
        componente_principal.setLayout(layout)
        self.setCentralWidget(componente_principal)
        self.label = QLabel("Resultado: ",self)
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
        layout.addWidget(self.comboBox, 0, 0)
        layout.addWidget(a, 0, 1)
        layout.addWidget(self.comboBox2, 0, 2)
        layout.addWidget(self.lineEdit, 1, 0, 1, 3)
        layout.addWidget(convertir, 2, 0, 1, 3)
        layout.addWidget(self.label, 3, 0)
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