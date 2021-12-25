import json
import requests


# Get db
#
#

account = [
    ('user1', '123456'),
    ('user2', '123456'),
    ('user3', '123456'),
    ('user4', '123456'),
    ('user5', '123456'),
]


def validateSignupUsername(username):
    if username == '':
        return False
    for user in account:
        if(user[0] == username):
            return False
    return True


def validateSignupPassword(password):
    if password == '':
        return False
    if len(password) < 6:
        return False
    return True


def validateSignupConfirmPassword(password, pass_conf):
    if pass_conf == '':
        return False
    if pass_conf == password:
        return True
    return False


def validateLoginAccount(username, password):
    for user in account:
        if (user[0] == username) and (user[1] == password):
            return True

    return False


def validateResquest(bank, currency_type):
    if bank not in ['Vietcombank', 'Vietinbank', 'Techcombank', 'BIDV', 'Sacombank', 'SBV']:
        return False
    if currency_type not in ['AUD', 'CAD', 'CHF', 'EUR', 'GBP', 'JPY', 'USD']:
        return False
    return True
