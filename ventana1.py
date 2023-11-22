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

        self.ladoDerecho = QFormLayout()
        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)
        self.letrero3 = QLabel()
        self.letrero3.setText("Recuperar Contraseña")
        self.letrero3.setFont(QFont("Andale Mono", 20))
        self.letrero3.setStyleSheet("color: #FDFDFD;")
        self.ladoDerecho.addRow(self.letrero3)
        self.horizontal.addLayout(self.ladoDerecho)
        self.letrero4 = QLabel()
        self.letrero4.setFixedWidth(400)
        self.letrero4.setText("Por favor ingrese la infomacion para recuperar"
                              "\nla contraseña. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        self.letrero4.setFont(QFont("Andale Mono", 12))
        self.letrero4.setStyleSheet("color: #FDFDFD; margin-bottom: 40px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #FDFDFD;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        self.ladoDerecho.addRow(self.letrero4)

        self.labelPregunta1 = QLabel("Pregunta de verificacion 1*")
        self.ladoDerecho.addRow(self.labelPregunta1)

        self.Pregunta1 = QLineEdit()
        self.Pregunta1.setFixedWidth(320)



        self.ladoDerecho.addRow(self.Pregunta1)

        self.labelRespuesta1 = QLabel("Respuesta de verificacion 1*")

        self.ladoDerecho.addRow(self.labelRespuesta1)

        self.respuesta1 = QLineEdit()

        self.respuesta1.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta1)








        self.labelPregunta2 = QLabel("Pregunta de verificacion 2*")
        self.ladoDerecho.addRow(self.labelPregunta2)

        self.Pregunta2 = QLineEdit()
        self.Pregunta2.setFixedWidth(320)



        self.ladoDerecho.addRow(self.Pregunta2)

        self.labelRespuesta2 = QLabel("Respuesta de verificacion 2*")

        self.ladoDerecho.addRow(self.labelRespuesta2)

        self.respuesta2 = QLineEdit()

        self.respuesta2.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta2)

        self.labelPregunta3 = QLabel("Pregunta de verificacion 3*")
        self.ladoDerecho.addRow(self.labelPregunta3)

        self.Pregunta3 = QLineEdit()
        self.Pregunta3.setFixedWidth(320)



        self.ladoDerecho.addRow(self.Pregunta3)

        self.labelRespuesta3 = QLabel("Respuesta de verificacion 3*")

        self.ladoDerecho.addRow(self.labelRespuesta3)

        self.respuesta3 = QLineEdit()

        self.respuesta3.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta3)

        self.botonBuscar = QPushButton("Buscar")
        self.botonBuscar.setFixedWidth(90)
        self.botonBuscar.setStyleSheet("background-color: #2843F0;"
                                       "color: #FDFDFD;"
                                       "padding: 10px;"
                                       "margin-top: 40px;")

        self.botonRecuperar = QPushButton("Recuperar")
        self.botonRecuperar.setFixedWidth(90)
        self.botonRecuperar.setStyleSheet("background-color: #2843F0;"
                                       "color: #FDFDFD;"
                                       "padding: 10px;"
                                       "margin-top: 40px;")
        self.ladoDerecho.addRow(self.botonBuscar, self.botonRecuperar)


        self.fondo.setLayout(self.horizontal)

    def accion_botonLimpiar(self):
        self.nombreCompleto.setText('')
        self.usuario.setText('')
        self.contraseña.setText('')
        self.contraseña2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.Pregunta1.setText('')
        self.respuesta1.setText('')
        self.Pregunta2.setText('')
        self.respuesta2.setText('')
        self.Pregunta3.setText('')
        self.respuesta3.setText('')
        

    def accion_botonRegistrar(self):
        self.ventaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        self.ventaDialogo.resize(300, 150)

        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventaDialogo.accepted)
        self.ventaDialogo.setWindowModality(Qt.ApplicationModal)
        self.ventaDialogo.setWindowTitle("Formulario de registro.")


        self.vetical = QVBoxLayout()
        self.mensaje = QLabel("")
        self.mensaje.setStyleSheet("background-color: #2843F0; color: #FFFFFF; padding: 10px;")

        self.vetical.addWidget(self.mensaje)
        self.vetical.addWidget(self.opciones)
        self.ventaDialogo.setLayout(self.vetical)
        self.datosCorrectos = True

        if (
                self.contraseña.text() != self.contraseña2.text()
        ):
            self.datosCorrectos = False
            self.mensaje.setText("Las contraseñas no son iguales")

            self.ventaDialogo.exec_()

        if (
                  self.nombreCompleto.text() == ''
                  or self.usuario.text() == ''
                  or self.contraseña.text() == ''
                  or self.contraseña2.text() == ''
                  or self.documento.text() == ''
                  or self.correo.text() == ''
                  or self.Pregunta1.text() == ''
                  or self.respuesta1.text() == ''
                  or self.Pregunta2.text() == ''
                  or self.respuesta2.text() == ''
                  or self.Pregunta3.text() == ''
                  or self.respuesta3.text() == ''

        ):
            self.datosCorrectos = False
            self.mensaje.setText('Deben ingresar todos los campos')

            self.ventaDialogo.exec_()

        if self.datosCorrectos:

            self.file = open('datos/Cliente.txt', 'ab')

            self.file.write(bytes(self.nombreCompleto.text() + ";"
                                  + self.usuario.text() + ";"
                                  + self.contraseña.text() + ";"
                                  + self.contraseña2.text() + ";"
                                  + self.documento.text() + ";"
                                  + self.correo.text() + ";"
                                  + self.Pregunta1.text() + ";"
                                  + self.respuesta1.text() + ";"
                                  + self.Pregunta2.text() + ";"
                                  + self.respuesta2.text() + ";"
                                  + self.Pregunta3.text() + ";"
                                  + self.respuesta3.text() + "\n",
                                  encoding='UTF-8'))
        self.file.close()
        self.file = open('datos/Cliente.txt', 'rb')
        while self.file:
            linea = self.file.readline().decode('UTF-8')
            print(linea)
            if linea == '':
                break
            self.file.close()











if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana1 = Ventana1()

    ventana1.show()
    sys.exit(app.exec_())