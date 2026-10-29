from Carro import Carro
from BrazoMecanico import BrazoMecanico
from Cuenta import Cuenta


class Trabajador:

    piezasRevisar = ["ruedas", "parabrisas", "vidrios", "espejos"]

    def __init__(self):
        self.brazoMaquina = BrazoMecanico()
        self.carroTaller = None

    def preguntar_estado(self, pieza):
        while True:
            respuesta = input(f"Estado de {pieza} (bueno/cambiar): ").strip().lower()
            if respuesta in ("bueno", "cambiar"):
                return respuesta
            print("Opción no válida, escribe 'bueno' o 'cambiar'.")

    def recibir_carro(self):
        print("\n--- Revisión del carro ---")
        estadoPiezas = {}
        for pieza in self.piezasRevisar:
            estadoPiezas[pieza] = self.preguntar_estado(pieza)
        self.carroTaller = Carro(estadoPiezas)

    def procesar_carro(self):
        piezasNuevas = self.brazoMaquina.atender_carro(self.carroTaller)

        if len(piezasNuevas) == 0:
            print("\nEl carro no necesita cambios. No se genera cobro.\n")
        else:
            print("\nEstado final del carro:")
            self.carroTaller.mostrar_estado()
            cuentaGenerada = Cuenta(piezasNuevas)
            cuentaGenerada.imprimir_cuenta()

        self.carroTaller = None

    def iniciar_jornada(self):
        print("=== Taller de vidrios y piezas ===")
        while True:
            print("1. Ingresar carro")
            print("2. Salir")
            opcion = input("Elige una opción: ").strip()

            if opcion == "1":
                self.recibir_carro()
                self.procesar_carro()
            elif opcion == "2":
                print("Jornada terminada.")
                break
            else:
                print("Opción no válida.\n")
