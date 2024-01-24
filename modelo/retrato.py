# retrato.py


class Retrato:
    def __init__(
        self,
        material: str,
        costo_materiales: float,
        superficie: str,
        costo_hora: float,
        horas_estimadas: float,
    ) -> None:
        self._material = material
        self._costo_materiales = costo_materiales
        self._superficie = superficie
        self._costo_hora = costo_hora
        self._costo_mano_obra = self.calcula_mano_obra(horas_estimadas)
        self._total = self.calcula_total(horas_estimadas)

    def calcula_mano_obra(self, horas_estimadas: float) -> float:
        mano_obra = self._costo_hora * horas_estimadas
        return mano_obra

    def calcula_total(self, horas_estimadas: float) -> float:
        total = self.calcula_mano_obra(horas_estimadas) + self._costo_materiales
        return total

    def genera_detalle_retrato(self) -> str:
        detalle_retrato = f"Costo insumos ({self._material}) = ${self._costo_materiales}\nMano de obra = ${self._costo_mano_obra}\nTotal = $ {self._total}"
        return detalle_retrato


# Podria tener una entidad que se llame superficies, donde se guarden con un tag que este unido al material, entonces cuando se elige el material, te da opciones de
# posibles superficies, teniendo datos como gramaje


class RetratoAcrilico(Retrato):
    def __init__(self, superficie: str, horas_estimadas: float) -> None:
        super().__init__("ACRÍLICOS", 6000.00, superficie, 2000.00, horas_estimadas)


class RetratoGouache(Retrato):
    def __init__(self, superficie: str, horas_estimadas: float) -> None:
        super().__init__("GOUACHE", 8000.00, superficie, 2000.00, horas_estimadas)


class RetratoOleo(Retrato):
    def __init__(self, superficie: str, horas_estimadas: float) -> None:
        super().__init__("ÓLEO", 11500.00, superficie, 3000.00, horas_estimadas)


class RetratoLapices(Retrato):
    def __init__(self, superficie: str, horas_estimadas: float) -> None:
        super().__init__("LAPICES", 6000.00, superficie, 1500.00, horas_estimadas)
