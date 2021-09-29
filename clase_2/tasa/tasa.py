import pyRofex
import yfinance as yf
import time
import json

with open('config.json') as f:
  cfg = json.load(f)

pyRofex.initialize(user=cfg["user"], password=cfg["password"],account=cfg["account"], environment=pyRofex.Environment.REMARKET)

tickers_spots = yf.Tickers

# diccionarios a ser actualizados por el handler de pyRofex
prices_fwd = dict()
sizes_fwd = dict()

def market_data_handler(message):
    global forwards
    fwd = message["instrumentId"]["symbol"]
  
    # si no hay órdenes en alguno de los futuros lo saco de la lista
    if not message["marketData"]["OF"] or not message["marketData"]["BI"]:
        del spots[forwards.index(fwd)]
        forwards.remove(fwd)
    else:
        prices_fwd[fwd] = [ message["marketData"]["OF"][0]["price"],
                            message["marketData"]["BI"][0]["price"] ]
        sizes_fwd[fwd] = [ message["marketData"]["OF"][0]["size"],
                           message["marketData"]["BI"][0]["size"] ]

def order_report_handler(message):
    print("Order Report Message Received: {0}".format(message))

def error_handler(message):
    print("Error Message Received: {0}".format(message))

def exception_handler(e):
    print("Exception Occurred: {0}".format(e.message))

pyRofex.init_websocket_connection(market_data_handler, 
                                  order_report_handler, 
                                  error_handler,
                                  exception_handler,
                                  pyRofex.Environment.REMARKET)

pyRofex.order_report_subscription(environment=pyRofex.Environment.REMARKET)

def get_rates(cost_c=0, cost_t=0):    
    # calcular tasas
    buy_spot = dict(); sell_spot = dict()
    for spot in spots:
        buy_spot[spot] = tickers_spots.tickers[spot].info["ask"]
        sell_spot[spot] = tickers_spots.tickers[spot].info["bid"]
    
    buy_fwd = dict(); sell_fwd = dict()
    for fwd in forwards:
        buy_fwd[fwd] = prices_fwd[fwd][0]
        sell_fwd[fwd] = prices_fwd[fwd][1]

    colocadora = []; tomadora = []
    for i in range(0, len(spots)):
        spot = spots[i]; fwd = forwards[i]
        colocadora.append( round( (sell_fwd[fwd] - buy_spot[spot] - cost_c)/buy_spot[spot] * 100, 6 ) )
        tomadora.append( round( (buy_fwd[fwd] - sell_spot[spot] - cost_t)/sell_spot[spot] * 100, 6 ) )
    
    return colocadora, tomadora, buy_spot, sell_spot, buy_fwd, sell_fwd

def print_rates(colocadora, tomadora):
    for i in range(0, len(spots)):
        print("{} vs {} -- tasa colocadora: {} -- tasa tomadora: {}\n".format(spots[i], forwards[i], colocadora[i], tomadora[i]))

def check_opportunities(colocadora, tomadora, buy_spot, sell_spot, buy_fwd, sell_fwd):
    for i in range(0, len(spots)):
        if colocadora[i] > tomadora[i]:
            # si hay una oportunidad enviar las ordenes a rofex
            fwd = forwards[i]; spot = spots[i]

            profit = round((colocadora[i]-tomadora[i])*100, 2)
            print("** Oportunidad ", spots[i], "-", fwd, " **",
                  "\nSpot - Comprar a: ", buy_spot[spot], " Vender a: ", sell_spot[spot],
                  "\nProfit: ", profit, "%\n")
            
            # mando las órdenes a Rofex usando el tamaño que veo disponible
            pyRofex.send_order(ticker=fwd, 
                               size=sizes_fwd[fwd][0], 
                               side=pyRofex.Side.BUY, 
                               order_type=pyRofex.OrderType.LIMIT, 
                               price=buy_fwd[fwd],
                               cancel_previous=True)

            pyRofex.send_order(ticker=fwd, 
                               size=sizes_fwd[fwd][1], 
                               side=pyRofex.Side.SELL, 
                               order_type=pyRofex.OrderType.LIMIT, 
                               price=sell_fwd[fwd],
                               cancel_previous=True)

def update_rates(cost_c=0, cost_t=0, wait_time=1):
    # actualizar tasas
    colocadora_prev = [0]*len(spots); tomadora_prev = [0]*len(spots)
    
    while True:       
        colocadora, tomadora, buy_spot, sell_spot, buy_fwd, sell_fwd = get_rates(cost_c, cost_t)
        
        if (colocadora != colocadora_prev) or (tomadora != tomadora_prev):
            print_rates(colocadora, tomadora)
            colocadora_prev = colocadora
            tomadora_prev = tomadora

            check_opportunities(colocadora, tomadora, buy_spot, sell_spot, buy_fwd, sell_fwd)
            
        time.sleep(wait_time)

def init_tickers(forwards, spots):
    global tickers_spots
    tickers_spots = yf.Tickers(' '.join(spots)) 
    pyRofex.market_data_subscription(tickers=forwards, entries=[pyRofex.MarketDataEntry.BIDS, 
                                                                pyRofex.MarketDataEntry.OFFERS])

cost_c, cost_t = (0.1, 0.1)

forwards = ["GGAL/Oct21", "DLR/Oct21"]
spots = ["GGAL.BA", "ARS=X"]

init_tickers(forwards, spots)
update_rates(cost_c, cost_t, wait_time=1)