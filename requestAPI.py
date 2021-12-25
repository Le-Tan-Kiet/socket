import requests
import json
from threading import Timer

data = ''
isUpdate = False


def getBankId(bank):  # Get bank name by bank ID
    if bank == 'Vietcombank':
        return 'vcb'
    if bank == 'Vietinbank':
        return 'ctg'
    if bank == 'Techcombank':
        return 'tcb'
    if bank == 'BIDV':
        return 'bid'
    if bank == 'Sacombank':
        return 'stb'
    if bank == 'SBV':
        return 'sbv'


def getData(bank):
    # Resquest to get token for authorization
    api_key = requests.get(
        'https://vapi.vnappmob.com/api/request_api_key?scope=exchange_rate&fbclid=IwAR1LiVpNea58gxXeGZgPX6QWRRJQpkFfS_r41PJRsuy2z7-1uurKflwhGWo')
    token = json.loads(api_key.content)["results"]

    # Resquest to get currency transform
    api_url = 'https://vapi.vnappmob.com/api/v2/exchange_rate/%s'
    api_url = api_url % (str(getBankId(bank)))
    response = requests.get(
        api_url, headers={'Authorization': 'Bearer ' + token})

    return json.loads(response.content)["results"]


def updateData(bank):
    global data
    data = getData(bank)
    Timer(1800, updateData).start()


def getCurrency(bank, type_currency):  # Get sell currency
    global isUpdate
    if isUpdate == False:
        updateData(bank)
        isUpdate == True

    # Find currency transform
    for x in data:
        if x["currency"] == type_currency:
            return x["sell"]
    return 0  # If don't find currency transform, return 0
