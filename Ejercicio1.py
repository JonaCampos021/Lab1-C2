import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

#Creamos una clase VentanaPrincipal 
class VentanaPrincipal(QWidget):
    def __init__(self):
        
        #Inicializamos el constructor de la clase 
        super().__init__()
        
        #Configuramos el título de la ventana
        self.setWindowTitle('Nombre y Edad')
        
        #Establecemos el tamaño y la posición inicial de la ventana
        self.setGeometry(100, 100, 300, 200)
        
        #Creamos dos etiquetas QLabel para mostrar el nombre completo y la edad del usuario
        self.nombre_label = QLabel('Nombre Completo: Jorge Gutierres', self)
        self.edad_label = QLabel('Edad: 30 años', self)
        
        #Centramos el texto de ambas etiquetas con el método setAlignment
        self.nombre_label.setAlignment(Qt.AlignCenter)
        self.edad_label.setAlignment(Qt.AlignCenter)
        
        #Creamos un diseño vertical para colocar los widgets en orden vertical
        layout = QVBoxLayout()
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.edad_label)
        
        #Aplicamos el layout a la ventana estableciendo la disposición de los widgets
        self.setLayout(layout)


if __name__ == '__main__':
    #Es el objeto principal de la aplicación que maneja los eventos
    app = QApplication(sys.argv)
    #creamos una instancia de la clase 
    ventana = VentanaPrincipal()
    #muestra la ventana en pantalla
    ventana.show()
    #Se inicia el bucle de eventos de la aplicación 
    sys.exit(app.exec_())

