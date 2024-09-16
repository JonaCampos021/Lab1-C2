import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

#Creamos la clase MascotasWindow 
class MascotasWindow(QWidget):
    def __init__(self):
        
        super().__init__()
        
        # Configuramos el título de la ventana.
        self.setWindowTitle("Datos de Mascotas")
        
        #Creamos un layout vertical para organizar los widgets en la ventana
        layout = QVBoxLayout()
 
        #Lista para almacenar los campos de entrada para cada mascota
        self.mascotas = []
        
        #Creamos tres bloques de widgets para tres mascotas
        for i in range(1, 4):
            
            #Etiqueta para indicar el número de mascota
            layout.addWidget(QLabel(f"Mascota {i}"))
            
            #Campo de entrada para el nombre de la mascota
            nombre = QLineEdit(self)
            nombre.setPlaceholderText(f"Nombre de la mascota {i}")
            layout.addWidget(nombre)
            
            #Campo de entrada para la raza de la mascota
            raza = QLineEdit(self)
            raza.setPlaceholderText(f"Raza de la mascota {i}")
            layout.addWidget(raza)
            
            #Campo de entrada para la edad de la mascota
            edad = QLineEdit(self)
            edad.setPlaceholderText(f"Edad de la mascota {i}")
            layout.addWidget(edad)
            
            #Añadimos los campos de entrada a la lista de mascotas
            self.mascotas.append((nombre, raza, edad))
 
        #Creamos un botón que al ser presionado muestra los datos ingresados
        self.boton = QPushButton("Mostrar Datos", self)
        
        #Conectamos el evento clic del botón con el método mostrar_datos
        self.boton.clicked.connect(self.mostrar_datos)
        layout.addWidget(self.boton)

        #Establecemos el layout para la ventana
        self.setLayout(layout)

    def mostrar_datos(self):
        #mostramos los datos de cada una de las mascotas
        for idx, (nombre, raza, edad) in enumerate(self.mascotas, start=1):
            
            #Imprimimos en la consola el número de la mascota y los datos ingresados
            print(f"Mascota {idx}:")
            print(f"Nombre: {nombre.text()}")  
            print(f"Raza: {raza.text()}")   
            print(f"Edad: {edad.text()}")   
            print("---")

app = QApplication(sys.argv)
#Cewamos uua instancia de la ventana
ventana = MascotasWindow()
ventana.show()
#Se ejecuta el bucle de eventos de la aplicación
sys.exit(app.exec_())
