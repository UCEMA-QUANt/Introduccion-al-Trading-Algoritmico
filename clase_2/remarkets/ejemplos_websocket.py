# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 18:17:08 2020

@author: Javier
"""

import pyRofex
import time
import json

with open('config.json') as f:
  cfg = json.load(f)

'''
estructura del json de config:
{
 "user":"user",
"password":"password",
"account":"account"
}
'''

#%%
# Detalles de la cuenta de test:
pyRofex.initialize(user=cfg["user"], password=cfg["password"],account=cfg["account"], environment=pyRofex.Environment.REMARKET)

#%%
     
# Primero hay que definir las funciones callback que van a ser invocadas para cada evento        
def market_data_handler(message):
    print("Mensaje de Market Data recibido: {0}".format(message))
def order_report_handler(message):
    print("Mensaje de Reporte de Orden recibido: {0}".format(message))
def error_handler(message):
    print("Mensaje de Error recibido: {0}".format(message))
def exception_handler(e):
    print("Ocurrió una excepción: {0}".format(e))

# Se inicia la conexión websocket y se pasan los callbacks definidos
pyRofex.init_websocket_connection(market_data_handler=market_data_handler,
                                  order_report_handler=order_report_handler,
                                  error_handler=error_handler,
                                  exception_handler=exception_handler)
#%%
# Definimos la lista de instrumentos de los cuales obtener Market Data
instruments = ["DLR/Oct21", "DLR/Nov21"]
# Definimos los detalles que queremos obtener de cada instrumento
entries = [pyRofex.MarketDataEntry.BIDS,
           pyRofex.MarketDataEntry.OFFERS,
           pyRofex.MarketDataEntry.LAST]
#%%
# Nos subscribimos para recibir mensajes
pyRofex.market_data_subscription(tickers=instruments,
                                 entries=entries, depth=5)

# Nos subscribimos a un instrumento inválido y vemos un error
#pyRofex.market_data_subscription(tickers=["InvalidInstrument"],
#                                 entries=entries)


#%%
# Subscribes to receive order report messages (default account will be used) **
pyRofex.order_report_subscription()

# Envía una orden límite de compra para el DONov20
order = pyRofex.send_order(ticker="DLR/Oct21",
                   side=pyRofex.Side.BUY,
                   size=10,
                   price=81.30,
                   order_type=pyRofex.OrderType.LIMIT)

# Esperar 5 segunos
time.sleep(5)


#%%
# Cancelar la orden
cancel_order = pyRofex.cancel_order(order["order"]["clientId"])


#%%
pyRofex.close_websocket_connection()
