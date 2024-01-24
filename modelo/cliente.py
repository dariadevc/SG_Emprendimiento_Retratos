# cliente.py
from database import DataBase


# Excepciones
class ClienteExistente(Exception):
    def __init__(self, dni) -> None:
        super().__init__(f"El cliente con DNI {dni} ya existe en la base de datos.")


# Cliente


# class Cliente: #*-> No creo usarlo
# def __init__(self, nombre=None, apellido=None, dni=None, email=None) -> None:
#     self._nombre = nombre
#     self._apellido = apellido
#     self._dni = dni
#     self._email = email

# def get_nombre(self):
#     print("Se accedió al nombre del cliente")
#     return self._nombre

# def set_nombre(self, nombre):
#     if self._nombre == nombre:
#         print("El nombre ingresado ya pertenece al cliente.")
#     else:
#         print("Se modificó el nombre del cliente")
#         self._nombre = nombre

# def get_apellido(self):
#     print("Se accedió al apellido del cliente")
#     return self._apellido

# def set_apellido(self, apellido):
#     if self._apellido == apellido:
#         print("El apellido ingresado ya pertenece al cliente.")
#     else:
#         print("Se modificó el apellido del cliente")
#         self._apellido = apellido

# def get_dni(self):
#     print("Se accedió al dni del cliente")
#     return self._dni

# def set_dni(self, dni):
#     if self._dni == dni:
#         print("El dni ingresado ya pertenece al cliente.")
#     else:
#         print("Se modificó el dni del cliente")
#         self._dni = dni

# def get_email(self):
#     print("Se accedió al email del cliente")
#     return self._email

# def set_email(self, email):
#     if self._email == email:
#         print("El email ingresado ya pertenece al cliente.")
#     else:
#         print("Se modificó el email del cliente")
#         self._email = email


# ModeloCliente
class ModeloClientes:
    def __init__(self) -> None:
        self.base = DataBase()
        self.cliente = None

    # ABM

    def insertar_cliente(self, nombre, apellido, dni, email):
        try:
            if self.cliente_existe(dni):
                raise ClienteExistente(dni)

            consulta = "INSERT INTO public.cliente (nombre_cliente, apellido_cliente, dni_cliente, email_cliente) VALUES (%s, %s, %s, %s)"
            parametros = nombre, apellido, dni, email
            self.base.query(consulta, parametros)
            print("Cliente agregado con éxito a la base de datos.")
        except ClienteExistente as e:
            print(f"Error: {e}")

    def modificar_cliente(self, dni_a, nombre_n, apellido_n, dni_n, email_n):
        consulta = "UPDATE public.cliente SET nombre_cliente = %s, apellido_cliente = %s, dni_cliente = %s, email_cliente = %s WHERE dni_cliente = %s;"
        parametros = (nombre_n, apellido_n, dni_n, email_n, dni_a)
        self.base.query(consulta, parametros)

    def eliminar_cliente(self, dni):
        datos = self.extrae_datos_cliente(dni)
        print(
            f"El cliente {datos[0]} {datos[1]}, con dni {datos[2]}, fue eliminado de la base de datos."
        )
        consulta = "DELETE FROM public.cliente WHERE dni_cliente = %s;"
        parametros = (dni,)
        self.base.query(consulta, parametros)

    # Otros

    def leer_clientes(self):
        datos = self.base.getAll(
            "SELECT nombre_cliente, apellido_cliente, dni_cliente, email_cliente FROM public.cliente"
        )
        for i in datos:
            print(i)

    def leer_un_cliente(self, dni):
        consulta = "SELECT nombre_cliente, apellido_cliente, dni_cliente, email_cliente FROM public.cliente WHERE dni_cliente = %s"
        parametro = (dni,)
        datos = self.base.get(consulta, parametro)
        print(datos)

    def extraer_datos_cliente(self, dni):
        consulta = "SELECT nombre_cliente, apellido_cliente, dni_cliente, email_cliente FROM public.cliente WHERE dni_cliente = %s"
        parametro = (dni,)
        datos = self.base.get(consulta, parametro)
        # cliente = Cliente(datos[0], datos[1], datos[2], datos[3]) #*¿Por qué usar un objeto cliente, si puedo usar la lista de datos para mostrar
        print("Estos fueron los datos extraídos: ", (datos))
        return datos

    def cliente_existe(self, dni):
        # Verificar si el cliente con el DNI especificado ya existe en la base de datos
        consulta = "SELECT COUNT(*) FROM public.cliente WHERE dni_cliente = %s"
        parametros = (dni,)
        cantidad_clientes = self.base.get(consulta, parametros)[0]
        return cantidad_clientes > 0


# * Prueba del ModeloClientes()

# clientes = ModeloClientes()

# clientes.insertar_cliente("MATEO", "CHOCOBAR", "12345678", "mchocobar@gmail.com")

# clientes.leer_clientes()
# clientes.leer_un_cliente("43719784")


# datos_cliente = clientes.extraer_datos_cliente("12345678")
# clientes.modificar_cliente(
#     "12345678", "ELIAS", datos_cliente[1], datos_cliente[2], datos_cliente[3]
# )

# clientes.leer_clientes()

# clientes.eliminar_cliente("12345678")

# clientes.leer_clientes()
