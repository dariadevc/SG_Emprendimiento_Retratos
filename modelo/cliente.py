# cliente.py
from database import DataBase

class Cliente:
    def __init__(self) -> None:
        self.__base= DataBase()

    def crear_cliente(self, nombre, apellido, dni, email):
        consulta = "INSERT INTO public.cliente (nombre_cliente, apellido_cliente, dni_cliente, email_cliente) VALUES (%s, %s, %s, %s)"
        parametros = nombre, apellido, dni, email
        self.__base.query(consulta, parametros)

    def leer_cliente(self):
        datos = self.__base.getAll(
            "SELECT * FROM public.cliente"
        )
        print((datos))

    def eliminar_cliente(self, id):
        pass


clientes = Cliente()

clientes.leer_cliente()