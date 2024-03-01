import sys

from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtGui

""" Importamos todas nuetras Ventana y funciones utiles"""
from vista.home import  *
from analizador_lexico import *
from analizador_sintactico import *

class Main(QMainWindow):
    """ Clase principal de nuestra app"""
    def __init__(self):
        """ Incializamos nuestra app"""
        QMainWindow.__init__(self)

        # Instaciamos nuestra ventanas widget home
        self.home = Ui_home()
        self.home.setupUi(self)
        
        # Eventos
        self.home.bt_lexico.clicked.connect(self.ev_lexico)
        self.home.bt_sintactico.clicked.connect(self.ev_sintactico)

        #Desarrollandores
        self.home.estado.showMessage("Desarrollando por Julian y Edrei")

    def ev_lexico(self):
        '''
        Manejo de analisis de expresion lexemas
        :return: 
        '''
        # print("lexico")

        # limpiamos el campo
        self.home.tx_lexico.setText('')

        #Obtenemos los datos ingresados
        datos = self.home.tx_ingreso.toPlainText().strip()

        # analizamos la lexemas de los datos ingresados
        resultado_lexico = prueba(datos)

       # self.home.tx_lexico.setText("Analizando lexico")
        cadena= ''
        for lex in resultado_lexico:
            cadena += lex + "\n"
        self.home.tx_lexico.setText(cadena)


    def ev_sintactico(self):
        '''
        Manejo de analisis gramatico
        :return: 
        '''
        # print("sintactico")

        # limpiamos el campo
        self.home.tx_sintactico.setText('')
        #Obtenemos los datos ingresados
        datos = self.home.tx_ingreso.toPlainText().strip()

        #analizamos la gramatica de los datos ingresados
        resultado_sintactico = prueba_sintactica(datos)
        cadena = ''

        #Armanos la cadena a mostrar
        for item in resultado_sintactico:
            cadena += item + "\n"
        # mostramos en pantalla
        self.home.tx_sintactico.setText( cadena )

   

def iniciar():
    # Instaciamos nuestro app por defecto esto no cambia
    app = QApplication(sys.argv)

    # Instaciomos nuestro ventana
    ventana = Main()
    # Mostramos nuestra app
    ventana.show()

    #Controlamos el cierre de la app
    sys.exit(app.exec_())


if __name__ == '__main__':
    iniciar()
