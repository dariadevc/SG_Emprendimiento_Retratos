from retrato import Retrato


class RetratoLapices(Retrato):
    def __init__(self, superficie: str, horas_estimadas: float) -> None:
        super().__init__("LAPICES", 6000.00, superficie, 1500.00, horas_estimadas)
