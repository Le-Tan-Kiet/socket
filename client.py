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

    client.sendall(END_MSG.encode(FORMAT))


def sendAccount(username, password):
    client.sendall(SIGNUP.encode(FORMAT))
    client.recv(BUFFSIZE).decode(FORMAT)
    client.sendall(username.encode(FORMAT))
    client.recv(BUFFSIZE).decode(FORMAT)
    client.sendall(password.encode(FORMAT))
    client.recv(BUFFSIZE).decode(FORMAT)


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


# def sendRequest():
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
            sendAccount(list)
            continue

        if msg == REQUEST:
            sendRequest()
            # Response
            response = receiveResponse()
            print('Response: ', response)
            continue
    client.close()
# End handle data received

# Start GUI


def changeFrameFromSignupToSearch(client_gui, username, password, pass_conf, alert_lbl):
    client.sendall(SIGNUP.encode(FORMAT))
    list = [username, password, pass_conf]
    sendList(list)

    # Input username
    is_valid_username = client.recv(BUFFSIZE).decode(FORMAT)
    if(is_valid_username == FAIL):
        alert_lbl.configure(text='Ten tai khoan khong hop le')
        return
    client.sendall(EMPTY_MSG.encode(FORMAT))
    # Input password

    is_valid_password = client.recv(BUFFSIZE).decode(FORMAT)
    if(is_valid_password == FAIL):
        alert_lbl.configure(text='Mat khau phai co it nhat 6 ki tu')
        return
    client.sendall(EMPTY_MSG.encode(FORMAT))
    # Input confirm password
    is_valid_pass_conf = client.recv(BUFFSIZE).decode(FORMAT)
    if(is_valid_pass_conf == FAIL):
        alert_lbl.configure(text='Mat khau khong khop')
        return
    client.sendall(EMPTY_MSG.encode(FORMAT))

    signup_frame.destroy()
    search_frame.pack(fill="both", expand=True)


def changeFrameFromLoginToSearch(client_gui, username, password, alert_lbl):
    client.sendall(LOGIN.encode(FORMAT))
    account = [username, password]
    sendList(account)

    is_valid_account = client.recv(BUFFSIZE).decode(FORMAT)
    if is_valid_account == FAIL:
        alert_lbl.configure(text='Tai khoan khong hop le')
        return

    # Delete current frame and add a new frame
    login_frame.destroy()
    search_frame.pack(fill="both", expand=True)


def changeFrameFromSignupToLogin(client_gui):
    # Delete current frame and add a new frame
    signup_frame.destroy()
    login_frame.pack(fill="both", expand=True)


def outputResult(entry_result, result):
    # Delete old value in result entry
    entry_result.delete(0, 15)
    # Insert new value in result entry
    entry_result.insert(0, result)


def handleRequestClient(entry_result, bank, currency_type):
    client.sendall(REQUEST.encode(FORMAT))
    request = [bank, currency_type]
    sendList(request)

    result = receiveResponse()
    outputResult(entry_result, result)


def endClient(client_gui):
    client_gui.destroy()


def search(client_gui):
    frame = Frame(client_gui)

    # Types of bank to search
    Label(frame, text='Bank').pack()
    bank = Combobox(frame)
    bank["value"] = ('Vietcombank', 'Vietinbank',
                     'Techcombank', 'BIDV', 'Sacombank', 'SBV')
    bank.current(0)
    bank.pack()

    # Types of currency to search
    Label(frame, text='Currency').pack()
    currency = Combobox(frame)
    currency["value"] = ('AUD', 'CAD', 'CHF', 'EUR', 'GBP', 'JPY', 'USD')
    currency.current(0)
    currency.pack()

    # Result of search
    Label(frame, text="Result: ").pack()
    entry_result = Entry(frame, width=20)
    btn = Button(frame, text="Search",
                 command=lambda: handleRequestClient(entry_result, bank.get(), currency.get()))
    btn.pack()
    entry_result.pack()
    # entry_result.configure(text=currency.get())

    # Exit button
    Button(frame, text="Exit", command=lambda: endClient(client_gui)).pack()

    return frame


def login(client_gui):
    frame = Frame(client_gui)
    # Username
    Label(frame, text="Username").pack()
    entry_username = Entry(frame, width=20)
    entry_username.pack()

    # Password
    Label(frame, text="Password").pack()
    entry_password = Entry(frame, width=20)
    entry_password.pack()

    # Alert when validation not successfully
    alert_lbl = Label(frame, text="", foreground='red')
    alert_lbl.pack()

    # Login button
    Button(frame, text="Login",
           command=lambda: changeFrameFromLoginToSearch(client_gui, entry_username.get(), entry_password.get(), alert_lbl)).pack()

    return frame


def signUp(client_gui):
    frame = Frame(client_gui)
    # Username
    Label(frame, text="Username").pack()
    entry_username = Entry(frame, width=20)
    entry_username.pack()

    # Password
    Label(frame, text="Password").pack()
    entry_password = Entry(frame, width=20)
    entry_password.pack()

    # Password confirm
    Label(frame, text="Password confirm").pack()
    entry_pass_conf = Entry(frame, width=20)
    entry_pass_conf.pack()

    # Alert when validation not successfully
    alert_lbl = Label(frame, text="", foreground='red')
    alert_lbl.pack()

    # Sign Up button
    Button(frame, text="Sign Up",
           command=lambda: changeFrameFromSignupToSearch(client_gui, entry_username.get(), entry_password.get(), entry_pass_conf.get(), alert_lbl)).pack()
    Button(frame, text="Da co tai khoan",
           command=lambda: changeFrameFromSignupToLogin(client_gui)).pack()
    return frame

# End GUI

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

    client_gui = Tk()
    client_gui.title("Client")
    client_gui.geometry("300x200")

    signup_frame = signUp(client_gui)
    login_frame = login(client_gui)
    search_frame = search(client_gui)
    signup_frame.pack(fill="both", expand=True)

    client_gui.mainloop()

except:
    print('Error')

client.close()
