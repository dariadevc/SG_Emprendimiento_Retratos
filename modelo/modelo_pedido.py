# pedido.py
from database import DataBase
import string
from datetime import datetime

# from modelo.modelo_cliente import Cliente
# from detalle import Detalle


# class Pedido:
    # def __init__(self, cliente: Cliente, detalle: Detalle, estado: str) -> None:
    #     self._id_pedido = None
    #     self._datos_cliente = cliente
    #     self._detalle = detalle
    #     self._estado_pedido = estado

    # # -- GETTERS Y SETTERS

    # def get_datos_cliente(self):
    #     print("Se estan obteniendo los datos de ")
    #     return self._datos_cliente

    # def set_datos_cliente(self, cliente):
    #     print("Se modificaron los datos de ")
    #     self._datos_cliente = cliente

    # def get_detalle(self):
    #     print("Se estan obteniendo los datos de ")
    #     return self._detalle

    # def set_detalle(self, detalle):
    #     print("Se modificaron los datos de ")
    #     self._detalle = detalle

    # def get_estado_pedido(self):
    #     print("Se estan obteniendo los datos de ")
    #     return self._estado_pedido

    # def set_estado_pedido(self, estado):
    #     print("Se modificaron los datos de ")
    #     self._estado_pedido = estado

    # def get_nro_pedido(self):
    #     print("Se esta obteniendo el número del pedido")
    #     return self._id_pedido

    # # -- OTROS MÉTODOS

    # def num_character(self, num) -> str:
    #     """Convierte al número en una str que se completa con ceros a la izquierda hasta completar 3 dígitos"""

    #     num_char = str(num)
    #     if len(num_char) == 3:
    #         num_char = str(num)
    #     else:
    #         num_char = str(num)
    #         while len(num_char) < 3:
    #             num_char = f"0{num_char}"

    #     return num_char

    # def genera_nro_pedido(
    #     self, posi_letra, num
    # ) -> str:  # posi_letra y num los obtiene de la base de datos
    #     abecedario = list(string.ascii_uppercase)

    #     if num == 999:
    #         posi_letra += 1
    #         num = 0
    #     else:
    #         num += 1
    #     self._id_pedido = f"{abecedario[posi_letra]}{self.num_character(num)}"


class ModeloPedidos:
    def __init__(self) -> None:
        self.base = DataBase()

    # * ABM

    def insertar_pedido(self, dni, horas_estimadas, requisitos):

        consulta = "SELECT id_cliente FROM public.cliente WHERE dni_cliente = %s"
        parametros = (dni,)
        id_cliente = self.base.get(consulta, parametros)
    
        # TODO: agregar código que genere carpeta titulada con el nro pedido según la ruta default (escritorio en carpeta emprendimiento, si no existe la genera al crear el primer pedido) o la que seleccione el usuario en el primer ingreso
        # TODO: agregar a la tabla config la ruta en la que se guardan las carpetas de referencia
        ruta_ref = "-"
        nro_pedido = self.genera_nro_pedido()

        consulta = "INSERT INTO public.pedido (id_cliente, horas_estimadas, estado_pedido, fecha_presupuestado, ruta_referencia, id_pedido_visible, requisitos_cliente) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        parametros = (
            id_cliente,
            horas_estimadas,
            "PRESUPUESTADO",
            datetime.now().strftime("%Y-%m-%d"),
            ruta_ref,
            nro_pedido,
            requisitos,
        )
        self.base.query(consulta, parametros)
        print("Pedido agregado con éxito a la base de datos.")

    def modificar_estado_pedido(self, nro_pedido, posi_estado):
        """Modifica el estado del pedido. Correlación entre posición y estado:
        (0) = APROBADO
        (1) = FINALIZADO
        (2) = ENTREGADO
        (3) = CANCELADO
        """
        estados = [
            "APROBADO",
            "FINALIZADO",
            "ENTREGADO",
            "CANCELADO",
        ]  # Cancelado funciona como una baja lógica, al igual que entregado, ya que dejan de figurar en la pantalla principal.

        if posi_estado == 0:
            consulta = "UPDATE public.pedido SET estado_pedido = %s, fecha_aprobado = %s WHERE id_pedido_visible = %s;"
        elif posi_estado == 1:
            consulta = "UPDATE public.pedido SET estado_pedido = %s, fecha_finalizado = %s WHERE id_pedido_visible = %s;"
        elif posi_estado == 2:
            consulta = "UPDATE public.pedido SET estado_pedido = %s, fecha_entregado = %s WHERE id_pedido_visible = %s;"
        else:
            consulta = "UPDATE public.pedido SET estado_pedido = %s, fecha_cancelado = %s WHERE id_pedido_visible = %s;"
        parametros = (
            estados[posi_estado],
            datetime.now().strftime("%Y-%m-%d"),
            nro_pedido,
        )
        self.base.query(consulta, parametros)

    def modificar_horas_reales(self, nro_pedido, horas):
        consulta = (
            "UPDATE public.pedido SET horas_reales = %s WHERE id_pedido_visible = %s;"
        )
        parametros = (horas, nro_pedido)
        self.base.query(consulta, parametros)

    # * OTROS

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

    def genera_nro_pedido(self) -> str:
        abecedario = list(string.ascii_uppercase)

        consulta = "SELECT id_dato, valor_dato FROM public.datos_id ORDER BY id_dato ASC;"  # Primer dato = posi_letra, segundo dato = num (Al reves en mi compu)
        valores = self.base.getAll(consulta)
        posi_letra = valores[0][1]
        num = valores[1][1] 

        nro_pedido = f"{abecedario[posi_letra]}{self.num_character(num)}"

        if num == 999:  # Obtenido de base de datos
            posi_letra += 1  # Obtenido de base de datos -> Tiene que actualizar la base
            num = 0
            consulta = "UPDATE public.datos_id SET valor_dato = CASE WHEN id_dato = 1 THEN %s WHEN id_dato = 2 THEN %s END;"
            parametros = posi_letra, num
        else:
            num += 1  # -> Tiene que actualizar la base
            consulta = "UPDATE public.datos_id SET valor_dato = %s WHERE id_dato = 2"
            parametros = (num,)
        self.base.query(consulta, parametros)

        print(f"Identificador del pedido generado: {nro_pedido}")
        return nro_pedido

pedido = ModeloPedidos()

pedido.insertar_pedido('43719784', '5', "Retrato de mascota al óleo.")
