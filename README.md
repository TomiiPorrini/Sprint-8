# Diseño del Sprint-8 - Sprint Final

## INTRODUCCION 

En ITBANK se piensa en facilitar en todo momento la operación de nuestros clientes, por ese motivo, se necesita contar con una API REST que contenga una serie de servicios que permita interactuar con el banco de forma autónoma para nuestros clientes. 

La API que vamos a desarrollar es privada, accesible sólo a usuarios registrados e identificados por el banco. En este caso usaremos, Basic Authentication para generar una clave que permita al usuario interactuar con nuestros servicios. Solo un usuario cliente puede consultar sus propios datos

## PROBLEMATICA

* OBTENER DATOS DE UN CLIENTE 
    - Un cliente autenticado puede consultar sus propios datos
    > Link prueba: http://127.0.0.1:8000/api/cliente/info/DniABuscar/

* OBTENER SALDO DE CUENTA DE UN CLIENTE
    - Un cliente autenticado puede obtener el tipo de cuenta y su saldo
    > Link prueba: http://127.0.0.1:8000/api/cliente/cuenta/DniABuscar/


* OBTENER MONTO DE PRESTAMOS DE UN CLIENTE
    - Un cliente autenticado puede obtener el tipo de préstamo y total del mismo 
    > Link prueba: http://127.0.0.1:8000/api/cliente/prestamo/DniABuscar/

* OBTENER MONTO DE PRESTAMOS DE UNA SUCURSAL
    - Un empleado autenticado puede obtener el listado de préstamos otorgados de una sucursal determinada. 
    > Link prueba: http://127.0.0.1:8000/api/cliente/sucursal/IdSucursal/

* OBTENER TARJETAS ASOCIADAS A UN CLIENTE
    - Un empleado autenticado puede obtener el listado de tarjetas de crédito de un cliente determinado 
    > Link prueba: http://127.0.0.1:8000/api/cliente/tarjeta/DniABuscar/

* GENERAR UNA SOLICITUD DE PRESTAMO PARA UN CLIENTE
    - Un empleado autenticado puede solicitar un préstamo para un cliente, registrado el mismo y acreditando el saldo en su cuenta 

    > Link prueba: http://127.0.0.1:8000/api/cliente/solicitud-prestamo/

* ANULAR SOLICITUD DE PRESTAMO DE CLIENTE
    - Un empleado autenticado puede anular un préstamo para un cliente, revirtiendo el monto correspondiente 
    > Link prueba: http://127.0.0.1:8000/api/cliente/anular-prestamo/DniABuscar/

* MODIFICAR DIRECCION DE UN CLIENTE
    - El propio cliente autenticado o un empleado puede modificar las direcciones. 
    > Link prueba: http://127.0.0.1:8000/api/cliente/direccion/DniABuscar/

* LISTADO DE TODAS LAS SUCURSALES
    - Un endpoint público que devuelve el listado todas las sucursales con la información correspondiente. 
    > Link prueba: http://127.0.0.1:8000/api/sucursales


### Archivo de consigna
[Archivo-consigna-pdf](ConsignaFinal-Sprint-8.pdf)

## DATOS PARA PRUEBAS

#### CUENTAS

* EMPLEADO : (es Conan Livingston)
    - user: empleado
    - pwd: employee123

* CLIENTE 1: (es Moses Greer)
    - user: cliente
    - pwd: customer123

* CLIENTE 2: (es Leslie Moses)
    - user: cliente2
    - pwd: customer123

#### DNI a probar para las tarjetas.

1. 8712075
2. 74701370

##imagenes de resultados
- ![WhatsApp Image 2023-01-04 at 18 32 50](https://user-images.githubusercontent.com/105433665/210654064-b8b482f0-862a-47d3-bebb-56c75dbe3baa.jpeg)
- ![WhatsApp Image 2023-01-04 at 18 32 50 (1)](https://user-images.githubusercontent.com/105433665/210654165-bb189f32-33dd-4a14-a558-a46afe5403f3.jpeg)
- ![WhatsApp Image 2023-01-04 at 18 32 50 (2)](https://user-images.githubusercontent.com/105433665/210654192-ea21d416-6f7c-471c-a869-592d7f0feb9c.jpeg)
- ![WhatsApp Image 2023-01-04 at 18 32 50 (3)](https://user-images.githubusercontent.com/105433665/210654223-319480ca-8c83-4d25-9dcf-a4a752bd5e6c.jpeg)
- ![WhatsApp Image 2023-01-04 at 18 32 50 (4)](https://user-images.githubusercontent.com/105433665/210654250-0c2a1074-81b2-4dc8-ae54-041408aa02c8.jpeg)
