class BrazoMecanico:

    def sustituir_pieza(self, carro, pieza):
        print(f"[Brazo mecánico] Retirando {pieza} dañados...")
        print(f"[Brazo mecánico] Instalando {pieza} nuevos...")
        carro.marcar_reparada(pieza)
        print(f"[Brazo mecánico] {pieza.capitalize()} listos.")

    def atender_carro(self, carro):
        piezasNuevas = []
        for pieza in carro.piezas_cambiar():
            self.sustituir_pieza(carro, pieza)
            piezasNuevas.append(pieza)
        return piezasNuevas
