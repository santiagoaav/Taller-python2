class Cuenta:

    tarifa = {
        "ruedas": 1500000,
        "parabrisas": 2000000,
        "vidrios": 1000000,
        "espejos": 500000,
    }

    def __init__(self, piezasNuevas):
        self.piezasNuevas = piezasNuevas
        self.totalPago = 0

    def formato_pesos(self, valor):
        return "$" + f"{valor:,}".replace(",", ".")

    def calcular_total(self):
        self.totalPago = 0
        for pieza in self.piezasNuevas:
            self.totalPago += self.tarifa[pieza]
        return self.totalPago

    def imprimir_cuenta(self):
        self.calcular_total()
        print("\n========== CUENTA DE COBRO ==========")
        for pieza in self.piezasNuevas:
            print(f"{pieza.capitalize():<15}{self.formato_pesos(self.tarifa[pieza]):>20}")
        print("-------------------------------------")
        print(f"{'TOTAL':<15}{self.formato_pesos(self.totalPago):>20}")
        print("=====================================\n")
