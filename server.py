import socket
from constant import *
from validation import *
# from requestAPI import getCurrency
import requestAPI as res
from threading import Thread


def receiveList(conn):
    list = []
    end_msg = 'end'

    item = conn.recv(BUFFSIZE).decode(FORMAT)
    while item != end_msg:
        list.append(item)
        conn.sendall(item.encode())
        item = conn.recv(BUFFSIZE).decode(FORMAT)

    return list


def receiveSignupAccount(conn):  # Receive account from client and return account
    account = []  # Init a list to contain username and password

    # Receive username, validate then add to list
    username = conn.recv(BUFFSIZE).decode(FORMAT)
    while validateSignupUsername(username) == False:
        conn.sendall('0'.encode(FORMAT))
        username = conn.recv(BUFFSIZE).decode(FORMAT)
    conn.sendall('1'.encode(FORMAT))
    account.append(username)
    # Receive password, validate then add to list
    password = conn.recv(BUFFSIZE).decode(FORMAT)
    while validateSignupPassword(password) == False:
        conn.sendall('0'.encode(FORMAT))
        password = conn.recv(BUFFSIZE).decode(FORMAT)
    conn.sendall('1'.encode(FORMAT))
    account.append(password)
    # Receive confirm password then validate
    pass_conf = conn.recv(BUFFSIZE).decode(FORMAT)
    while validateSignupConfirmPassword(password, pass_conf) == False:
        conn.sendall('0'.encode(FORMAT))
        pass_conf = conn.recv(BUFFSIZE).decode(FORMAT)
    conn.sendall('1'.encode(FORMAT))

    return account


def receiveLoginAccount(conn):
    account = []

    username = conn.recv(BUFFSIZE).decode(FORMAT)
    conn.sendall(username.encode(FORMAT))
    password = conn.recv(BUFFSIZE).decode(FORMAT)
    while validateLoginAccount(username, password) == False:
        conn.sendall('0'.encode(FORMAT))
        username = conn.recv(BUFFSIZE).decode(FORMAT)
        conn.sendall(username.encode(FORMAT))
        password = conn.recv(BUFFSIZE).decode(FORMAT)
    conn.sendall('1'.encode(FORMAT))
    account.append(username)
    account.append(password)

    return account


def receiveRequest(conn):
    request = []

    bank = conn.recv(BUFFSIZE).decode(FORMAT)
    conn.sendall(bank.encode(FORMAT))
    currency_type = conn.recv(BUFFSIZE).decode(FORMAT)
    while validateResquest(bank, currency_type) == False:
        conn.sendall('0'.encode(FORMAT))
        bank = conn.recv(BUFFSIZE).decode(FORMAT)
        conn.sendall(bank.encode(FORMAT))
        currency_type = conn.recv(BUFFSIZE).decode(FORMAT)
    conn.sendall('1'.encode(FORMAT))
    a = conn.recv(BUFFSIZE).decode(FORMAT)
    request.append(bank)
    request.append(currency_type)

    return request


def sendResponse(conn, request):
    response = str(res.getCurrency(request[0], request[1]))
    conn.sendall(response.encode(FORMAT))


def receiveMessage(conn, addr):
    print(f'Connected to client {addr}')

    while True:
        try:
            msg = conn.recv(BUFFSIZE).decode(FORMAT)
        except:
            break

        if msg == CLOSE:
            conn.close()
            break

        if msg == SIGNUP:
            account = receiveSignupAccount(conn)
            print('Sign Up Account: ', account)
            continue

        if msg == LOGIN:
            account = receiveLoginAccount(conn)
            print('Log In Account: ', account)
            continue

        if msg == 'list':
            list = receiveList(conn)
            print('List: ', list)
            continue

        if msg == REQUEST:
            request = receiveRequest(conn)
            print('Request: ', request)
            # Response
            sendResponse(conn, request)
            continue

        print(f'Client {addr} says {msg}')

    print(f'Client {addr} finished')


# -------------- main ----------------
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print('Server: ', HOST, PORT)
print('Waiting for client...')

while True:
    try:
        conn, addr = server.accept()
        thr = Thread(target=receiveMessage, args=(conn, addr))
        thr.daemon = False
        thr.start()

    except:
        print('Error')


print('End')
server.close()
