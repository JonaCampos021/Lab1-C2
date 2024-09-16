import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QRadioButton, QComboBox, QSpinBox, 
                             QPushButton, QLabel, QMessageBox)

# Clase principal
class Pago_suscripcion(QWidget):
    def _init_(self):
        super()._init_()

        # Nombre de nuestra ventana y configuración de dimensiones
        self.setWindowTitle("Tramite de pago")
        self.setGeometry(100, 100, 300, 300)

        # Ventana principal
        layout = QVBoxLayout()

        # Hacemos uso del widget QRadioButton que consiste en una selección de diferentes opciones 
        self.radio_opcion1 = QRadioButton("Efectivo")
        self.radio_opcion2 = QRadioButton("Tarjeta")

        # Añadimos nuestra caja de opciones a nuestra ventana principal
        layout.addWidget(QLabel("Metodo de pago:"))
        layout.addWidget(self.radio_opcion1)
        layout.addWidget(self.radio_opcion2)

        # Hacemos uso del widget QComboBox que consiste en un menu de opciones
        self.combo = QComboBox()
        self.combo.addItems(["Ahora", "Mañana"])

        # Añadimos nuestro menu de opciones a nuestra ventana principal
        layout.addWidget(QLabel("Fecha de pago:"))
        layout.addWidget(self.combo)

        # Hacemos uso del widget QSpinBox que consiste en el ingreso de datos numericos
        self.spinbox = QSpinBox()
        self.spinbox.setRange(0, 100)  # Rango de 0 a 100

        # Añadimos nuestro widget a nuestra ventana principal
        layout.addWidget(QLabel("De cuantos meses es su suscripción:"))
        layout.addWidget(self.spinbox)

        # Añadimos un botón que mostrará los datos seleccionados 
        self.boton = QPushButton("Mostrar datos seleccionados")
        self.boton.clicked.connect(self.mostrar_seleccion)

        layout.addWidget(self.boton)

        # Añadimos un nuevo layout a nuestra ventana principal
        self.setLayout(layout)

    # Función para mostrar los valores seleccionados
    def mostrar_seleccion(self):
        radio_seleccion = None
        if self.radio_opcion1.isChecked():
            radio_seleccion = "Efectivo"
        elif self.radio_opcion2.isChecked():
            radio_seleccion = "Tarjeta"
        else:
            radio_seleccion = "Ninguna opción seleccionada"

        combo_seleccion = self.combo.currentText()
        spinbox_valor = self.spinbox.value()

        # Mostrar los valores en un cuadro de mensaje
        QMessageBox.information(self, "Selección",
                                f"Metodo de pago: {radio_seleccion}\n"
                                f"Fecha de pago: {combo_seleccion}\n"
                                f"Meses de suscripción: {spinbox_valor}")

# Función principal
def main():
    app = QApplication(sys.argv)
    ventana = Pago_suscripcion()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "_main_":
    main()


#Este codigo nos permite mantener un control de datos seleccionados por el usuario
#en este caso tomamos a bien crear un programa referente a un proceso de tramite de pago
#un pago de suscripción donde el usuario elige su metodo de pago, fecha y tiempo de sucripción
#al final obtenemos todos los datos seleccionados por el usuario.