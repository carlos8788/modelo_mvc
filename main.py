from controlador import EstudianteControlador
from modelo import EstudianteModelo
from vista import EstudianteVista

class Main:

    @classmethod
    def main(self):
        self.modelo = EstudianteModelo()
        self.controlador = EstudianteControlador(self.modelo)
        self.vista = EstudianteVista(self.controlador)

        while True:
            print("\n1. Agregar estudiante")
            print("2. Mostrar estudiantes")
            print("3. Salir")
            opcion = int(input("Elige una opción: "))

            if opcion == 1:
                self.vista.agregar_estudiante()
            elif opcion == 2:
                self.vista.mostrar_estudiantes()
            elif opcion == 3:
                break
            else:
                print("Opción no válida. Por favor, vuelve a intentarlo.")

if __name__ == "__main__":
    Main.main()
