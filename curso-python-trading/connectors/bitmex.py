#API Key
#w2VkMeZPaagaKK-Yf6gAwaxz

#API Secret
#aJ3MgDn99XK6pbzFrmIhjd5KiXw99WnOYKw2us-4OUrby81t

import requests

def get_contracts():
    contracts = []

    #imprimimos los contratos activos
    response_object = requests.get("https://www.bitmex.com/api/v1/instrument/active") 

    for contract in response_object.json():
        contracts.append(contract['symbol'])

    return contracts

print(get_contracts())