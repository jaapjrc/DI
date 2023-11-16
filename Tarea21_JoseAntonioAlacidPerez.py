import os
import platform
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QDockWidget, QToolBar, QWhatsThis

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana")
        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Menu")
        ruta_a_icono = os.path.join(os.path.dirname (__file__), "print.png")
        
        accion = QAction(QIcon(ruta_a_icono), "Imprimir por dock", self)
        accion.setWhatsThis("Al ejecutar esta acción, se añadirá el texto Acción pulsada en el dock. Se puede lanzar por Menú > Imprimir en dock, con Ctrl + P o haciendo clic en el botón correspondiente de la barra de herramientas")
        accion.setStatusTip("Imprimir por dock")
        accion.setShortcut(QKeySequence("Ctrl+p"))
        accion.triggered.connect(self.imprimir_por_dock)
        
        menu.addAction(accion)
        ruta_a_icono1 = os.path.join(os.path.dirname (__file__), "ayuda.png")
        accion1 = QAction(QIcon(ruta_a_icono1), "¿Qué es esto?", self)
        accion1.setStatusTip("¿Qué es esto?")
        accion1.setShortcut(QKeySequence("F1"))
        accion1.triggered.connect(self.entrar_whatsthis)
        menu.addAction(accion1)
        
        barra_herramientas = QToolBar("Barra de herramientas 1")
        barra_herramientas.addAction(accion)
        barra_herramientas.addAction(accion1)
        barra_herramientas.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(barra_herramientas)
        
        barra_estado = self.statusBar()
        barra_estado.addPermanentWidget(QLabel(platform.system()))
        barra_estado.showMessage("Listo. Esperando acción ...", 3000)

        dock1 = QDockWidget()
        dock1.setWindowTitle("Componente base 1")
        self.texto_dock = QTextEdit("")
        dock1.setWidget(self.texto_dock)
        self.addDockWidget(Qt.TopDockWidgetArea, dock1)
        self.setCentralWidget(QLabel("Componente principal"))

    def imprimir_por_dock(self):
        self.texto_dock.append("Acción Pulsada")
        
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