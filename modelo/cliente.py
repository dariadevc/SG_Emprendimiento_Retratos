# cliente.py
from database import DataBase


class ClienteExistente(Exception):
    def __init__(self, dni) -> None:
        super().__init__(f"El cliente con DNI {dni} ya existe en la base de datos.")


class ModeloClientes:
    def __init__(self) -> None:
        self.base = DataBase()

    # ABM

    def crear_cliente(self, nombre, apellido, dni, email):
        try:
            if self.cliente_existe(dni):
                raise ClienteExistente(dni)

            consulta = "INSERT INTO public.cliente (nombre_cliente, apellido_cliente, dni_cliente, email_cliente) VALUES (%s, %s, %s, %s)"
            parametros = nombre, apellido, dni, email
            self.base.query(consulta, parametros)
        except ClienteExistente as e:
            print(f"Error: {e}")



    def eliminar_cliente(self, id):
        pass

    # Otros

        def leer_clientes(self):
        datos = self.base.getAll("SELECT * FROM public.cliente")
        for i in datos:
            print(i)

    def cliente_existe(self, dni):
        # Verificar si el cliente con el DNI especificado ya existe en la base de datos
        consulta = "SELECT COUNT(*) FROM public.cliente WHERE dni_cliente = %s"
        parametros = (dni,)
        cantidad_clientes = self.base.get(consulta, parametros)[0]
        return cantidad_clientes > 0


clientes = ModeloClientes()

clientes.crear_cliente("MATEO", "CHOCOBAR", "12345678", "mchocobar@gmail.com")

clientes.leer_clientes()
