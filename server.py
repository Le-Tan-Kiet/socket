import socket
import sqlite3
from constant import *
import requestAPI as res
from threading import Thread
from tkinter.ttk import *
from tkinter import *
import os


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


def handleRequestServer(conn, addr):
    request = receiveList(conn)
    response = res.getCurrency(request[0], request[1])

    size = str(len(response))
    conn.sendall(size.encode(FORMAT))
    conn.recv(BUFFSIZE).decode(FORMAT)
    app.currentFrame.actiList.insert(
        END, f'Client: {addr} request ({request[0]},{request[1]})')

    for item in response:
        sendList(conn, item)
        conn.recv(BUFFSIZE).decode(FORMAT)


def closeAllConnect():
    # for c in clients:
    #     # try:
    #     #     c[0].sendall(CLOSE.encode(FORMAT))
    #     # except:
    #     #     pass
    #     c[0].close()
    # conx.close()

    app.destroy()
    s.close()
    os._exit(1)


def updateCliList():
    app.currentFrame.cliList.delete(0, END)
    for c in clients:
        app.currentFrame.cliList.insert(END, c[1])


# Start GUI


def StartServer(app):

    frame = Frame(app)
    canvas = Canvas(
        frame,
        bg="#ffffff",
        height=600,
        width=1000,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)
    # Background
    canvas.background_img = PhotoImage(file=f"ServerImg/background.png")
    canvas.create_image(
        0, 36, anchor='nw',
        image=canvas.background_img)
    # Entry IP
    canvas.entryIP_img = PhotoImage(file=f"ServerImg/IP.png")
    canvas.create_image(
        150, 28, anchor='nw',
        image=canvas.entryIP_img)

    frame.entryIP = Entry(frame,
                          bd=0, font=("", 11),
                          bg="#dfdfdf",
                          highlightthickness=0)

    frame.entryIP.place(
        x=165, y=28, anchor='nw',
        width=70.0,
        height=38)
    # Entry Port
    canvas.entryPort_img = PhotoImage(file=f"ServerImg/Port.png")
    canvas.create_image(
        264, 28, anchor='nw',
        image=canvas.entryPort_img)

    frame.entryPort = Entry(frame,
                            bd=0, font=("", 11),
                            bg="#dfdfdf",
                            highlightthickness=0)

    frame.entryPort.place(
        x=275, y=30, anchor='nw',
        width=50.0,
        height=35)
    # Activity List
    actiList_img = PhotoImage(file=f"ServerImg/img_textBox1.png")
    canvas.create_image(
        296.0, 44.0, anchor='nw',
        image=actiList_img)

    frame.actiList = Listbox(frame,
                             bd=0, font=("", 14),
                             bg="#dfdfdf",
                             highlightthickness=0)

    frame.actiList.place(
        x=428, y=132, anchor='nw',
        width=330,
        height=364)
    # Create Button
    canvas.btnCreate_img = PhotoImage(file=f"ServerImg/Create.png")
    btnCreate = Button(frame, image=canvas.btnCreate_img,
                       bd=0, bg="white", command=lambda: createServer(app))

    btnCreate.place(
        x=358, y=28, anchor=NW,
        width=70,
        height=40)

    return frame


def MainServer(app):
    frame = Frame(app)
    canvas = Canvas(
        frame,
        bg="#ffffff",
        height=600,
        width=1000,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)
    # Background
    canvas.background_img = PhotoImage(file=f"ServerImg/background.png")
    canvas.create_image(
        0, 36, anchor='nw',
        image=canvas.background_img)
    # Entry IP
    canvas.labelIP_img = PhotoImage(file=f"ServerImg/IP.png")
    canvas.create_image(
        150, 28, anchor='nw',
        image=canvas.labelIP_img)

    frame.labelIP = Label(frame,
                          bd=0, font=("", 11), text="",
                          bg="#dfdfdf",
                          highlightthickness=0)

    frame.labelIP.place(
        x=165, y=28, anchor='nw',
        width=70.0,
        height=38)
    # Entry Port
    canvas.labelPort_img = PhotoImage(file=f"ServerImg/Port.png")
    canvas.create_image(
        264, 28, anchor='nw',
        image=canvas.labelPort_img)

    frame.labelPort = Label(frame,
                            bd=0, font=("", 11), text="",
                            bg="#dfdfdf",
                            highlightthickness=0)

    frame.labelPort.place(
        x=280, y=28, anchor='nw',
        width=40.0,
        height=38)
    # Quit Button
    canvas.btnQuit_img = PhotoImage(file=f"ServerImg/quit0.png")
    btnQuit = Button(frame, image=canvas.btnQuit_img, bd=0,
                     bg="white", command=closeAllConnect)

    btnQuit.place(
        x=817, y=538, anchor=NW,
        width=120,
        height=50)
    actiList_img = PhotoImage(file=f"ServerImg/img_textBox1.png")
    canvas.create_image(
        296.0, 44.0, anchor='nw',
        image=actiList_img)

    frame.actiList = Listbox(frame,
                             bd=0, font=("", 11),
                             bg="#dfdfdf",
                             highlightthickness=0)

    frame.actiList.place(
        x=428, y=132, anchor='nw',
        width=330,
        height=364)

    cliList_img = PhotoImage(file=f"ServerImg/img_textBox2.png")
    canvas.create_image(
        580.0, 44.0, anchor='nw',
        image=cliList_img)

    frame.cliList = Listbox(frame,
                            bd=0, font=("", 11), justify="center",
                            bg="#dfdfdf",
                            highlightthickness=0)

    frame.cliList.place(
        x=799, y=132, anchor='nw',
        width=156,
        height=364)
    return frame


