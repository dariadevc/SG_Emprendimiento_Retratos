# SG_Emprendimiento_Pinturas

_Proyecto para la asignatura Programación Orientada a Objetos en el año 2024._

## Requisitos del proyecto
* Utilizar el paradigma orientado a objetos.
* Altas bajas y modificaciones en base de datos (Al menos 3 ABMs).
* Impresión de reportes.
* Hacer uso de patrones de diseño. (3 Obligatorios)
* Uso significativo de herencia y excepciones.

## Descripción del proyecto
<p>Sistema que permite gestionar el servicio de realización de retratos a pedido del cliente y la venta de obras originales.<br>
El artista se maneja de la siguiente manera cuando es a pedido:</p>

* El cliente se contacta por email con detalles sobre el retrato que le gustaría que el artista realice.
* El precio lo determina con el costo de los insumos que estima que va a usar y las horas que estima que va a tomarle realizar el retrato, ya que trabaja con una relación de salario/hora.
* Comienza a trabajar en el retrato una vez se paga la totalidad del precio pactado.
* Una vez realizado el pago, el artista tiene establecido una cantidad de días como límite para la entrega del retrato encargado, que se le aclara al cliente en un inicio.

<p>Por el momento el artista realiza pinturas con gouache sobre hojas con gramaje de 300gr y pinceles varios, pero tiene la intención de probar nuevos materiales y trabajar en distintas superficies en el futuro.<br>
Teniendo esto en cuenta, el sistema gestionará los estados en que se encuentra el pedido de un cliente y el stock de materiales e insumos que posee, registrará datos de los clientes y determinará el precio final de un pedido.<br>
Además, al artista le interesa conocer la cantidad de retratos realizados, los insumos utilizados en total y las horas dedicadas, en un plazo de tiempo determinado.</p>

## Funcionalidades

<details>
<summary>Gestión de Pedidos</summary>

* Un pedido contiene los siguientes datos:
    * Nombre y apellido del cliente.
    * DNI del cliente
    * Número del pedido
    * Detalle
        * Al presupuestar un pedido:
            * Fecha de entrega estimada
            * Botón que genera una carpeta para guardar imagenes de referencia para el retrato.
            * Requisitos del cliente
        * En los estados “pendiente” y “en proceso”:
            * Fecha de entrega estimada
            * Botón que abre la carpeta en la que se encuentran las referencias para el retrato.
            * Requisitos del cliente.
        * Al finalizar un pedido:
            * Fecha de entrega estimada
    * Días restantes para la entrega del retrato (Todos los estados menos “presupuestado” y “entregado”)
* Un pedido pasa por los siguientes estados:
    * PRESUPUESTADO
    * DECLINADO
    * PENDIENTE
    * EN PROCESO
    * FINALIZADO
    * EMPAQUETADO
    * ENTREGADO AL CORREO
    * EN CAMINO
    * ENTREGADO AL CLIENTE

</details>

<details>
<summary>Registro de Clientes y sus pedidos</summary>

* Datos del cliente:
    * Nombre
    * Apellido
    * DNI
    * Email de contacto
* Listado de pedidos del cliente ordenados por número y el estado en el que se encuentran.
* Vista para que los clientes, al ingresar su DNI, puedan ver el estado de sus pedidos.
</details>

<details>
<summary>Impresión de reportes</summary>

* Se realizan reportes mensuales, para acceder a ellos debe ingresar el mes y año del que desea obtener los datos (MMAAAA).
* Los reportes a realizarse son los siguientes:
    * Listado de pedidos y clientes.
    * Listado de costos y ventas, y cálculo de ganancias.

</details>

- - - -

## Notas

<details>
<summary>06/03/24</summary>

* Ahora entiendo para qué funciona el patron DAO (Data Access Object). Permite separar la lógica de negocios del programa de la lógica de la base de datos.
    * El código se vuelve más mantenible, ya que si se cambia el lenguaje de la base de datos, la lógica de negocio no se ve modificada, solo la clase que maneja la conexión con la base de datos.
    * Permite que se cumpla el principio Single Responsability de SOLID, el cuál indica que una clase debe tener una única responsabilidad. De esta manera la clase Pedido maneja la lógica de negocio del pedido, mientras que PedidoDAO maneja los ABM en la base de datos.
    * Se realiza la abstracción, uno de los cuatros pilares de POO, ya que solo las clases DAO acceden a los datos de la base de datos, el resto del programa no necesita conocer como se trabaja con ella.
    * Todas estas cosas hacen que el código sea más robusto.

</details>
