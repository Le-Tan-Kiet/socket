import socket
from constant import *
from tkinter import *
from tkinter.ttk import *
from validation import *

# Start handle data received


def sendList(list):
    for item in list:
        client.sendall(item.encode(FORMAT))
        client.recv(BUFFSIZE).decode(FORMAT)

    end_msg = 'end'
    client.sendall(end_msg.encode(FORMAT))


def sendSignupAccount():  # Send account to server
    # Input username
    username = input('Enter username: ')
    client.sendall(username.encode(FORMAT))
    is_valid_username = client.recv(BUFFSIZE).decode(FORMAT)
    while is_valid_username == '0':
        print('Invalid username! Please enter username again.')
        username = input('Enter username: ')
        client.sendall(username.encode(FORMAT))
        is_valid_username = client.recv(BUFFSIZE).decode(FORMAT)

    # Input password
    password = input('Enter password: ')
    client.sendall(password.encode(FORMAT))
    is_valid_password = client.recv(BUFFSIZE).decode(FORMAT)
    while is_valid_password == '0':
        print('Invalid password! Please enter password again.')
        password = input('Enter password: ')
        client.sendall(password.encode(FORMAT))
        is_valid_password = client.recv(BUFFSIZE).decode(FORMAT)

    # Input confirm password
    pass_conf = input('Enter confirm password: ')
    client.sendall(pass_conf.encode(FORMAT))
    is_valid_pass_conf = client.recv(BUFFSIZE).decode(FORMAT)
    while is_valid_pass_conf == '0':
        print('Password not match! Please enter confirm password again.')
        pass_conf = input('Enter confirm password: ')
        client.sendall(pass_conf.encode(FORMAT))
        is_valid_pass_conf = client.recv(BUFFSIZE).decode(FORMAT)

    print('Sign in successfully')


def sendLoginAccount():
    username = input('Enter username: ')
    client.sendall(username.encode(FORMAT))
    client.recv(BUFFSIZE).decode(FORMAT)
    password = input('Enter password: ')
    client.sendall(password.encode(FORMAT))
    is_validate_account = client.recv(BUFFSIZE).decode(FORMAT)
    while is_validate_account == '0':
        print('Username or password is not correct. Please login again')
        username = input('Enter username: ')
        client.sendall(username.encode(FORMAT))
        client.recv(BUFFSIZE).decode(FORMAT)
        password = input('Enter password: ')
        client.sendall(password.encode(FORMAT))
        is_validate_account = client.recv(BUFFSIZE).decode(FORMAT)

    print('Login successfully')


def sendRequest():
    bank = input('Enter bank: ')
    client.sendall(bank.encode(FORMAT))
    client.recv(BUFFSIZE).decode(FORMAT)
    currency_type = input('Enter currency_type: ')
    client.sendall(currency_type.encode(FORMAT))
    is_validate_request = client.recv(BUFFSIZE).decode(FORMAT)
    while is_validate_request == '0':
        print('Bank or currency_type is not correct. Please login again')
        bank = input('Enter bank: ')
        client.sendall(bank.encode(FORMAT))
        client.recv(BUFFSIZE).decode(FORMAT)
        currency_type = input('Enter currency_type: ')
        client.sendall(currency_type.encode(FORMAT))
        is_validate_request = client.recv(BUFFSIZE).decode(FORMAT)

    client.sendall(is_validate_request.encode(FORMAT))


def receiveResponse():
    response = client.recv(BUFFSIZE).decode(FORMAT)
    return response


def sendMessage():
    print('Client address: ', client.getsockname())

    while True:
        msg = input('Client: ')
        try:
            client.sendall(msg.encode(FORMAT))
        except:
            break

        if msg == CLOSE:
            break

        if msg == SIGNUP:
            sendSignupAccount()
            continue

        if msg == LOGIN:
            sendLoginAccount()
            continue

        if msg == 'list':
            list = ['kietle', '123']
            sendList(list)
            continue

        if msg == REQUEST:
            sendRequest()
            # Response
            response = receiveResponse()
            print('Response: ', response)
            continue
    client.close()
# End handle data received

# ----------------- main -------------------
# HOST = input('Enter host: ')
# PORT = input('Enter port: ')
# if not PORT:
#     PORT = 55555
# else:
#     PORT = int(PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    client.connect((HOST, PORT))
    sendMessage()


except:
    print('Error')

client.close()
