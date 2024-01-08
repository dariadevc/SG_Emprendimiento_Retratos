from retrato import Retrato


class RetratoGouache(Retrato):
    def __init__(self, superficie: str, horas_estimadas: float) -> None:
        super().__init__("GOUACHE", 8000.00, superficie, 2000.00, horas_estimadas)
