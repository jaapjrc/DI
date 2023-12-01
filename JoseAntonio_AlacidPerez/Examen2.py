import os
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (
QApplication, QMainWindow, QToolBar, QWhatsThis, QDockWidget, QLabel,
QTextEdit
)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("¿Cual es la asignatura mas importante?")
        self.setMinimumSize(400,400)
        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Asignaturas")
        
        rutas = {
            "libros": os.path.join(os.path.dirname (__file__), "libros.png"),
            "ayuda": os.path.join(os.path.dirname (__file__), "ayuda.png")
            }
        
        accion = QAction(QIcon(rutas["libros"]), "Prioridad de asignaturas \n 2ºDAM", self)
        accion.setWhatsThis("Nos indica cual es la asignatura mas importante de 2ºDAM")
        accion.setShortcut(QKeySequence("Ctrl+p"))
        accion.triggered.connect(self.imprimir_por_dock)
        
        accion1 = QAction(QIcon(rutas["ayuda"]), "Ayuda", self)
        accion1.setWhatsThis("Activamos el modo ayuda")
        accion1.setShortcut(QKeySequence("Shift+F1"))
        accion1.triggered.connect(self.entrar_whatsthis)
        
        menu.addActions([accion,accion1])
        
        barra_herramientas = QToolBar("Barra de herramientas 1")
        barra_herramientas.addActions([accion, accion1])
        barra_herramientas.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(barra_herramientas)
        
        dock1 = QDockWidget()
        dock1.setWindowTitle("El subsconsciente del alumno")
        self.texto_dock = QTextEdit("")
        dock1.setWidget(self.texto_dock)
        self.addDockWidget(Qt.TopDockWidgetArea, dock1)
        
    def imprimir_por_dock(self):
        self.texto_dock.append("La asignatura mas importante de 2ºDAM es Desarrollo de Interfaces")
        
    def entrar_whatsthis(self):
        if (QWhatsThis.inWhatsThisMode()):
            QWhatsThis.leaveWhatsThisMode()
        else:
            QWhatsThis.enterWhatsThisMode()
            
if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()