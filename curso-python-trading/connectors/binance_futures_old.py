#Endpoint Base
#https://fapi.binance.com
#Endpoint dedicated
#https://testnet.binancefuture.com

#WebSocket Protocol
#wss://fstream.binance.com

#API Key
#I17yujEACdU03xH8h4sJZy9BhvikVImjAjSehabxS5XL60JqLfEvGSl89nSIoH7c

#Secret Key
#R5pn6X565F7iwWepdzeAgGk2L3Bh0cJGHZIUNi7aacVjZam3mV0q5ElvoFr23vJc

import logging
import requests
import pprint


logger = logging.getLogger()

def get_contracts():
    response_object = requests.get("https://api.binance.com/api/v3/exchangeInfo")
    #print(response_object.status_code, response_object.json())

    #mostramos el JSON formateado
    #pprint.pprint( response_object.json())

    contracts = []
    
    for contract in response_object.json()['symbols']:
        #imprimimos los contrato
        #pprint.pprint(contract)
        #imprimimos los pares de cada contrato
        #print(contract['symbol'])
        
        contracts.append(contract['symbol'])

    return contracts

#imprimimos los contratos tradeables en Binance Futures
print(get_contracts())