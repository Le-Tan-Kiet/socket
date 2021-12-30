from tkinter import *
from tkinter import ttk


def SignUpPage(app):
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
    canvas.background0_img = PhotoImage(file=f"LogSignImg/background0.png")
    canvas.create_image(
        0, 0, anchor=NW,
        image=canvas.background0_img)
    # username
    canvas.entrySigUpUser_img = PhotoImage(file=f"LogSignImg/img_textBox0.png")
    canvas.create_image(
        600, 211, anchor=NW,
        image=canvas.entrySigUpUser_img)
    entrySignUpUser = Entry(frame,
                            bd=0,
                            bg="#dfdfdf",
                            highlightthickness=0)

    entrySignUpUser.place(
        x=620, y=211,
        width=255.0,
        height=43)
    # Password
    canvas.entrySignUpPass_img = PhotoImage(
        file=f"LogSignImg/img_textBox0.png")
    canvas.create_image(600, 319, anchor=NW, image=canvas.entrySignUpPass_img)

    entrySignUpPass = Entry(frame,
                            bd=0, show="*",
                            bg="#dfdfdf",
                            highlightthickness=0)

    entrySignUpPass.place(
        x=620, y=319,
        width=255.0,
        height=43)
    # Confirm Password
    canvas.entryCFSignUPPass_img = PhotoImage(
        file=f"LogSignImg/img_textBox0.png")
    canvas.create_image(
        600, 427, anchor=NW,
        image=canvas.entryCFSignUPPass_img)

    entryCFSignUPPass = Entry(frame,
                              bd=0, show="*",
                              bg="#dfdfdf",
                              highlightthickness=0)

    entryCFSignUPPass.place(
        x=620, y=427,
        width=255.0,
        height=43)
    # Notice
    LabelSignUp = Label(frame,  text="", background="red")
    LabelSignUp.place(x=600, y=141, width=300, height=25)

    # Sign Up Button
    canvas.btnSignup_img = PhotoImage(file=f"LogSignImg/signup0.png")
    btnSignUp = Button(frame, image=canvas.btnSignup_img, bd=0,
                       bg="white", command=lambda: changeFrameFromSignupToSearch(app, SearchPage, entrySignUpUser.get(), entrySignUpPass.get(), entryCFSignUPPass.get(), LabelSignUp))

    btnSignUp.place(
        x=690, y=497, anchor=NW,
        width=120,
        height=50)
    return frame


def LoginPage(app):
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
    canvas.background1_img = PhotoImage(file=f"LogSignImg/background1.png")
    canvas.create_image(
        0, 0, anchor=NW,
        image=canvas.background1_img)
    # username
    canvas.entryUser_img = PhotoImage(file=f"LogSignImg/img_textBox0.png")
    canvas.create_image(
        600, 211, anchor=NW,
        image=canvas.entryUser_img)

    entryUser = Entry(frame,
                      bd=0,
                      bg="#dfdfdf",
                      highlightthickness=0)

    entryUser.place(
        x=620, y=211,
        width=255.0,
        height=43)
    # Password
    canvas.entryPass_img = PhotoImage(file=f"LogSignImg/img_textBox0.png")
    canvas.create_image(600, 319, anchor=NW, image=canvas.entryPass_img)

    entryPass = Entry(frame,
                      bd=0, show="*",
                      bg="#dfdfdf",
                      highlightthickness=0)

    entryPass.place(
        x=620, y=319,
        width=255.0,
        height=43)

    # Notice
    LabelLogin = Label(text="", background="red")
    LabelLogin.place(x=600, y=373, width=300, height=25)
    # login Button
    canvas.btnLogin_img = PhotoImage(file=f"LogSignImg/login0.png")
    btnLogin = Button(frame, bd=0, bg="white", image=canvas.btnLogin_img,
                      command=lambda: switchFrame(app, SearchPage))

    btnLogin.place(
        x=690, y=407, anchor=NW,
        width=120,
        height=50)
    # Sign Up Button
    canvas.btnSignUp_img = PhotoImage(file=f"LogSignImg/signup1.png")
    btnSignUp = Button(frame, image=canvas.btnSignUp_img, bd=0,
                       bg="white", command=lambda: switchFrame(app, SignUpPage))

    btnSignUp.place(
        x=806, y=466, anchor=NW,
        width=110,
        height=30)
    return frame


