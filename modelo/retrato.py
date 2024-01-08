# retrato.py
# from abc import ABC, abstractmethod


class Retrato:
    def __init__(self, material: str, costo_hora: float) -> None:
        self._material = material
        self._costo_hora = costo_hora

    def calcula_costo_retrato(self, horas_estimadas: float) -> float:
        costo_retrato = self._costo_hora * horas_estimadas
        return costo_retrato
