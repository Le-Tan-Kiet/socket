from tkinter import *
from tkinter.ttk import *


def changeFrameFromSignupToSearch(client, recv_username, recv_password, pass_conf, alert_lbl):
    # Validate before change frame
    if(validateUsername(recv_username) == False):
        alert_lbl.configure(text='Ten tai khoan khong hop le')
        return
    elif(validatePassword(recv_password) == False):
        alert_lbl.configure(text='Mat khau phai co it nhat 6 ki tu')
        return
    elif(validatePasswordConfirm(recv_password, pass_conf) == False):
        alert_lbl.configure(text='Mat khau khong khop')
        return

    # Delete current frame and add a new frame
    signup_frame.destroy()
    search_frame.pack(fill="both", expand=True)


def changeFrameFromLoginToSearch(client, recv_username, recv_password, alert_lbl):
    if validateLoginAccount(recv_username, recv_password) == False:
        alert_lbl.configure(text='Tai khoan khong hop le')
        return

    # Delete current frame and add a new frame
    login_frame.destroy()
    search_frame.pack(fill="both", expand=True)


def changeFrameFromSignupToLogin(client):
    # Delete current frame and add a new frame
    signup_frame.destroy()
    login_frame.pack(fill="both", expand=True)


def outputResult(entry_result, type_currency, bank):
    # Delete old value in result entry
    entry_result.delete(0, 15)
    # Insert new value in result entry
    entry_result.insert(0, getCurrency(type_currency, bank))


def endClient():
    client.destroy()


def search(client):
    frame = Frame(client)
    # Types of currency to search
    Label(frame, text='Currency').pack()
    currency = Combobox(frame)
    currency["value"] = ('AUD', 'CAD', 'CHF', 'EUR', 'GBP', 'JPY', 'USD')
    currency.current(0)
    currency.pack()

    # Types of bank to search
    Label(frame, text='Bank').pack()
    bank = Combobox(frame)
    bank["value"] = ('Vietcombank', 'Vietinbank',
                     'Techcombank', 'BIDV', 'Sacombank', 'SBV')
    bank.current(0)
    bank.pack()

    # Result of search
    Label(frame, text="Result: ").pack()
    entry_result = Entry(frame, width=20)
    btn = Button(frame, text="Search",
                 command=lambda: outputResult(entry_result, currency.get(), bank.get()))
    btn.pack()
    entry_result.pack()
    entry_result.configure(text=currency.get())

    # Exit button
    Button(frame, text="Exit", command=lambda: endClient(client)).pack()

    return frame


def login(client):
    frame = Frame(client)
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
           command=lambda: changeFrameFromLoginToSearch(client, entry_username.get(), entry_password.get(), alert_lbl)).pack()

    return frame


def signUp(client):
    frame = Frame(client)
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
           command=lambda: changeFrameFromSignupToSearch(client, entry_username.get(), entry_password.get(), entry_pass_conf.get(), alert_lbl)).pack()
    Button(frame, text="Da co tai khoan",
           command=lambda: changeFrameFromSignupToLogin(client)).pack()
    return frame
# End GUI


# ----------------- main ------------------
client = Tk()

client.title("Client")
client.geometry("300x200")

signup_frame = signUp(client)
login_frame = login(client)
search_frame = search(client)
signup_frame.pack(fill="both", expand=True)

client.mainloop()
