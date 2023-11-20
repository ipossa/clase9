import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QApplication, QHBoxLayout, QFormLayout, QLineEdit, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout
from PyQt5 import QtGui, QtCore

class Ventana1(QMainWindow):

    def __init__(self,parent=None):
        super(Ventana1,self).__init__(parent)

        self.setWindowTitle("Formulario de resgistro")
        self.setWindowIcon(QtGui.QIcon('imagenes/carro2.jpg'))

        self.ancho = 900

        self. alto = 600

        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()

        self.centro = QDesktopWidget().availableGeometry().center()

        self.pantalla.moveCenter(self.centro)

        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)

        self.setFixedHeight(self.alto)
        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap('imagenes/carro3.jpg')
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())
        self.setCentralWidget(self.fondo)
        self.horizontal = QHBoxLayout()
        self.horizontal.setContentsMargins(30,30,30,30)
        self.ladoIzquierdo = QFormLayout()
        self.letrero1 = QLabel()
        self.letrero1.setText("Informacion del cliente")

        self.letrero1.setFont(QFont("Andale Mono",20))
        self.letrero1.setStyleSheet("color: #FDFDFD;")
        self.ladoIzquierdo.addRow(self.letrero1)

        self.letrero2 = QLabel()

        self.letrero2.setFixedWidth(340)

        self.letrero2.setText("Por favor ingrese la informacion del cliente"
                              "\nen el formulario de abajo los campos marcados"
                              "\ncon arterisco son obligatorios.")

        self.letrero2.setFont(QFont("Andale Mono", 12))

        self.letrero2.setStyleSheet("color: #FDFDFD; margin-bottom: 40px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #FDFDFD;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        self.ladoIzquierdo.addRow(self.letrero2)
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Nombre Completo*", self.nombreCompleto)
        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)
        self.ladoIzquierdo.addRow("Usuario*", self.usuario)
        self.contraseña = QLineEdit()
        self.contraseña.setFixedWidth(250)
        self.contraseña.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("Contraseña*", self.contraseña)

        self.contraseña2 = QLineEdit()
        self.contraseña2.setFixedWidth(250)
        self.contraseña2.setEchoMode(QLineEdit.Password)
        self.ladoIzquierdo.addRow("Contraseña*", self.contraseña2)
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)
        self.ladoIzquierdo.addRow("Correo*",self.correo)

        self.botonRegistrar = QPushButton("Registrar")

        self.botonRegistrar.setFixedWidth(90)


        self.botonRegistrar.setStyleSheet("background-color: #2843F0;"
                                          "color: #FDFDFD;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        self.botonLimpiar = QPushButton("Limpiar")

        self.botonLimpiar.setFixedWidth(90)

        self.botonLimpiar.setStyleSheet("background-color: #2843F0;"
                                          "color: #FDFDFD;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)


        self.horizontal.addLayout(self.ladoIzquierdo)
        self.fondo.setLayout(self.horizontal)

    def accion_botonLimpiar(self):
        pass
    def accion_botonRegistrar(self):
        pass









        self.fondo.setLayout(self.horizontal)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana1 = Ventana1()

    ventana1.show()
    sys.exit(app.exec_())