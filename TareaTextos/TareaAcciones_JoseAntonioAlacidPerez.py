import os
import platform
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QDockWidget, QToolBar, QWhatsThis

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de notas 2")
        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Archivo")
        editar = barra_menus.addMenu("&Editar")
        
        ruta_a_icono = os.path.join(os.path.dirname (__file__), "nuevo.png")
        accion = QAction(QIcon(ruta_a_icono), "Nuevo", self)
        accion.setStatusTip("Nuevo")
        accion.setShortcut(QKeySequence("Ctrl+n"))
        accion.triggered.connect(self.nuevo)
        menu.addAction(accion)
        
        ruta_a_icono1 = os.path.join(os.path.dirname (__file__), "abrir.png")
        accion1 = QAction(QIcon(ruta_a_icono1), "Abrir", self)
        accion1.setStatusTip("Abrir")
        accion1.setShortcut(QKeySequence("Ctrl+o"))
        accion1.triggered.connect(self.abrir)
        menu.addAction(accion1)
        
        ruta_a_icono2 = os.path.join(os.path.dirname (__file__), "save_icon.png")
        accion2 = QAction(QIcon(ruta_a_icono2), "Guardar", self)
        accion2.setStatusTip("Guardar")
        accion2.setShortcut(QKeySequence("Ctrl+s"))
        accion2.triggered.connect(self.guardar)
        menu.addAction(accion2)

        ruta_a_icono3 = os.path.join(os.path.dirname (__file__), "undo.png")
        accion3 = QAction(QIcon(ruta_a_icono3), "Deshacer", self)
        accion3.setStatusTip("Deshacer")
        accion3.setShortcut(QKeySequence("Ctrl+q"))
        accion3.triggered.connect(self.deshacer)
        menu.addAction(accion3)

        ruta_a_icono4 = os.path.join(os.path.dirname (__file__), "redo.png")
        accion4 = QAction(QIcon(ruta_a_icono4), "Rehacer", self)
        accion4.setStatusTip("Rehacer")
        accion4.setShortcut(QKeySequence("Ctrl+w"))
        accion4.triggered.connect(self.rehacer)
        menu.addAction(accion4)

        ruta_a_icono5 = os.path.join(os.path.dirname (__file__), "cut.png")
        accion5 = QAction(QIcon(ruta_a_icono5), "Cortar", self)
        accion5.setStatusTip("Cortar")
        accion5.setShortcut(QKeySequence("Ctrl+e"))
        accion5.triggered.connect(self.cortar)
        editar.addAction(accion5)

        ruta_a_icono6 = os.path.join(os.path.dirname (__file__), "copy.png")
        accion6 = QAction(QIcon(ruta_a_icono6), "Copiar", self)
        accion6.setStatusTip("Copiar")
        accion6.setShortcut(QKeySequence("Ctrl+r"))
        accion6.triggered.connect(self.copiar)
        editar.addAction(accion6)

        ruta_a_icono7 = os.path.join(os.path.dirname (__file__), "paste.png")
        accion7 = QAction(QIcon(ruta_a_icono7), "Pegar", self)
        accion7.setStatusTip("Pegar")
        accion7.setShortcut(QKeySequence("Ctrl+t"))
        accion7.triggered.connect(self.pegar)
        editar.addAction(accion7)
        
        barra_herramientas = QToolBar("Barra de herramientas 1")
        barra_herramientas.addAction(accion)
        barra_herramientas.addAction(accion1)
        barra_herramientas.addAction(accion2)
        barra_herramientas.addAction(accion3)
        barra_herramientas.addAction(accion4)
        barra_herramientas.addAction(accion5)
        barra_herramientas.addAction(accion6)
        barra_herramientas.addAction(accion7)
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

    def nuevo(self):
        self.texto_dock.append("Acción Nuevo")
        
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

    def deshacer(self):
        self.texto_dock.append("Acción Deshacer")
        
    def rehacer(self):
        self.texto_dock.append("Acción Rehacer")
        
    def cortar(self):
        self.texto_dock.append("Acción Cortar")
        
    def copiar(self):
        self.texto_dock.copy();
        
    def pegar(self):
        self.texto_dock.append("Acción Pegar")
        
if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()