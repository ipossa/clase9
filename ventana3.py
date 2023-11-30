import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QScrollArea, QTableWidget, \
    QTableWidgetItem, QPushButton, QApplication
from PyQt5 import QtGui
from Cliente import cliente  # Asegúrate de importar la clase cliente desde el módulo Cliente

class Ventana3(QMainWindow):
    def __init__(self, anterior=None):
        super(Ventana3, self).__init__(anterior)
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
        self.imagenFondo = QPixmap('imagenes/carro6.jpg')
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())
        self.setCentralWidget(self.fondo)

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
        self.vertical = QVBoxLayout()
        self.letrero1 = QLabel()
        self.letrero1.setText("Usuarios Registrados")
        self.letrero1.setFont(QFont("Andale Mono", 20))
        self.letrero1.setStyleSheet("color: #FDFDFD;")
        self.vertical.addWidget(self.letrero1)
        self.vertical.addStretch()

        self.scrollArea = QScrollArea()
        self.scrollArea.setStyleSheet("background-color: #FFFFFF;")
        self.scrollArea.setWidgetResizable(True)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(11)
        self.tabla.setHorizontalHeaderLabels(['Nombre', 'Usuario', 'Contraseña', 'Documento', 'Correo', 'Pregunta1',
                                              'Respuesta1', 'Pregunta2', 'Respuesta2', 'Pregunta3', 'Respuesta3'])

        self.tabla.setRowCount(self.numeroUsuarios)

        for u in self.usuarios:
            self.tabla.setItem(self.contador, 0, QTableWidgetItem(u.nombreCompleto))
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.usuario))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.contraseña))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.documento))
            self.tabla.setItem(self.contador, 4, QTableWidgetItem(u.correo))
            self.tabla.setItem(self.contador, 5, QTableWidgetItem(u.Pregunta1))
            self.tabla.setItem(self.contador, 6, QTableWidgetItem(u.respuesta1))
            self.tabla.setItem(self.contador, 7, QTableWidgetItem(u.Pregunta2))
            self.tabla.setItem(self.contador, 8, QTableWidgetItem(u.respuesta2))
            self.tabla.setItem(self.contador, 9, QTableWidgetItem(u.Pregunta3))
            self.tabla.setItem(self.contador, 10, QTableWidgetItem(u.respuesta3))
            self.contador += 1

        self.scrollArea.setWidget(self.tabla)
        self.vertical.addWidget(self.scrollArea)
        self.vertical.addStretch()

        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(100)
        self.botonVolver.setStyleSheet("background-color: #2843F0;"
                                       "color: #FFFFFF;"
                                       "padding: 5px;"
                                       "margin-top: 5px;"
                                       "font-size: 10px;")
        self.botonVolver.clicked.connect(self.volver_a_ventana_principal)
        self.vertical.addWidget(self.botonVolver, alignment=Qt.AlignBottom | Qt.AlignLeft)

        self.vertical.addWidget(self.botonVolver)

        self.fondo.setLayout(self.vertical)

    def volver_a_ventana_principal(self):
        self.close()
        if self.ventanaAnterior:
            self.ventanaAnterior.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana3 = Ventana3()
    ventana3.show()
    sys.exit(app.exec_())
