import math
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QVBoxLayout, QScrollArea, \
    QWidget, QGridLayout, QButtonGroup, QPushButton
from PyQt5 import QtGui
from Cliente import cliente
from ventana3 import Ventana3  # Asegúrate de tener una importación correcta de Ventana3

class Ventana2(QMainWindow):
    def __init__(self, anterior=None):
        super(Ventana2, self).__init__(anterior)

        self.ventanaAnterior = anterior
        self.setWindowTitle("Usuarios Registrados")
        self.setWindowIcon(QtGui.QIcon('imagenes/carro5.jpg'))

        self.ancho = 900
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap('imagenes/carro4.jpg')
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())
        self.setCentralWidget(self.fondo)

        self.horizontal = QHBoxLayout()
        self.vertical = QVBoxLayout()
        self.letrero1 = QLabel()
        self.letrero1.setText("Usuarios Registrados")
        self.letrero1.setFont(QFont("Andale Mono", 20))
        self.letrero1.setStyleSheet("color: #FDFDFD;")
        self.vertical.addWidget(self.letrero1)
        self.vertical.addStretch()

        self.scrollArea = QScrollArea()
        self.scrollArea.setStyleSheet("background-color: transparent;")
        self.scrollArea.setWidgetResizable(True)

        self.contenedora = QWidget()
        self.cuadricula = QGridLayout(self.contenedora)
        self.scrollArea.setWidget(self.contenedora)
        self.vertical.addWidget(self.scrollArea)

        self.file = open('datos/Cliente.txt', 'rb')
        self.usuarios = []
        while True:
            linea = self.file.readline().decode('UTF-8')
            if not linea:
                break

            lista = linea.split(";")
            u = cliente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9],
                lista[10],
            )
            self.usuarios.append(u)

        self.file.close()

        self.numeroUsuarios = len(self.usuarios)
        self.contador = 0
        self.elementosPorColumna = 3
        self.numeroFilas = math.ceil(self.numeroUsuarios / self.elementosPorColumna) + 1
        self.botones = QButtonGroup()
        self.botones.setExclusive(False)

        for fila in range(1, self.numeroFilas):
            for columna in range(1, self.elementosPorColumna + 1):
                if self.contador < self.numeroUsuarios:
                    self.ventanaAuxiliar = QWidget()
                    self.ventanaAuxiliar.setFixedHeight(100)
                    self.ventanaAuxiliar.setFixedWidth(200)
                    self.verticalCuadricula = QVBoxLayout()
                    self.botonAccion = QPushButton(self.usuarios[self.contador].documento)
                    self.botonAccion.setFixedWidth(150)
                    self.botonAccion.setStyleSheet("background-color: #2843F0;"
                                                  "color: #FDFDFD;"
                                                  "padding: 5px;"
                                                  "margin-top: 5px;"
                                                  "font-size: 10px;")
                    self.verticalCuadricula.addWidget(self.botonAccion)

                    try:
                        documento_int = int(self.usuarios[self.contador].documento)
                    except ValueError:
                        documento_int = 0

                    self.botones.addButton(self.botonAccion, documento_int)
                    self.verticalCuadricula.addStretch()
                    self.ventanaAuxiliar.setLayout(self.verticalCuadricula)
                    self.cuadricula.addWidget(self.ventanaAuxiliar, fila, columna)
                    self.contador += 1

        self.botones.buttonClicked[int].connect(self.metodo_accionBotones)

        # Agregar botón "Forma Tabular" encima del botón "Volver"
        self.botonFormaTabular = QPushButton("Forma Tabular")
        self.botonFormaTabular.setFixedWidth(100)
        self.botonFormaTabular.setStyleSheet("background-color: #2843F0;"
                                             "color: #FFFFFF;"
                                             "padding: 5px;"
                                             "margin-top: 5px;"
                                             "font-size: 10px;")
        self.vertical.addWidget(self.botonFormaTabular, alignment=Qt.AlignTop | Qt.AlignLeft)
        self.botonFormaTabular.clicked.connect(self.metodo_botonFormaTabular)  # Conectar con el método correspondiente

        # Agregar botón "Volver" en la parte inferior izquierda
        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(100)
        self.botonVolver.setStyleSheet("background-color: #2843F0;"
                                       "color: #FFFFFF;"
                                       "padding: 5px;"
                                       "margin-top: 5px;"
                                       "font-size: 10px;")
        self.botonVolver.clicked.connect(self.volver_a_ventana_principal)
        self.vertical.addWidget(self.botonVolver, alignment=Qt.AlignBottom | Qt.AlignLeft)

        # Ajustar la posición del área de desplazamiento
        self.scrollArea.verticalScrollBar().setValue(0)

        self.fondo.setLayout(self.vertical)

    def metodo_accionBotones(self, cedulaUsuario):
        print(cedulaUsuario)

    def volver_a_ventana_principal(self):
        self.close()
        if self.ventanaAnterior:
            self.ventanaAnterior.show()

    def metodo_botonFormaTabular(self):
        self.hide()
        self.ventana3 = Ventana3(self)
        self.ventana3.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana2 = Ventana2()
    ventana2.show()
    sys.exit(app.exec_())
