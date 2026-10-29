class Carro:

    def __init__(self, estadoPiezas):
        self.estadoPiezas = estadoPiezas

    def piezas_cambiar(self):
        piezasCambio = []
        for pieza, estado in self.estadoPiezas.items():
            if estado == "cambiar":
                piezasCambio.append(pieza)
        return piezasCambio

    def marcar_reparada(self, pieza):
        self.estadoPiezas[pieza] = "bueno"

    def mostrar_estado(self):
        for pieza, estado in self.estadoPiezas.items():
            print(f"   - {pieza}: {estado}")
