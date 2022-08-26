# Diseño del Sprint-8 - Sprint Final

## INTRODUCCION 

En ITBANK se piensa en facilitar en todo momento la operación de nuestros clientes, por ese motivo, se necesita contar con una API REST que contenga una serie de servicios que permita interactuar con el banco de forma autónoma para nuestros clientes. 

La API que vamos a desarrollar es privada, accesible sólo a usuarios registrados e identificados por el banco. En este caso usaremos, Basic Authentication para generar una clave que permita al usuario interactuar con nuestros servicios. Solo un usuario cliente puede consultar sus propios datos

## PROBLEMATICA

* OBTENER DATOS DE UN CLIENTE 
    - Un cliente autenticado puede consultar sus propios datos 
* OBTENER SALDO DE CUENTA DE UN CLIENTE
    - Un cliente autenticado puede obtener el tipo de cuenta y su saldo 
* OBTENER MONTO DE PRESTAMOS DE UN CLIENT
    - Un cliente autenticado puede obtener el tipo de préstamo y total del mismo 
* OBTENER MONTO DE PRESTAMOS DE UNA SUCURSA
    - Un empleado autenticado puede obtener el listado de préstamos otorgados de una sucursal determinada. 
* OBTENER TARJETAS ASOCIADAS A UN CLIENTE
    - Un empleado autenticado puede obtener el listado de tarjetas de crédito de un cliente determinado 
* GENERAR UNA SOLICITUD DE PRESTAMO PARA UN CLIENTE
    - Un empleado autenticado puede solicitar un préstamo para un cliente, registrado el mismo y acreditando el saldo en su cuenta 
* ANULAR SOLICITUD DE PRESTAMO DE CLIENTE
    - Un empleado autenticado puede anular un préstamo para un cliente, revirtiendo el monto correspondiente 
* MODIFICAR DIRECCION DE UN CLIENTE
    - El propio cliente autenticado o un empleado puede modificar las direcciones. 
* LISTADO DE TODAS LAS SUCURSALES
    - Un endpoint público que devuelve el listado todas las sucursales con la información correspondiente. 

### Archivo de consigna
[Archivo-consigna-pdf](ConsignaFinal-Sprint-8.pdf)

# DATOS PARA PRUEBAS

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