import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

#Definimos la clase VentanaPrincipal
class VentanaPrincipal(QWidget):
    def __init__(self):
        
        #Inicializamos el constructor de la clase 
        super().__init__()
        
        self.setWindowTitle('Ingresar Cédula y Nombre')
        
        #Definimos las dimensiones de la ventana
        self.setGeometry(100, 100, 300, 250)
        
        #Creamos las etiquetas que describen los campos a ingresar
        self.cedula_label = QLabel('Numero de Cédula:', self)
        self.nombre_label = QLabel('Nombre Completo:', self)
        
        #Creamos una etiqueta vacía para mostrar los resultados
        self.resultado_label = QLabel('', self)
        
        #Alineamos el texto de la etiqueta de resultado al centro
        self.resultado_label.setAlignment(Qt.AlignCenter)
        
        #Creamos los campos de entrada de texto.
        self.cedula_input = QLineEdit(self)
        self.cedula_input.setPlaceholderText("Numero de cédula")  
        self.nombre_input = QLineEdit(self)
        self.nombre_input.setPlaceholderText("Nombre completo")  
        
        #Creamos un botón que al hacer clic mostrará los datos ingresados
        self.boton_mostrar = QPushButton('Mostrar Datos', self)
        
        #Conectamos el evento clic del botón con el método mostrar_datos
        self.boton_mostrar.clicked.connect(self.mostrar_datos)
        
        #Creamos un layout vertical para organizar los widgets en la ventana.
        layout = QVBoxLayout()
        layout.addWidget(self.cedula_label) 
        layout.addWidget(self.cedula_input) 
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_input)  
        layout.addWidget(self.boton_mostrar)
        layout.addWidget(self.resultado_label)  
        
        #Asignamos el layout a la ventana
        self.setLayout(layout)
    
    def mostrar_datos(self):
        #Obtenemos el texto ingresado en los campos de cédula y nombre
        cedula = self.cedula_input.text()
        nombre = self.nombre_input.text()
        
        #Verificamos si ambos campos tienen datos
        if cedula and nombre:
            #Si los campos están completos mostramos los datos ingresados
            self.resultado_label.setText(f'Cédula: {cedula}\nNombre: {nombre}')
        else:
            #Si falta algún dato mostramos un mensaje 
            self.resultado_label.setText('Por favor, ingresa ambos datos.')

if __name__ == '__main__':
    #Inicializamos la aplicación.
    app = QApplication(sys.argv)
    #Creamos una instancia de la ventana 
    ventana = VentanaPrincipal()
    ventana.show()
    #Se ejecuta el bucle de eventos de la aplicación
    sys.exit(app.exec_())
