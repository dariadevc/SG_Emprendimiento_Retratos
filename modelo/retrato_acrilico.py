from retrato import Retrato


class RetratoAcrilico(Retrato):
    def __init__(self, superficie: str, horas_estimadas: float) -> None:
        super().__init__("ACRÍLICOS", 6000.00, superficie, 2000.00, horas_estimadas)
