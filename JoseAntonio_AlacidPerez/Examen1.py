import sys
from PySide6.QtWidgets import (
QApplication, QMainWindow, QWidget, QFormLayout, QVBoxLayout,
QLabel, QLineEdit, QPushButton
)

class VentanaPrincipal(QMainWindow) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de empleados")
        self.setMinimumWidth(300)
        layout_vertical = QVBoxLayout()
        self.layout_labels = QVBoxLayout()
        registrar = QPushButton("Registrar")
        registrar.clicked.connect(self.registrarEmpleado)
        label = QLabel("Empleados Registrados:")
        layout_formulario = QFormLayout()
        componente_principal = QWidget()
        componente_principal.setLayout(layout_vertical)
        layout_vertical.addLayout(layout_formulario)
        self.setCentralWidget(componente_principal)
        self.nombre = QLineEdit()
        layout_formulario.addRow(QLabel("Nombre: "), self.nombre)
        self.edad = QLineEdit()
        layout_formulario.addRow(QLabel("Edad: "), self.edad)
        self.direccion = QLineEdit()
        layout_formulario.addRow(QLabel("Dirección: "), self.direccion)
        self.telefono = QLineEdit()
        layout_formulario.addRow(QLabel("Teléfono: "), self.telefono)
        self.cargo = QLineEdit()
        layout_formulario.addRow(QLabel("Cargo: "), self.cargo)
        self.salario = QLineEdit()
        layout_formulario.addRow(QLabel("Salario: "), self.salario)
        layout_vertical.addWidget(registrar)
        layout_vertical.addWidget(label)
        layout_vertical.addLayout(self.layout_labels)
        
    def registrarEmpleado(self):
        if self.nombre.text() != "" and self.cargo.text() != "" and self.salario.text() != "":
            label = QLabel()
            label.setText(f"{self.nombre.text()} - {self.cargo.text()} - {self.salario.text()}")
            self.layout_labels.addWidget(label)
            self.nombre.clear()
            self.edad.clear()
            self.direccion.clear()
            self.telefono.clear()
            self.cargo.clear()
            self.salario.clear()
        
        
if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()