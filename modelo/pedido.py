# pedido.py
import string
from cliente import Cliente
from detalle import Detalle


class Pedido:
    def __init__(self, cliente: Cliente, detalle: Detalle, estado: str) -> None:
        self._datos_cliente = cliente
        self._detalle = detalle
        self._nro_pedido = None
        self._estado_pedido = estado

    # -- GETTERS Y SETTERS

    def get_datos_cliente(self):
        print("Se estan obteniendo los datos de ")
        return self._datos_cliente

    def set_datos_cliente(self, cliente):
        print("Se modificaron los datos de ")
        self._datos_cliente = cliente

    def get_detalle(self):
        print("Se estan obteniendo los datos de ")
        return self._detalle

    def set_detalle(self, detalle):
        print("Se modificaron los datos de ")
        self._detalle = detalle

    def get_estado_pedido(self):
        print("Se estan obteniendo los datos de ")
        return self._estado_pedido

    def set_estado_pedido(self, estado):
        print("Se modificaron los datos de ")
        self._estado_pedido = estado

    def get_nro_pedido(self):
        print("Se esta obteniendo el número del pedido")
        return self._nro_pedido

    # -- OTROS MÉTODOS

    def num_character(self, num) -> str:
        """Convierte al número en una str que se completa con ceros a la izquierda hasta completar 3 dígitos"""

        num_char = str(num)
        if len(num_char) == 3:
            num_char = str(num)
        else:
            num_char = str(num)
            while len(num_char) < 3:
                num_char = f"0{num_char}"

        return num_char

    def genera_nro_pedido(
        self, posi_letra, num
    ) -> str:  # posi_letra y num los obtiene de la base de datos
        abecedario = list(string.ascii_uppercase)

        if num == 999:
            posi_letra += 1
            num = 0
        else:
            num += 1
        self._nro_pedido = f"{abecedario[posi_letra]}{self.num_character(num)}"
