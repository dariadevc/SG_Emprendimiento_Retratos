from retrato import Retrato


class RetratoOleo(Retrato):
    def __init__(self, superficie: str, horas_estimadas: float) -> None:
        super().__init__("ÓLEO", 11500.00, superficie, 3000.00, horas_estimadas)
