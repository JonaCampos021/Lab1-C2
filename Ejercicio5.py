import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

#Creamos la clase PersonaWindow 
class PersonaWindow(QWidget):
    def __init__(self):
        
        #Inicializamos la ventana principal
        super().__init__()
        
        self.setWindowTitle("Datos de una Persona")
        
        #Creamos un layout vertical para organizar los widgets
        layout = QVBoxLayout()
 
        #Definimos una lista de características que se solicitarán al usuario
        caracteristicas_especificas = [
            "Color Favorito", "Habilidades", "Comida Favorita", "Tipo de Música", "Juego Favorito",
            "Altura", "Peso", "Color de Cabello", "Color de Ojos", "Color de Piel"
        ]
 
        #Lista para almacenar los campos de entrada correspondientes a cada característica
        self.caracteristicas = []
        
        #Creamos etiquetas y campos de texto para cada característica
        for i, caracteristica in enumerate(caracteristicas_especificas, start=1):
            
            #Creamos una etiqueta con el nombre de la característica
            label = QLabel(f"{i}. {caracteristica}", self)
            layout.addWidget(label)
            
            #Creamos un campo de entrada para que el usuario ingrese el valor de la característica
            campo = QLineEdit(self)
            campo.setPlaceholderText(f"Ingrese {caracteristica}")
            layout.addWidget(campo)
            
            #Añadimos el campo a la lista de características
            self.caracteristicas.append(campo)
 
        #Creamos un botón para mostrar los datos ingresados
        self.boton = QPushButton("Mostrar Datos", self)
        
        #Conectamos el clic del botón con el método mostrar_datos
        self.boton.clicked.connect(self.mostrar_datos)
        layout.addWidget(self.boton)
 
        #Establecemos el layout para la ventana
        self.setLayout(layout)

    def mostrar_datos(self):
        
        #Definimos las características que se solicitaron al usuario
        caracteristicas_especificas = [
            "Color Favorito", "Habilidades", "Comida Favorita", "Tipo de Música", "Juego Favorito",
            "Altura", "Peso", "Color de Cabello", "Color de Ojos", "Color de Piel"
        ]

        #Recorremos cada campo de entrada y característica y mostramos el resultado en la consola.
        for idx, (campo, nombre) in enumerate(zip(self.caracteristicas, caracteristicas_especificas), start=1):
            print(f"{nombre}: {campo.text()}")  
            
 
app = QApplication(sys.argv)
#Cewamos uua instancia de la ventana
ventana = PersonaWindow()
ventana.show()
#Se ejecuta el bucle de eventos de la aplicación
sys.exit(app.exec_())
