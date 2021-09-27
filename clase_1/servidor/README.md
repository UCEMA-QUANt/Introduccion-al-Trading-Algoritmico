Ejemplo de uso de Python Quickfix
=================================

Servidor de FIX4.2 que permite controlar las respuestas que el servidor devuelve manualmente. Notifica cuando los clientes se conectan
y desconectan, cuando envian órdenes, cancelaciones y requisiciones de reemplazo. No responde automáticamente, permite que el usuario
reaccione manualmente de la manera que desee.

Comandos:

--> help ## ayuda
    print "Los comandos son: "
    book                       ## Muestra el libro de ordenes actual"
    ack [orderID]              ## Manda ack de un orden con orderID [orderID]"
    cancel [orderID]           ## Manda ack de cancelacion de orden con [orderID]"
    fill [orderID] [quantity]  ## Manda Fill de orderID con cantidad [quantity]"
    order [orderID]            ## Detalles de la orden [orderID]"
    remove [orderID]           ## Saca la orden [orderID] del libro"
    replace [orderID]          ## Manda un ReplaceAck para la orden [orderID]"
    replacepend [orderID]      ## Manda mensaje ReplacePending para la orden [orderID]"
    exit                       ## Cierra el servidor"
    
Algunas notas:
- "orderID" de los parámetros de un comando es la orderID asignada, no la clientOrderID en el mensaje recibido
- el programa soporta clientes concurrentes
- no hay lógica para lidiar con problemas de sequence numbers
- no elimina la orden del libro cuando está finalizada, se pueden seguir mandando mensajes para estas órdenes
