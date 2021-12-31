import requests
import json
from constant import *
from threading import Timer
from datetime import datetime

data = {}


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
    # Resquest to get currency
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

    for item in BANK_LIST:
        data[item] = getBankData(item, token)

    return data


def updateData():
    global data
    data = getData()
    global DATETIME
    DATETIME = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    Timer(1800, updateData).start()


def getCurrencyBank(bank, type_currency):
    list = ["0", "0", "0", "0", "0"]
    for item in data[bank]:
        if item["currency"] == type_currency:
            list[0] = bank
            list[1] = item["currency"]
            list[4] = item["sell"]
            for i in item:
                if list[2] == "0" and (i == "buy" or i == "buy_cash"):
                    list[2] = str(item[i])
                if list[3] == "0" and i == "buy_transfer":
                    list[3] = str(item[i])
    return list


def getCurrency(bank, type_currency):  # Get sell currency
    # Find currency
    list = []
    if bank == "All" and type_currency == "All":
        for i in BANK_LIST:
            for j in TYPE_CURRENCY_LIST:
                list_item = getCurrencyBank(i, j)
                list.append(list_item)
    elif bank == "All":
        for i in BANK_LIST:
            list_item = getCurrencyBank(i, type_currency)
            list.append(list_item)
    elif type_currency == "All":
        for j in TYPE_CURRENCY_LIST:
            list_item = getCurrencyBank(bank, j)
            list.append(list_item)
    else:
        list_item = getCurrencyBank(bank, type_currency)
        list.append(list_item)

    return list
