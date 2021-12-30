import socket
from constant import *
from validation import *
import requestAPI as res
from threading import Thread


def sendList(conn, list):
    for item in list:
        conn.sendall(str(item).encode(FORMAT))
        conn.recv(BUFFSIZE).decode(FORMAT)

    conn.sendall(END_MSG.encode(FORMAT))


def receiveList(conn):
    list = []

    item = conn.recv(BUFFSIZE).decode(FORMAT)
    while item != END_MSG:
        list.append(item)
        conn.sendall(EMPTY_MSG.encode(FORMAT))
        item = conn.recv(BUFFSIZE).decode(FORMAT)

    return list


def receiveSignupAccount(conn):  # Receive account from client and return account
    list = receiveList(conn)

    # Receive username, validate then add to list
    if validateSignupUsername(list[0]) == True:
        conn.sendall(SUCCESS.encode(FORMAT))
    else:
        conn.sendall(FAIL.encode(FORMAT))
        return []
    conn.recv(BUFFSIZE).decode(FORMAT)
    # Receive password, validate then add to list
    if validateSignupPassword(list[1]) == True:
        conn.sendall(SUCCESS.encode(FORMAT))
    else:
        conn.sendall(FAIL.encode(FORMAT))
        return []
    conn.recv(BUFFSIZE).decode(FORMAT)
    # Receive confirm password then validate
    if validateSignupConfirmPassword(list[1], list[2]) == True:
        conn.sendall(SUCCESS.encode(FORMAT))
    else:
        conn.sendall(FAIL.encode(FORMAT))
        return []
    conn.recv(BUFFSIZE).decode(FORMAT)
    account = []  # Init a list to contain username and password
    account.append(list[0])
    account.append(list[1])

    return account


def receiveLoginAccount(conn):
    account = receiveList(conn)

    if validateLoginAccount(account[0], account[1]) == False:
        conn.sendall(FAIL.encode(FORMAT))
        return []
    conn.sendall(SUCCESS.encode(FORMAT))

    return account


def handleRequestServer(conn):
    request = receiveList(conn)
    response = res.getCurrency(request[0], request[1])

    size = str(len(response))
    conn.sendall(size.encode(FORMAT))
    conn.recv(BUFFSIZE).decode(FORMAT)

    for item in response:
        sendList(conn, item)
        conn.recv(BUFFSIZE).decode(FORMAT)


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
            # conn.sendall(EMPTY_MSG.encode(FORMAT))
            account = receiveSignupAccount(conn)
            print('Sign Up Account: ', account)
            continue

        if msg == LOGIN:
            account = receiveLoginAccount(conn)
            print('Log In Account: ', account)
            continue

        if msg == REQUEST:
            handleRequestServer(conn)
            continue

        print(f'Client {addr} says {msg}')

    print(f'Client {addr} finished')


# -------------- main ----------------
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print('Server: ', HOST, PORT)
print('Waiting for client...')
res.updateData()

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
