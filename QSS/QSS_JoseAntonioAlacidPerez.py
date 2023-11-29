from PySide6.QtWidgets import QApplication, QLabel, QWidget, QCheckBox

class Ventana(QWidget):
     def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana")
        self.setFixedSize(500,300)
        
        self.checkbox = QCheckBox(self)
        self.checkbox.setStyleSheet(self.StyleSheet())
        
     def StyleSheet(self):
         return """QCheckBox::indicator:unchecked { image: url('2.png');}
        QCheckBox::indicator:checked {
        image: url('1.png');}"""
     
if __name__ == "__main__":
    app = QApplication([])
    ventana1 = Ventana()
    ventana1.show()
    app.exec()
