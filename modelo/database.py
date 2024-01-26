import psycopg2
import string

class DataBaseMeta(type):
    __instances = None

    def __call__(cls, *args, **kwargs):
        if cls.__instances is None:
            instance = super().__call__(*args, **kwargs)
            cls.__instances = instance
        return cls.__instances


class DataBase(metaclass=DataBaseMeta):
    def __init__(self):
        try:
            self.conexion = psycopg2.connect(
                host="localhost",
                port="5432",
                database="emprendimiento_retratos",
                user="postgres",
                password="postgres",
            )
            print("¡Conexion exitosa!")
        except (Exception, psycopg2.DatabaseError) as error:
            print("error")

    def getAll(self, query, params=None):
        cursor = self.conexion.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
        # result = cursor.fetchall()
        # if result:
        #     return [item[0] for item in result]  # Extrae el primer elemento de cada tupla
        # else:
        #     return []

    def get(self, query, params=None):
        cursor = self.conexion.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()

    def query(self, query, params=None):
        cursor = self.conexion.cursor()
        cursor.execute(query, params)
        return cursor.connection.commit()


base = DataBase()
consulta = "SELECT detalle_dato, valor_dato FROM public.datos_id ORDER BY id_dato ASC; "
valores = base.getAll(consulta)

print(valores[0])  # Extrae como tupla

def num_character(num) -> str:
    """Convierte al número en una str que se completa con ceros a la izquierda hasta completar 3 dígitos"""

    num_char = str(num)
    if len(num_char) == 3:
        num_char = str(num)
    else:
        num_char = str(num)
        while len(num_char) < 3:
            num_char = f"0{num_char}"

    return num_char

abecedario = list(string.ascii_uppercase)

consulta = "SELECT id_dato, valor_dato FROM public.datos_id ORDER BY id_dato ASC;"  # Primer dato = posi_letra, segundo dato = num (Al reves en mi compu)
valores = base.getAll(consulta)
posi_letra = valores[0][1]
num = valores[1][1] 

nro_pedido = f"{abecedario[posi_letra]}{num_character(num)}"

if num >= 999:  # Obtenido de base de datos
    posi_letra += 1  # Obtenido de base de datos -> Tiene que actualizar la base
    num = 0
    consulta = "UPDATE public.datos_id SET valor_dato = CASE WHEN id_dato = 1 THEN %s WHEN id_dato = 2 THEN %s END;"
    parametros = posi_letra, num
else:
    num += 1  # -> Tiene que actualizar la base
    consulta = "UPDATE public.datos_id SET valor_dato = %s WHERE id_dato = 2"
    parametros = (num,)
base.query(consulta, parametros)

print(nro_pedido)
