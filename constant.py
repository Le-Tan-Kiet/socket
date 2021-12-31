from datetime import datetime

HOST = '127.0.0.1'
PORT = 55555
BUFFSIZE = 1024
FORMAT = 'utf8'

LOGIN = 'login'
SIGNUP = 'signup'
REQUEST = 'request'
CLOSE = 'close'

SUCCESS = 'success'
FAIL = 'fail'

END_MSG = 'end'
EMPTY_MSG = 'empty'

NAMEUSER = ""
DATETIME = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))


BANK_LIST = ['Vietcombank', 'Vietinbank',
             'Techcombank', 'BIDV', 'Sacombank', 'SBV']
TYPE_CURRENCY_LIST = ['AUD', 'CAD', 'CHF', 'EUR', 'GBP', 'JPY', 'USD']
