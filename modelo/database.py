import psycopg2


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
                database="emprendimiento_retratos_db",
                user="postgres",
                password="postgres",
            )
            print("¡Conexion exitosa!")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def getAll(self, query, params = None):
        cursor = self.conexion.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    def get(self, query, params = None):
        cursor = self.conexion.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()

    def query(self, query, params = None):
        cursor = self.conexion.cursor()
        cursor.execute(query, params)
        return cursor.connection.commit()
