import os
import platform
from PySide6 import QtWidgets
from PySide6.QtCore import QFile, QStringConverter, QTextStream, Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QDockWidget, QToolBar, QWhatsThis

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de texto plano")
        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Menu")
        
        ruta_a_icono = os.path.join(os.path.dirname (__file__), "abrir.png")
        accion = QAction(QIcon(ruta_a_icono), "Abrir archivo", self)
        accion.setStatusTip("Abrir archivo")
        accion.setShortcut(QKeySequence("Ctrl+o"))
        accion.triggered.connect(self.abrir)
        menu.addAction(accion)
        
        ruta_a_icono1 = os.path.join(os.path.dirname (__file__), "save_icon.png")
        accion1 = QAction(QIcon(ruta_a_icono1), "Guardar a archivo", self)
        accion1.setStatusTip("Guardar a archivo")
        accion1.setShortcut(QKeySequence("Ctrl+s"))
        accion1.triggered.connect(self.guardar)
        menu.addAction(accion1)
        
        accion2 = QAction("Salir", self)
        accion2.setStatusTip("Salir")
        accion2.setShortcut(QKeySequence("Ctrl+q"))
        accion2.triggered.connect(self.salir)
        menu.addAction(accion2)
        
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

    def abrir(self):
        ruta_a_archivo = os.path.join(os.path.dirname (__file__), "archivo.txt")
        f = open(ruta_a_archivo,"rt")
        data = f.read()
        self.texto_dock.setText(data)
        f.close()
        
        
    def guardar(self):
        ruta_a_archivo = os.path.join(os.path.dirname (__file__), "archivo.txt")
        data = self.texto_dock.toPlainText()
        f = open(ruta_a_archivo, "wt")
        f.write(data)
        f.close()
        
    def salir(self):
        QApplication.quit()
        
        
        

        

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()