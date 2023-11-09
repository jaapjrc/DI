from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QWidget,
    QFormLayout,
    QLabel,
    QLineEdit,
    QSpinBox,
    QDoubleSpinBox,
    QVBoxLayout
)

class VentanaPrincipal(QMainWindow) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout Formulario")
        layout_vertical = QVBoxLayout()
        login = QPushButton("Login")
        login.clicked.connect(self.modificarLabel)
        self.label = QLabel()
        layout_formulario = QFormLayout()
        componente_principal = QWidget()
        componente_principal.setLayout(layout_vertical)
        layout_vertical.addLayout(layout_formulario)
        self.setCentralWidget(componente_principal)
        self.user = QLineEdit()
        self.user.setPlaceholderText("Usuario")
        layout_formulario.addRow(QLabel("Usuario: "), self.user)
        self.password = QLineEdit()
        self.password.setPlaceholderText("Contraseña")
        self.password.setEchoMode(QLineEdit.Password)
        layout_formulario.addRow(QLabel("Contraseña: "), self.password)
        layout_vertical.addWidget(login)
        layout_vertical.addWidget(self.label)
        
        
    def modificarLabel(self):
        if self.user.text() == "admin" and self.password.text() == "admin":
            self.label.setStyleSheet("color:green;")
            self.label.setText("Usuario correcto")
        else:
            self.label.setStyleSheet("color:red;")
            self.label.setText("Usuario incorrecto")

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
