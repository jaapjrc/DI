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
        
        rutas = {
            "nuevo": os.path.join(os.path.dirname (__file__), "nuevo.png"),
            "abrir": os.path.join(os.path.dirname (__file__), "abrir.png"),
            "guardar": os.path.join(os.path.dirname (__file__), "save_icon.png"),
            "undo": os.path.join(os.path.dirname (__file__), "undo.png"),
            "redo": os.path.join(os.path.dirname (__file__), "redo.png"),
            "cortar": os.path.join(os.path.dirname (__file__), "cut.png"),
            "copiar": os.path.join(os.path.dirname (__file__), "copy.png"),
            "pegar": os.path.join(os.path.dirname (__file__), "paste.png"),
            }
        
        accion = QAction(QIcon(rutas["nuevo"]), "Nuevo", self)
        accion.setStatusTip("Nuevo")
        accion.setShortcut(QKeySequence("Ctrl+n"))
        accion.triggered.connect(self.nuevo)
        
        accion1 = QAction(QIcon(rutas["abrir"]), "Abrir", self)
        accion1.setStatusTip("Abrir")
        accion1.setShortcut(QKeySequence("Ctrl+o"))
        accion1.triggered.connect(self.abrir)
        
        accion2 = QAction(QIcon(rutas["guardar"]), "Guardar", self)
        accion2.setStatusTip("Guardar")
        accion2.setShortcut(QKeySequence("Ctrl+s"))
        accion2.triggered.connect(self.guardar)

        accion3 = QAction(QIcon(rutas["undo"]), "Deshacer", self)
        accion3.setStatusTip("Deshacer")
        accion3.setShortcut(QKeySequence("Ctrl+q"))
        accion3.triggered.connect(self.deshacer)

        accion4 = QAction(QIcon(rutas["redo"]), "Rehacer", self)
        accion4.setStatusTip("Rehacer")
        accion4.setShortcut(QKeySequence("Ctrl+w"))
        accion4.triggered.connect(self.rehacer)

        accion5 = QAction(QIcon(rutas["cortar"]), "Cortar", self)
        accion5.setStatusTip("Cortar")
        accion5.setShortcut(QKeySequence("Ctrl+e"))
        accion5.triggered.connect(self.cortar)

        accion6 = QAction(QIcon(rutas["copiar"]), "Copiar", self)
        accion6.setStatusTip("Copiar")
        accion6.setShortcut(QKeySequence("Ctrl+r"))
        accion6.triggered.connect(self.copiar)

        accion7 = QAction(QIcon(rutas["pegar"]), "Pegar", self)
        accion7.setStatusTip("Pegar")
        accion7.setShortcut(QKeySequence("Ctrl+t"))
        accion7.triggered.connect(self.pegar)
        
        menu.addActions([accion, accion1, accion2, accion3, accion4])
        
        editar.addActions([accion5, accion6, accion7])
        
        barra_herramientas = QToolBar("Barra de herramientas 1")
        barra_herramientas.addActions([accion, accion1, accion2, accion3, accion4, accion5, accion6, accion7])
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