def SearchPage(app):
    frame = Frame(app)
    canvas = Canvas(
        frame,
        bg="#99b1f6",
        height=600,
        width=1000,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    # Bachground
    canvas.backgroundSearch_img = PhotoImage(
        file=f"SearchPageImg/backgroundSearch.png")
    canvas.create_image(
        7, 23, anchor="nw",
        image=canvas.backgroundSearch_img)

    canvas.nameLabel_img = PhotoImage(file=f"SearchPageImg/img_nameLabel.png")
    canvas.create_image(
        26, 85, anchor='nw',
        image=canvas.nameLabel_img)

    nameLabel = Label(frame, text="Name", justify="center", font=",25",
                      bd=0,
                      bg="#ffffff",
                      highlightthickness=0)

    nameLabel.place(
        x=45, y=86,
        width=260.0,
        height=38)
    # Combobox Bank
    canvas.comboboxBank_img = PhotoImage(
        file=f"SearchPageImg/img_bankSearch.png")
    canvas.create_image(
        372, 85, anchor="nw",
        image=canvas.comboboxBank_img)

    comboboxBank = ttk.Combobox(frame, background="white", justify="center")
    comboboxBank["value"] = ('Vietcombank', 'Vietinbank',
                             'Techcombank', 'BIDV', 'Sacombank', 'SBV')
    comboboxBank.current(0)
    comboboxBank.place(
        x=387, y=87,
        width=140.0,
        height=26)

    # Combobox Currency

    canvas.comboboxCurrency_img = PhotoImage(
        file=f"SearchPageImg/img_currencySearch.png")
    canvas.create_image(
        597, 85, anchor="nw",
        image=canvas.comboboxCurrency_img)

    comboboxCurrency = ttk.Combobox(
        frame, background="white", justify="center")
    comboboxCurrency["value"] = (
        'AUD', 'CAD', 'CHF', 'EUR', 'GBP', 'JPY', 'USD')
    comboboxCurrency.current(6)

    comboboxCurrency.place(
        x=612, y=86,
        width=70.0,
        height=28)

    # Result
# entry3_img = PhotoImage(file = f"img_textBox3.png")
# entry3_bg = canvas.create_image(
#     285.0, 52.0,
#     image = entry3_img)

# entry3 = Entry(
#     bd = 0,
#     bg = "#ffffff",
#     highlightthickness = 0)

# entry3.place(
#     x = -20, y = -153,
#     width = 610,
#     height = 408)

    # SearchButton
    canvas.searchButton_img = PhotoImage(
        file=f"SearchPageImg/searchButton.png")
    btnSearch = Button(frame,
                       image=canvas.searchButton_img,
                       background="#99b1f6",
                       borderwidth=0,
                       highlightthickness=0,
                       relief="flat")

    btnSearch.place(
        x=766, y=85,
        width=100,
        height=30)
    # Reset Button
    canvas.btnRS_img = PhotoImage(file=f"SearchPageImg/resetButton.png")
    btnRS = Button(
        image=canvas.btnRS_img,
        background="#99b1f6",
        borderwidth=0,
        highlightthickness=0,
        relief="flat")

    btnRS.place(
        x=878, y=85,
        width=100,
        height=30)
    # Back button
    canvas.backButton_img = PhotoImage(file=f"SearchPageImg/backButton.png")
    btnBack = Button(
        image=canvas.backButton_img,
        background="#99b1f6",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switchFrame(app, LoginPage),
        relief="flat")

    btnBack.place(
        x=872, y=17,
        width=106,
        height=45)
    return frame


def switchFrame(app, nextFrame):
    newFrame = nextFrame(app)
    if app.currentFrame is not None:
        app.currentFrame.destroy()
    app.currentFrame = newFrame
    app.currentFrame.pack(fill="both", expand=True)


# Init window
# app = Tk()
# app.title("Currency App")
# app.geometry("1000x600")
# app.configure(bg="white")
# app.resizable(width=False, height=False)
# app.currentFrame = None
# switchFrame(app, LoginPage)
# app.mainloop()