def switchFrame(app, nextFrame):
    newFrame = nextFrame(app)
    if app.currentFrame is not None:
        app.currentFrame.destroy()
    app.currentFrame = newFrame
    app.currentFrame.pack(fill="both", expand=True)


def createServer(app):
    global HOST, PORT
    HOST = app.currentFrame.entryIP.get()
    PORT = app.currentFrame.entryPort.get()
    if(HOST == "" or PORT == ""):
        app.currentFrame.actiList.delete(0, END)
        app.currentFrame.actiList.insert(END, 'Fields cannot be empty')
    else:
        global s
        PORT = int(app.currentFrame.entryPort.get())
        switchFrame(app, MainServer)
        app.currentFrame.labelIP["text"] = HOST
        app.currentFrame.labelPort["text"] = PORT
        s.bind((HOST, PORT))  # Create server
        s.listen()
        app.currentFrame.actiList.insert(END, f'Server: {HOST} {PORT}')
        app.currentFrame.actiList.insert(END, 'Waiting for client.........')

        # Update data
        res.updateData()

        thr = Thread(target=connectToCli)
        thr.daemon = True
        thr.start()


# Conncect To Client
def connectToCli():
    while True:
        try:
            conn, addr = s.accept()

            clients.add((conn, addr))
            thr = Thread(target=handleClient, args=(conn, addr))
            thr.daemon = True  # TRUE = Close thread whenever end main code
            thr.start()

        except:
            break
    # Handle Client


def serverLogin(conn: socket, addr, cursor):
    conn.sendall(EMPTY_MSG.encode(FORMAT))
    account = receiveList(conn)
    clientUsername = account[0]
    clientPassword = account[1]

    cursor.execute(
        'select password from loginInfo where username = ?', (clientUsername,))
    password = cursor.fetchone()
    # verify
    msg = SUCCESS
    if(password != None and clientPassword == password[0]):
        app.currentFrame.actiList.insert(
            END, f'{clientUsername}, login successfully!')
        msg = SUCCESS
    else:
        app.currentFrame.actiList.insert(END, f'{clientUsername}, login fail!')
        msg = FAIL
    conn.sendall(msg.encode(FORMAT))


def serverSignUp(conn: socket, addr, cursor, conx):
    account = receiveList(conn)
    clientUsername = account[0]
    clientPassword = account[1]
    clientPassConf = account[2]

    cursor.execute(
        'select password from loginInfo where username = ?', (clientUsername,))
    data = cursor.fetchall()
    # verify
    msg = SUCCESS
    if(len(data) == 0 and clientPassword == clientPassConf):
        cursor.execute("INSERT INTO loginInfo (username,password) values (?,?)",
                       (clientUsername, clientPassword))
        msg = SUCCESS
        app.currentFrame.actiList.insert(
            END, f'{clientUsername}, sign up succesfully!')
    else:
        app.currentFrame.actiList.insert(
            END, f'{clientUsername}, sign up fail!')
        msg = FAIL
    conx.commit()
    conn.sendall(msg.encode(FORMAT))


def handleClient(conn: socket, addr):
    app.currentFrame.cliList.insert(END, addr)
    app.currentFrame.actiList.insert(END, f'Client: {addr} connected')
    msg = None
    # Connect Database
    conx = sqlite3.connect('database.db')
    # Cursor
    cursor = conx.cursor()
    listOfTables = cursor.execute(
        """ SELECT name FROM sqlite_master WHERE type='table' AND name='loginInfo';""").fetchall()
    if listOfTables == []:
        cursor.execute(
            "CREATE TABLE loginInfo ( username varchar(10),password varchar(10))")
        cursor.execute(
            "INSERT INTO loginInfo (username,password) values ('admin','1')")
        app.currentFrame.actiList.insert(END, 'Database is created!')
    else:
        app.currentFrame.actiList.insert(END, 'Databse: Connected !')
    # Commit the changes db
    conx.commit()

    while (TRUE):
        try:
            msg = conn.recv(BUFFSIZE).decode(FORMAT)
        except:
            break
        if(msg == SIGNUP):
            serverSignUp(conn, addr, cursor, conx)
            continue
        if(msg == LOGIN):
            serverLogin(conn, addr, cursor)
            continue
        if(msg == REQUEST):
            handleRequestServer(conn, addr)
            continue
        if(msg == CLOSE):
            conn.close()
            break
        app.currentFrame.actiList.insert(END, f'Client {addr} says {msg}')

    clients.remove((conn, addr))
    updateCliList()
    app.currentFrame.actiList.insert(END, f'Client {addr} finised')
    # Login Server


# End GUI
# -------------- main ----------------
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients = set()
# Init window
app = Tk()
app.title("Currency App")
app.geometry("1000x600")
app.configure(bg="white")
app.resizable(width=False, height=False)
app.currentFrame = None
switchFrame(app, StartServer)
app.protocol("WM_DELETE_WINDOW", closeAllConnect)
app.mainloop()
