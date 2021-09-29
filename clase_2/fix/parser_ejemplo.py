# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:20:18 2020

@author: Javier
"""

#%%

import simplefix as sf

DATA_PATH = 'sample.log'

sample_W = "8=FIXT.1.19=69935=W34=3149=STUN52=20191218-15:13:47.00656=XXXX115=FGW48=AY24-0003-C-CT-ARS55=AY24106=0500-R167=GO207=XMEV262=-LwOZbEHbfINndJqyo1021=2268=14269=0270=2891271=25031346=1290=163=3269=0270=2889.5271=198528346=1290=263=3269=0270=2888271=3145346=3290=363=3269=0270=2883271=206881346=2290=463=3269=0270=2881271=1000346=1290=563=3269=1270=2894.5271=69096346=1290=163=3269=1270=2895271=90194346=1290=263=3269=1270=2896271=21730346=2290=363=3269=1270=2899.5271=500346=1290=463=3269=1270=2900271=341000346=7290=563=3269=2270=2889.5271=1472273=15:13:44288=-289=-63=3269=4270=274963=3269=8270=274563=3269=7270=292063=310=136'"
sample_Xs = ["8=FIXT.1.19=94135=X34=3949=STUN52=20191218-15:13:47.32556=XXXX115=FGW262=HUB083_MD_15766707131421021=2268=9279=0269=455=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=274963=3279=0269=855=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=274563=3279=0269=755=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=292063=3279=0269=955=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=2879.898262563=3279=0269=B55=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=14302101271=411885958.5600004273=15:13:47346=178563=3279=0269=2278=1887555=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=2891271=23425273=15:13:4763=3279=0269=A55=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=5.4363=3279=0269=655=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=289163=3279=0269=e55=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=274263=310=193",
"8=FIXT.1.19=82435=X34=4049=STUN52=20191218-15:13:47.33556=XXXX115=FGW262=HUB083_MD_15766707131421021=2268=8279=0269=455=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=274963=3279=0269=855=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=274563=3279=0269=755=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=292063=3279=0269=955=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=2879.91641663=3279=0269=B55=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=14325526271=412563175.3100004273=15:13:47346=178663=3279=0269=A55=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=5.4363=3279=0269=655=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=289163=3279=0269=e55=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=274263=310=095",
"8=FIXT.1.19=20935=X34=4349=STUN52=20191218-15:13:47.41056=XXXX115=FGW262=HUB083_MD_15766707131421021=2268=1279=1269=055=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=2891271=1606346=1290=163=310=102",
"8=FIXT.1.19=94335=X34=5949=STUN52=20191218-15:13:47.87856=XXXX115=FGW262=HUB083_MD_15766707131421021=2268=9279=0269=455=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=274963=3279=0269=855=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=274563=3279=0269=755=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=292063=3279=0269=955=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=2879.91641663=3279=0269=B55=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=14325526271=412563175.3100004273=15:13:47346=178663=3279=0269=2278=1888255=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=2894.5271=4066273=15:13:4763=3279=0269=A55=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=5.5663=3279=0269=655=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=2894.563=3279=0269=e55=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=274263=310=046",
"8=FIXT.1.19=82735=X34=6049=STUN52=20191218-15:13:47.91356=XXXX115=FGW262=HUB083_MD_15766707131421021=2268=8279=0269=455=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=274963=3279=0269=855=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=274563=3279=0269=755=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=292063=3279=0269=955=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=2879.920554163=3279=0269=B55=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=14329592271=412680865.6800004273=15:13:47346=178763=3279=0269=A55=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=5.5663=3279=0269=655=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=2894.563=3279=0269=e55=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=274263=310=023",
"8=FIXT.1.19=21235=X34=7149=STUN52=20191218-15:13:48.01256=XXXX115=FGW262=HUB083_MD_15766707131421021=2268=1279=1269=155=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=2894.5271=65030346=1290=163=310=248",
"8=FIXT.1.19=30935=X34=7549=STUN52=20191218-15:13:48.02356=XXXX115=FGW262=HUB083_MD_15766707131421021=2268=2279=2269=155=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=2894.5271=65030290=163=3279=0269=155=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=2903271=500346=1290=563=310=076",
"8=FIXT.1.19=21235=X34=8549=STUN52=20191218-15:13:48.05556=XXXX115=FGW262=HUB083_MD_15766707131421021=2268=1279=0269=155=AY2448=AY24-0003-C-CT-ARS167=GO207=XMEV106=0500-R270=2894.5271=69096346=1290=163=310=019"]

# constantes:

REFRESH_TYPE = '35'
FULL_REFRESH = b'W'
INCREMENTAL_REFRESH = b'X'

TICKER = '55'
AY24D = b'AY24D'
AY24C = b'AY24C'
AY24 = b'AY24'

PRICE = '270'
QTY = '271'

NUM_MESSAGES = '268'

MESSAGE_TYPE = '269'
BID = b'0'
OFFER = b'1'

ACTION = '279'
NEW = b'0'
CHANGE = b'1'
DELETE = b'2'

POSITION = '290'

#

#%%

def refresh_type(message):
    ''' retorna el tipo de mensaje de FIX de market data del que se trata '''
    if message.get(fix.REFRESH_TYPE) == fix.FULL_REFRESH:
        return 'FULL'
    elif message.get(fix.REFRESH_TYPE) == fix.INCREMENTAL_REFRESH:
        return 'INCREMENTAL'
    else:
        print('Unknown refresh message type')

def get_message_from_string(string):
    ''' retorna el objeto Fix Message correspondiente a la data cruda de input '''
    parser = sf.parser.FixParser()
    parser.append_buffer(string)
    return parser.get_message()

def parse_full_refresh_message(message):
    '''
    Parametros
    ----------
    message : un mensaje de snapshot full refresh de fix procesado por simplefix

    retorna el libro de ordenes en el formato
    [[[qty, px],
     [qty, px],
     [qty, px],
     [qty, px], 
     [qty, px]],
    
    [[qty, px],
     [qty, px],
     [qty, px],
     [qty, px], 
     [qty, px]]]
    

    '''
    bids = [[0,0]]*5
    offers = [[0,0]]*5
    num_blocks = msg.get(NUM_MESSAGES) # obtiene el numero de entradas del tag 268
    for i in range(1, int(num_blocks)+1):
        type_ = msg.get(MESSAGE_TYPE,i) # determina si es un bid o ask
        if type_ in [BID,OFFER]:
            px = float(msg.get(PRICE,i)) # obtiene el precio
            qty = int(msg.get(QTY,i)) # la cantidad
            position = int(msg.get(POSITION,i)) # y la posicion en el libro
            if type_ == BID:
                bids[position-1] = [qty,px]
            if type_ == OFFER:
                offers[position-1] = [qty,px]
    return [bids,offers]

def parse_incremental_refresh_message(message, book):
    '''
    Parametros
    ----------
    message : un mensaje de incremental refresh de fix procesado por simplefix
    book : un libro de ordenes en el format [bids,offers],
           donde bids y offers son dos listas de 5 elementos cada una de la forma
           [[qty, px],
            [qty, px],
            [qty, px],
            [qty, px], 
            [qty, px]]

    retorna el libro de ordenes con el mensaje incremental aplicado

    '''
    bids,offers = book
    num_blocks = msg.get(NUM_MESSAGES)
    for i in range(1, int(num_blocks)+1):
        type_ = msg.get(MESSAGE_TYPE,i)
        if type_ in [BID,OFFER]:
            position = int(msg.get(POSITION,i))
            action = msg.get(ACTION,i)
            if action == NEW:
                px = float(msg.get(PRICE,i))
                qty = int(msg.get(QTY,i))
                if type_ == BID:
                    bids = bids[0:position-1]+[[qty,px]]+bids[position-1:]
                if type_ == OFFER:
                    offers = offers[0:position-1]+[[qty,px]]+offers[position-1:]
            if action == DELETE:
                if type_ == BID:
                    del bids[position-1]
                if type_ == OFFER:
                    del offers[position-1]
            if action == CHANGE:
                if type_ == BID:
                    px_ = msg.get(PRICE,i)
                    if not px_ is None:    
                        px = float(px_)
                    else:
                        px = bids[position-1][1]
                    
                    qty_ = msg.get(QTY,i)
                    if not qty_ is None:    
                        qty = int(qty_)
                    else:
                        qty = bids[position-1][0]
                        
                    bids[position-1] = [qty,px]
                    
                if type_ == OFFER:
                    px_ = msg.get(PRICE,i)
                    if not px_ is None:    
                        px = float(px_)
                    else:
                        px = offers[position-1][1]
                    
                    qty_ = msg.get(QTY,i)
                    if not qty_ is None:    
                        qty = int(qty_)
                    else:
                        qty = offers[position-1][0]
                        
                    offers[position-1] = [qty,px]
                    
    return [bids[0:5],offers[0:5]]
   
#%%   

msg = get_message_from_string(sample_W)
book = parse_full_refresh_message(msg)

print(book[0])
print(book[1])

#%%

msg = get_message_from_string(sample_Xs[0])
new_book = parse_incremental_refresh_message(msg,book)

print(new_book[0])
print(new_book[1])

#%%

msg = get_message_from_string(sample_Xs[1])
new_book_2 = parse_incremental_refresh_message(msg,new_book)

print(new_book_2[0])
print(new_book_2[1])

#%%

msg = get_message_from_string(sample_Xs[2])
new_book_3 = parse_incremental_refresh_message(msg,new_book_2)

print(new_book_3[0])
print(new_book_3[1])

#%%

msg = get_message_from_string(sample_Xs[3])
new_book_4 = parse_incremental_refresh_message(msg,new_book_3)
print(new_book_4[0])
print(new_book_4[1])