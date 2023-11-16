from tkinter import messagebox
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QComboBox, QVBoxLayout, QWidget, QLineEdit, QPushButton

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conversor de Temperaturas")
        layout_vertical = QVBoxLayout()
        componente_principal = QWidget()
        componente_principal.setLayout(layout_vertical)
        self.setCentralWidget(componente_principal)
        self.label = QLabel("Resultado: ",self)
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Celsius")
        self.comboBox.addItem("Fahrenheit")
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("Ingrese temperatura")
        convertir = QPushButton("Convertir")
        layout_vertical.addWidget(self.comboBox)
        layout_vertical.addWidget(self.lineEdit)
        layout_vertical.addWidget(convertir)
        layout_vertical.addWidget(self.label)
        convertir.clicked.connect(self.convertir_temperatura)
        
    
    def convertir_temperatura(self):
        try:
            if self.comboBox.currentText() == "Celsius":
                    resultado = ((float(self.lineEdit.text()) * 9/5) + 32)
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