import requests
import json
from threading import Timer

data = []


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


def getBankData(bank, token):  # Get bank data by bank
    # Resquest to get currency transform
    api_url = 'https://vapi.vnappmob.com/api/v2/exchange_rate/%s'
    api_url_bank = api_url % (str(getBankId(bank)))
    response = requests.get(
        api_url_bank, headers={'Authorization': 'Bearer ' + token})
    return json.loads(response.content)["results"]


def getData():
    global data
    # Resquest to get token for authorization
    api_key = requests.get(
        'https://vapi.vnappmob.com/api/request_api_key?scope=exchange_rate&fbclid=IwAR1LiVpNea58gxXeGZgPX6QWRRJQpkFfS_r41PJRsuy2z7-1uurKflwhGWo')
    token = json.loads(api_key.content)["results"]

    bank_list = ['Vietcombank', 'Vietinbank',
                 'Techcombank', 'BIDV', 'Sacombank', 'SBV']
    for item in bank_list:
        data.append(getBankData(item, token))

    return data


def updateData():
    data = getData()
    Timer(1800, updateData).start()


def getCurrency(bank, type_currency):  # Get sell currency
    # Find currency transform
    if bank == 'Vietcombank':
        for x in data[0]:
            if x["currency"] == type_currency:
                return x["sell"]
    elif bank == 'Vietinbank':
        for x in data[1]:
            if x["currency"] == type_currency:
                return x["sell"]
    elif bank == 'Techcombank':
        for x in data[2]:
            if x["currency"] == type_currency:
                return x["sell"]
    elif bank == 'BIDV':
        for x in data[3]:
            if x["currency"] == type_currency:
                return x["sell"]
    elif bank == 'Sacombank':
        for x in data[4]:
            if x["currency"] == type_currency:
                return x["sell"]
    elif bank == 'SBV':
        for x in data[5]:
            if x["currency"] == type_currency:
                return x["sell"]
