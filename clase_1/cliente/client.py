# -*- coding: utf-8 -*-
'''
Ejemplo de cliente de FIX utilizando la librería quickfix
El cliente se conecta a un servidor según los detalles de conexión del archivo de 
configuración. 
Es posible enviar una orden con el comando '1' y finalizar el programa con el comando '2'.
'''
import sys
import time
import thread
import argparse
from datetime import datetime
import quickfix as fix
from tools.echo import echo

ECHO_DEBUG=True
if ECHO_DEBUG:
    from tools.echo import echo
else:
    def echo(f):
        def decorated(*args, **kwargs):
            f(*args, **kwargs)
        return decorated

class Application(fix.Application):
    orderID = 0
    execID = 0
    def gen_ord_id(self):
        global orderID
        orderID+=1
        return orderID

    @echo
    def onCreate(self, sessionID):
            return
    @echo
    def onLogon(self, sessionID):
        # callback invocado en el logon
        self.sessionID = sessionID
        print ("Logueado con exito a la sesion '%s'." % sessionID.toString())
        return
    @echo
    def onLogout(self, sessionID): return
    @echo
    def toAdmin(self, sessionID, message):
        return
    @echo
    def fromAdmin(self, sessionID, message):
        return

    @echo
    def toApp(self, sessionID, message):
        # callback invocado cuando envia mensaje de aplicacion
        print "Mensaje enviado: %s" % message.toString()
        return
    @echo
    def fromApp(self, message, sessionID):
        # callback invocado cuando recibe mensaje de aplicacion
        print "Mensaje recibido: %s" % message.toString()
        return
    @echo
    def genOrderID(self):
    	self.orderID = self.orderID+1
    	return `self.orderID`
    @echo
    def genExecID(self):
    	self.execID = self.execID+1
    	return `self.execID`
    def put_order(self):
        # esta funcion envia una nueva orden LIMIT de compra, con ticker SMBL, cantidad 100 y precio 10
        print("Creando la siguiente orden: ")
        trade = fix.Message()
        trade.getHeader().setField(fix.BeginString(fix.BeginString_FIX42)) #
        trade.getHeader().setField(fix.MsgType(fix.MsgType_NewOrderSingle)) #39=D
        trade.setField(fix.ClOrdID(self.genExecID())) #11=Unique order
        trade.setField(fix.HandlInst(fix.HandlInst_MANUAL_ORDER_BEST_EXECUTION)) #21=3 (Manual order, best executiona)
        trade.setField(fix.Symbol('SMBL')) #55=SMBL ?
        trade.setField(fix.Side(fix.Side_BUY)) #43=1 Buy
        trade.setField(fix.OrdType(fix.OrdType_LIMIT)) #40=2 Limit order
        trade.setField(fix.OrderQty(100)) #38=100
        trade.setField(fix.Price(10)) # 44=10
        trade.setField(fix.TransactTime())
        print trade.toString()
        fix.Session.sendToTarget(trade, self.sessionID)

def main(config_file):
    try:
        # lee las configuraciones del archivo y se conecta al servidor
        settings = fix.SessionSettings( config_file )
        application = Application()
        storeFactory = fix.FileStoreFactory( settings )
        logFactory = fix.FileLogFactory( settings )
        initiator = fix.SocketInitiator( application, storeFactory, settings, logFactory )
        initiator.start()

        while 1:
            # espera input de la consola
            input = raw_input()
            if input == '1':
                # el comando "1" coloca una orden
                print "Colocando orden"
                application.put_order()
            if input == '2':
                # el comando "2" sale del programa
                sys.exit(0)
            if input == 'd':
                # el comando "d" permite debuguear
                import pdb
                pdb.set_trace()
            else:
                print "Ingresar 1 para mandar una orden, 2 para salir"
                continue
    except (fix.ConfigError, fix.RuntimeError), e:
        print e

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Cliente FIX')
    parser.add_argument('file_name', type=str, help='Nombre del archivo de configuracion')
    args = parser.parse_args()
    main(args.file_name)
