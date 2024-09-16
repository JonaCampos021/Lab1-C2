import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

#Creamos una clase VentanaPrincipal 
class VentanaPrincipal(QWidget):
    def __init__(self):
        
        #Inicializamos el constructor de la clase 
        super().__init__()
        
        self.setWindowTitle('Ingrese su Clave Secreta')
        
        #Definimos el tamaño y la posición de la ventana 
        self.setGeometry(100, 100, 300, 200)
        
        self.instrucciones_label = QLabel('Ingresa tu clave secreta:', self)
        #Alineamos el texto de la etiqueta al centro
        self.instrucciones_label.setAlignment(Qt.AlignCenter)
        
        #Creamos un campo de entrada QLineEdit para la clave secreta
        self.clave_input = QLineEdit(self)
        
        #Configuramos el modo "Password" para ocultar el texto mientras se escribe
        self.clave_input.setEchoMode(QLineEdit.Password)
        
        #Añadimos un texto de marcador de posición en el campo de entrada
        self.clave_input.setPlaceholderText("Clave secreta")
        
        #Creamos un botón QPushButton con el texto "Mostrar Clave"
        self.boton_mostrar = QPushButton('Mostrar Clave', self)
        
        #Conectamos el evento clic del botón con el método mostrar_clave
        self.boton_mostrar.clicked.connect(self.mostrar_clave)
        
        #Creamos una etiqueta QLabel vacía para mostrar la clave ingresada
        self.resultado_label = QLabel('', self)
        self.resultado_label.setAlignment(Qt.AlignCenter)
        
        #Creamos un layout vertical 
        layout = QVBoxLayout()
        #Añadimos los widgets al layout en orden
        layout.addWidget(self.instrucciones_label)
        layout.addWidget(self.clave_input)
        layout.addWidget(self.boton_mostrar)
        layout.addWidget(self.resultado_label)
       
        #Establecemos el layout en la ventana
        self.setLayout(layout)
    
    def mostrar_clave(self):
        
        #Obtenemos el texto ingresado en el campo de clave
        clave = self.clave_input.text()
        
        #Mostramos la clave ingresada en la etiqueta resultado_label
        self.resultado_label.setText(f'Clave ingresada: {clave}')

if __name__ == '__main__':
    #Inicializamos la aplicación
    app = QApplication(sys.argv)
    #Creamos una instancia de la ventana
    ventana = VentanaPrincipal()
    #Mostramos la ventana
    ventana.show()
    #Se ejecuta el bucle de eventos de la aplicación
    sys.exit(app.exec_())



