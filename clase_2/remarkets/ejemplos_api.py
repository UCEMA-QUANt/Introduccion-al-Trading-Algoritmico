# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 18:15:33 2020

@author: Javier
"""

import pyRofex
import datetime

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
pyRofex.initialize(user=cfg["user"],
                   password=cfg["password"],
                   account=cfg["account"],
                   environment=pyRofex.Environment.REMARKET)

#%% ############ DATOS DE REFERENCIA SOBRE EL MERCADO ################

# Obtener los segmentos del mercado
segmentos = pyRofex.get_segments()

# Obtener los segmentos e imprimirlos:
segments = pyRofex.get_segments()
for segment in segments['segments']:
    print("ID del segmento: {0}".format(segment['marketSegmentId']))

# Obtenemos una lista de los instrumentos y contamos cuantos son
instruments = pyRofex.get_all_instruments()
print("Número de instrumentos:: {0}".format(len(instruments['instruments'])))

# Obtenemos una lista detallada e imprimimos detalles:
detailed = pyRofex.get_detailed_instruments()
for i in range(5):
    print("#### DETALLE para {0}: {1}".format(detailed['instruments'][i]['instrumentId']['symbol'],
                                                  detailed['instruments'][i]))
    print("#### FIN DE DETALLE ####")

#%% ########### MARKET DATA #############
# Realiza un pedido a la API Rest para obtener el último precio, bids y offers del instrumento
entries = [pyRofex.MarketDataEntry.BIDS, pyRofex.MarketDataEntry.OFFERS, pyRofex.MarketDataEntry.LAST]
ticker = "DLR/Oct21"
market_data = pyRofex.get_market_data(ticker=ticker,entries=entries, depth=5)

print("Respuesta al pedido de market data para {0}: {1}".format(ticker, market_data))
#%%

# Obtener toda la info del instrumento:
entries = [
    pyRofex.MarketDataEntry.BIDS,
    pyRofex.MarketDataEntry.OFFERS,
    pyRofex.MarketDataEntry.LAST,
    pyRofex.MarketDataEntry.CLOSING_PRICE,
    pyRofex.MarketDataEntry.OPENING_PRICE,
    pyRofex.MarketDataEntry.HIGH_PRICE,
    pyRofex.MarketDataEntry.LOW_PRICE,
    pyRofex.MarketDataEntry.SETTLEMENT_PRICE,
    pyRofex.MarketDataEntry.NOMINAL_VOLUME,
    pyRofex.MarketDataEntry.TRADE_EFFECTIVE_VOLUME,
    pyRofex.MarketDataEntry.TRADE_VOLUME,
    pyRofex.MarketDataEntry.OPEN_INTEREST
]
market_data = pyRofex.get_market_data(ticker, entries)
print("Market data más completa para {0}: {1}".format(ticker, market_data))

#%%
import datetime


# Obtener datos históricos desde el comienzo del año hasta hoy
end = datetime.date.today()
start = datetime.date(year=end.year, month=9, day=1)
historic_trades = pyRofex.get_trade_history(ticker=ticker, start_date=start, end_date=end)
print("Datos históricos {0} from {1} to {2}: {3}".format(ticker, start, end, historic_trades))

# obtener los precios de los trades y printear
trades = [e['price'] for e in historic_trades['trades']]
print(trades)

#%% Manejo de órdenes

# Envía una orden límite de compra para el instrumento
order = pyRofex.send_order(ticker=ticker,
                           side=pyRofex.Side.BUY,
                           size=10,
                           price=100.72,
                           order_type=pyRofex.OrderType.LIMIT)

# Print the response
print("Respuesta del envío de orden: {0}".format(order))

# Ver cómo quedó la orden
order_status = pyRofex.get_order_status(order["order"]["clientId"])

# Mostrarlo
print("Respuesta del estado de la orden: {0}".format(order_status))

# si la orden se queda en PENDING_NEW continuar 'poleando' hasta que se coloque
timeout = 5 # Time out 5 seconds

while order_status["order"]["status"] == "PENDING_NEW" and timeout > 0:
    time.sleep(1)
    order_status = pyRofex.get_order_status(order["order"]["clientId"])

    # Print Order Status
    print("Chequear nuevamente el estado de la orden: {0}".format(order_status))

    timeout = timeout - 1

# Obetener nuevamente el status
pyRofex.get_order_status(order["order"]["clientId"])

#%%

# Cancelar la orden
cancel_order = pyRofex.cancel_order(order["order"]["clientId"])

# Chequear el status de la orden luego del envío de la cancelación
pyRofex.get_order_status(cancel_order["order"]["clientId"])

#%%

# Obtener el estado de las órdenes de esta cuenta
print(pyRofex.get_all_orders_status())

