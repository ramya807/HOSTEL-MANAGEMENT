from tkinter import *

import pyttsx3
from PIL import ImageTk

engine = pyttsx3.init()


def func_for_file1():
    from PIL import ImageTk, Image
    roota = Tk()
    roota.title("GIRLS HOSTEL MANAGEMENT")  # Title of the application
    roota.geometry('500x500+400+100')  # Size of the screen

    image = Image.open(
        "C:\\Users\hp\Desktop\\Campus View of Birla Institute of Technology Extension Centre Deoghar_Campus-View.jpg")
    # Resize the image using resize() method
    resize_image = image.resize((1000, 500))
    img = ImageTk.PhotoImage(resize_image)
    # create label and add resize image
    label1 = Label(image=img)
    label1.image = img
    label1.pack()

    Label(text='BIT GIRLS HOSTEL MANAGEMENT', fg='red', font=44).pack()  # text size and color of the topic

    Chooser = Menu()  # chooser is used for menubar
    itemone = Menu()  # itemone is display for the topics which comes under the my-profile
    itemone.add_command(label='LOGIN', command=func_for_file2)  # topic one under my-profile

    itemtwo = Menu()  # itemtwo is display for the topics which comes under the users
    itemtwo.add_command(label='STUDENT CONTACT SYSTEM', command=func_for_file3)
    itemtwo.add_command(label='PARENT CONTACT SYSTEM', command=func_for_file13)

    itemthree = Menu()  # itemthree is display for the topics which comes under the hostels
    itemthree.add_command(label='STUDENT RECORD', command=func_for_file4)
    itemthree.add_command(label='STAFF RECORD', command=func_for_file5)

    itemfour = Menu()  # itemfour is display for the topics which comes under the warden
    itemfour.add_command(label='GENERATE BILL', command=func_for_file6)
    itemfour.add_command(label='MESS STARTERS', command=func_for_file15)

    itemfive = Menu()  # itemfive is display for the topics which comes under the payment list
    itemfive.add_command(label='CHAT BOX', command=func_for_file7)
    itemfive.add_command(label='TO-DO-LIST', command=func_for_file11)
    itemfive.add_command(label='CLANDER', command=func_for_file12)

    itemsix = Menu()  # itemsix is display for the topics which comes under the room list
    itemsix.add_command(label='RULES AND REGULATIONS', command=func_for_file8)

    itemseven = Menu()  # itemsix is display for the topics which comes under the room list
    itemseven.add_command(label='ROOM DETAILS', command=func_for_file9)
    itemseven.add_command(label='SEARCH ROOM', command=func_for_file10)

    itemeight = Menu()  # itemsix is display for the topics which comes under the room list
    itemeight.add_command(label='ADDRESS', command=func_for_file14)



    # Used to view in screen all the labels in menubar
    Chooser.add_cascade(label='MY PROFILE', menu=itemone)
    Chooser.add_cascade(label='CONTACT', menu=itemtwo)
    Chooser.add_cascade(label='RECORD', menu=itemthree)
    Chooser.add_cascade(label='BILL', menu=itemfour)
    Chooser.add_cascade(label='CHAT', menu=itemfive)
    Chooser.add_cascade(label='RULES', menu=itemsix)
    Chooser.add_cascade(label='ROOM', menu=itemseven)
    Chooser.add_cascade(label='ADDRESS BOOK', menu=itemeight)
    roota.config(menu=Chooser)
    roota.mainloop()


engine.say('GIRLS HOSTEL MANAGEMENT APPLICATION')
engine.runAndWait()

def func_for_file2():

    import tkinter.messagebox as tkMessageBox
    import sqlite3
    root = Tk()
    root.title("Login")

    width = 640
    height = 480
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    # =======================================VARIABLES=====================================
    USERNAME = StringVar()
    PASSWORD = StringVar()
    FIRSTNAME = StringVar()
    LASTNAME = StringVar()

    # =======================================METHODS=======================================
    def Database():
        global conn, cursor
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, firstname TEXT, lastname TEXT)")

    def LOGOUT():
        result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            root.destroy()
            exit()

    def LoginForm():
        global LoginFrame, lbl_result1
        LoginFrame = Frame(root)
        LoginFrame.pack(side=TOP, pady=80)
        lbl_username = Label(LoginFrame, text="Username:", font=('arial', 25), bd=18)
        lbl_username.grid(row=1)
        lbl_password = Label(LoginFrame, text="Password:", font=('arial', 25), bd=18)
        lbl_password.grid(row=2)
        lbl_result1 = Label(LoginFrame, text="", font=('arial', 18))
        lbl_result1.grid(row=3, columnspan=2)
        username = Entry(LoginFrame, font=('arial', 20), textvariable=USERNAME, width=15)
        username.grid(row=1, column=1)
        password = Entry(LoginFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
        password.grid(row=2, column=1)
        btn_login = Button(LoginFrame, text="LOGIN", font=('arial', 18), width=35, command=Login)
        btn_login.grid(row=4, columnspan=2, pady=20)
        lbl_register = Label(LoginFrame, text="Register", fg="Blue", font=('arial', 12))
        lbl_register.grid(row=0, sticky=W)
        lbl_register.bind('<Button-1>', ToggleToRegister)

    def RegisterForm():
        global RegisterFrame, lbl_result2
        RegisterFrame = Frame(root)
        RegisterFrame.pack(side=TOP, pady=40)
        lbl_username = Label(RegisterFrame, text="Username:", font=('arial', 18), bd=18)
        lbl_username.grid(row=1)
        lbl_password = Label(RegisterFrame, text="Password:", font=('arial', 18), bd=18)
        lbl_password.grid(row=2)
        lbl_firstname = Label(RegisterFrame, text="Firstname:", font=('arial', 18), bd=18)
        lbl_firstname.grid(row=3)
        lbl_lastname = Label(RegisterFrame, text="Lastname:", font=('arial', 18), bd=18)
        lbl_lastname.grid(row=4)
        lbl_result2 = Label(RegisterFrame, text="", font=('arial', 18))
        lbl_result2.grid(row=5, columnspan=2)
        username = Entry(RegisterFrame, font=('arial', 20), textvariable=USERNAME, width=15)
        username.grid(row=1, column=1)
        password = Entry(RegisterFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
        password.grid(row=2, column=1)
        firstname = Entry(RegisterFrame, font=('arial', 20), textvariable=FIRSTNAME, width=15)
        firstname.grid(row=3, column=1)
        lastname = Entry(RegisterFrame, font=('arial', 20), textvariable=LASTNAME, width=15)
        lastname.grid(row=4, column=1)
        btn_login = Button(RegisterFrame, text="Register", font=('arial', 18), width=35, command=Register)
        btn_login.grid(row=6, columnspan=2, pady=20)
        lbl_login = Label(RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
        lbl_login.grid(row=0, sticky=W)
        lbl_login.bind('<Button-1>', ToggleToLogin)

    def ToggleToLogin(event=None):
        RegisterFrame.destroy()
        LoginForm()

    def ToggleToRegister(event=None):
        LoginFrame.destroy()
        RegisterForm()

    def Register():
        Database()
        if USERNAME.get == "" or PASSWORD.get() == "" or FIRSTNAME.get() == "" or LASTNAME.get == "":
            lbl_result2.config(text="Please complete the required field!", fg="orange")
        else:
            cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (USERNAME.get(),))
            if cursor.fetchone() is not None:
                lbl_result2.config(text="Username is already taken", fg="red")
            else:
                cursor.execute("INSERT INTO `member` (username, password, firstname, lastname) VALUES(?, ?, ?, ?)",
                               (str(USERNAME.get()), str(PASSWORD.get()), str(FIRSTNAME.get()), str(LASTNAME.get())))
                conn.commit()
                USERNAME.set("")
                PASSWORD.set("")
                FIRSTNAME.set("")
                LASTNAME.set("")
                lbl_result2.config(text="Successfully Created!", fg="black")
            cursor.close()
            conn.close()

    def Login():
        Database()
        if USERNAME.get == "" or PASSWORD.get() == "":
            lbl_result1.config(text="Please complete the required field!", fg="orange")
        else:
            cursor.execute("SELECT * FROM `member` WHERE `username` = ? and `password` = ?",
                           (USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
                lbl_result1.config(text="You Successfully Login", fg="blue")
            else:
                lbl_result1.config(text="Invalid Username or password", fg="red")

    LoginForm()

    # ========================================MENUBAR WIDGETS==================================
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="LOGOUT", command=LOGOUT)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)

    # ========================================INITIALIZATION===================================
    if __name__ == '__main__':
        root.mainloop()


def func_for_file3():
    # Importing the modules
    import tkinter
    import tkinter.ttk as ttk

    import sqlite3
    import tkinter.messagebox as tkMessageBox

    root = Tk()
    root.title("Contact Management System")
    root.geometry("780x400+0+0")
    root.config(bg="Pink")

    # Variables required for storing the values
    f_name = StringVar()
    m_name = StringVar()
    l_name = StringVar()
    age = StringVar()
    home_address = StringVar()
    gender = StringVar()
    phone_number = StringVar()

    # Function for resetting the values
    def Reset():
        f_name.set("")
        m_name.set("")
        l_name.set("")
        gender.set("")
        age.set("")
        home_address.set("")
        phone_number.set("")

    # For creating the database and the table
    def Database():
        connectn = sqlite3.connect("contactdata.db")
        cursor = connectn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `contactinformation` (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, first_name TEXT, middle_name TEXT, last_name TEXT, gender TEXT, age TEXT, home_address TEXT, phone_number TEXT)")
        cursor.execute("SELECT * FROM `contactinformation` ORDER BY `last_name` ASC")
        fetchinfo = cursor.fetchall()
        for data in fetchinfo:
            tree.insert('', 'end', values=(data))
        cursor.close()
        connectn.close()

    # Function for exiting the system
    def Exit():
        O = tkinter.messagebox.askyesno("Contact Management System", "Do you want to exit the system")
        if O > 0:
            root.destroy()
        return

    # Insert query for inserting the value in database Table
    def Submit():
        if f_name.get() == "" or m_name.get() == "" or l_name.get() == "" or gender.get() == "" or age.get() == "" or home_address.get() == "" or phone_number.get() == "":
            msgg = tkMessageBox.showwarning('', 'Please Complete All the Fields', icon="warning")
        else:
            tree.delete(*tree.get_children())
        connectn = sqlite3.connect("contactdata.db")
        cursor = connectn.cursor()

        cursor.execute(
            "INSERT INTO `contactinformation` (first_name, middle_name, last_name, gender, age, home_address, phone_number ) VALUES(?, ?, ?, ?, ?, ?, ?)",
            (str(f_name.get()), str(m_name.get()), str(l_name.get()), str(gender.get()), int(age.get()),
             str(home_address.get()),
             int(phone_number.get())))

        connectn.commit()
        cursor.execute("SELECT * FROM `contactinformation` ORDER BY `last_name` ASC")
        fetchinfo = cursor.fetchall()

        for data in fetchinfo:
            tree.insert('', 'end', values=(data))
        cursor.close()
        connectn.close()
        f_name.set("")
        m_name.set("")
        l_name.set("")
        gender.set("")
        age.set("")
        home_address.set("")
        phone_number.set("")

    # Update Query for updating the table in the database
    def Update():
        if gender.get() == "":
            msgg = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
        else:
            tree.delete(*tree.get_children())
        connectn = sqlite3.connect("contactdata.db")
        cursor = connectn.cursor()
        cursor.execute(
            "UPDATE `contactinformation` SET `first_name` = ?, `middle_name` = ? , `last_name` = ?, `gender` =?, `age` = ?, `home_address` = ?, `phone_number` = ? WHERE `id` = ?",
            (str(f_name.get()), str(m_name.get()), str(l_name.get()), str(gender.get()), int(age.get()),
             str(home_address.get()),
             str(phone_number.get()), int(id)))
        connectn.commit()
        cursor.execute("SELECT * FROM `contactinformation` ORDER BY `last_name` ASC")
        fetchinfo = cursor.fetchall()
        for data in fetchinfo:
            tree.insert('', 'end', values=(data))
        gender1 = gender.get()
        if not gender1:
            tkMessageBox.showerror("Please select the gender")

        cursor.close()
        connectn.close()

        f_name.set("")
        m_name.set("")
        l_name.set("")
        gender.set("")
        age.set("")
        home_address.set("")
        phone_number.set("")

    # Module for the update contact form window
    def UpdateContact(event):
        global id, UpdateWindow
        curItem = tree.focus()
        contents = (tree.item(curItem))
        item = contents['values']
        id = item[0]
        f_name.set("")
        m_name.set("")
        l_name.set("")
        gender.set("")
        age.set("")
        home_address.set("")
        phone_number.set("")

        f_name.set(item[1])
        m_name.set(item[2])
        l_name.set(item[3])

        age.set(item[5])
        home_address.set(item[6])
        phone_number.set(item[7])

        UpdateWindow = Toplevel()
        UpdateWindow.title("Contact Information")
        UpdateWindow.geometry("500x520+0+0")
        UpdateWindow.resizable(0, 0)
        if 'Opennewwindow' in globals():
            Opennewwindow.destroy()

        # FRAMES
        # module is for the frame, labels, text entry, and button for update contact form window
        FormTitle = Frame(UpdateWindow)
        FormTitle.pack(side=TOP)
        ContactForm = Frame(UpdateWindow)
        ContactForm.pack(side=TOP, pady=10)
        RadioGroup = Frame(ContactForm)
        Male = Radiobutton(RadioGroup, text="Male", variable=gender, value="Male", font=('arial', 14)).pack(side=LEFT)
        Female = Radiobutton(RadioGroup, text="Female", variable=gender, value="Female", font=('arial', 14)).pack(
            side=LEFT)

        # LABELS
        label_title = Label(FormTitle, text="Update the Contact Information", font=('Arial', 17), bg="light green",
                            width=400)
        label_title.pack(fill=X)
        label_FirstName = Label(ContactForm, text="First Name", font=('Calibri', 14), bd=5)
        label_FirstName.grid(row=0, sticky=W)

        label_MiddleName = Label(ContactForm, text="Middle Name", font=('Calibri', 14), bd=5)
        label_MiddleName.grid(row=1, sticky=W)

        label_LastName = Label(ContactForm, text="Last Name", font=('Calibri', 14), bd=5)
        label_LastName.grid(row=2, sticky=W)

        label_Gender = Label(ContactForm, text="Gender", font=('Calibri', 14), bd=5)
        label_Gender.grid(row=3, sticky=W)

        label_Age = Label(ContactForm, text="Age", font=('Calibri', 14), bd=5)
        label_Age.grid(row=4, sticky=W)

        label_HomeAddress = Label(ContactForm, text=" Home Address", font=('Calibri', 14), bd=5)
        label_HomeAddress.grid(row=5, sticky=W)

        label_PhoneNumber = Label(ContactForm, text="Phone Number", font=('Calibri', 14), bd=5)
        label_PhoneNumber.grid(row=6, sticky=W)

        # TEXT ENTRY
        FirstName = Entry(ContactForm, textvariable=f_name, font=('Calibri', 14, 'bold'), bd=2, width=20,
                          justify='left')
        FirstName.grid(row=0, column=1)

        MiddleName = Entry(ContactForm, textvariable=m_name, font=('Calibri', 14, 'bold'), bd=2, width=20,
                           justify='left')
        MiddleName.grid(row=1, column=1)

        LastName = Entry(ContactForm, textvariable=l_name, font=('Calibri', 14, 'bold'), bd=2, width=20, justify='left')
        LastName.grid(row=2, column=1)

        RadioGroup.grid(row=3, column=1)

        Age = Entry(ContactForm, textvariable=age, font=('Calibri', 14, 'bold'), bd=2, width=20, justify='left')
        Age.grid(row=4, column=1)

        HomeAddress = Entry(ContactForm, textvariable=home_address, font=('Calibri', 14, 'bold'), bd=2, width=20,
                            justify='left')
        HomeAddress.grid(row=5, column=1)

        PhoneNumber = Entry(ContactForm, textvariable=phone_number, font=('Calibri', 14, 'bold'), bd=2, width=20,
                            justify='left')
        PhoneNumber.grid(row=6, column=1)

        #  Buttons
        ButtonUpdatContact = Button(ContactForm, text='Update', bd=2, font=('Calibri', 14, 'bold'), fg="black",
                                    bg="lightgreen", command=Update)
        ButtonUpdatContact.grid(row=8, columnspan=2, pady=10)

    # Delete query for deleting the value
    def Delete():
        if not tree.selection():
            msgg = tkMessageBox.showwarning('', 'Please Select the data!', icon="warning")
        else:
            msgg = tkMessageBox.askquestion('', 'Are You Sure You Want To Delete', icon="warning")
        if msgg == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            item = contents['values']
            tree.delete(curItem)
        connectn = sqlite3.connect("contactdata.db")
        cursor = connectn.cursor()
        cursor.execute("DELETE FROM `contactinformation` WHERE `id` = %d" % item[0])
        connectn.commit()
        cursor.close()
        connectn.close()

    # For creating the frame, labels, text entry, and button for add new contact form window
    def MyNewContact():
        global opennewwindow
        f_name.set("")
        m_name.set("")
        l_name.set("")
        gender.set("")
        age.set("")
        home_address.set("")
        phone_number.set("")

        Opennewwindow = Toplevel()
        Opennewwindow.title("Contact Details")
        Opennewwindow.resizable(0, 0)
        Opennewwindow.geometry("500x500+0+0")
        if 'UpdateWindow' in globals():
            UpdateWindow.destroy()

        #############Frames####################
        FormTitle = Frame(Opennewwindow)
        FormTitle.pack(side=TOP)
        ContactForm = Frame(Opennewwindow)
        ContactForm.pack(side=TOP, pady=10)
        RadioGroup = Frame(ContactForm)
        Male = Radiobutton(RadioGroup, text="Male", variable=gender, value="Male", font=('Calibri', 14)).pack(side=LEFT)
        Female = Radiobutton(RadioGroup, text="Female", variable=gender, value="Female", font=('Calibri', 14)).pack(
            side=LEFT)
        # ===================LABELS==============================
        label_title = Label(FormTitle, text="Adding New Contacts", bd=12, fg="black", bg="Lightgreen",
                            font=("Calibri", 15, "bold"), pady=2)
        label_title.pack(fill=X)
        label_FirstName = Label(ContactForm, text="First Name", font=('Calibri', 14), bd=5)
        label_FirstName.grid(row=0, sticky=W)

        label_MiddleName = Label(ContactForm, text="Middle Name", font=('Calibri', 14), bd=5)
        label_MiddleName.grid(row=1, sticky=W)

        label_LastName = Label(ContactForm, text="Last Name", font=('Calibri', 14), bd=5)
        label_LastName.grid(row=2, sticky=W)

        label_Gender = Label(ContactForm, text="Gender", font=('Calibri', 14), bd=5)
        label_Gender.grid(row=3, sticky=W)

        label_Age = Label(ContactForm, text="Age", font=('Calibri', 14), bd=5)
        label_Age.grid(row=4, sticky=W)

        label_HomeAddress = Label(ContactForm, text="Home Address", font=('Calibri', 14), bd=5)
        label_HomeAddress.grid(row=5, sticky=W)

        label_PhoneNumber = Label(ContactForm, text="Phone Number", font=('Calibri', 14), bd=5)
        label_PhoneNumber.grid(row=6, sticky=W)

        # ===================ENTRY===============================
        FirstName = Entry(ContactForm, textvariable=f_name, font=('Calibri', 14, 'bold'), bd=3, width=20,
                          justify='left')
        FirstName.grid(row=0, column=1)

        MiddleName = Entry(ContactForm, textvariable=m_name, font=('Calibri', 14, 'bold'), bd=3, width=20,
                           justify='left')
        MiddleName.grid(row=1, column=1)

        LastName = Entry(ContactForm, textvariable=l_name, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
        LastName.grid(row=2, column=1)

        RadioGroup.grid(row=3, column=1)

        Age = Entry(ContactForm, textvariable=age, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
        Age.grid(row=4, column=1)

        HomeAddress = Entry(ContactForm, textvariable=home_address, font=('Calibri', 14, 'bold'), bd=3, width=20,
                            justify='left')
        HomeAddress.grid(row=5, column=1)

        PhoneNumber = Entry(ContactForm, textvariable=phone_number, font=('Calibri', 14, 'bold'), bd=3, width=20,
                            justify='left')
        PhoneNumber.grid(row=6, column=1)

        # ==================BUTTONS==============================
        ButtonAddContact = Button(ContactForm, text='Please Save', bd=5, font=('Calibri', 12, 'bold'), fg="black",
                                  bg="lightgreen", command=Submit)
        ButtonAddContact.grid(row=7, columnspan=2, pady=10)

    # module for whole frame window, labels and button of contact management system
    # ============================FRAMES======================================
    Top = Frame(root, width=600, bd=1)
    Top.pack(side=TOP)
    M = Frame(root, width=650, bg="pink")
    M.pack(side=BOTTOM)
    F = Frame(width=7, height=8, bd=10, bg="pink")
    F.pack(side=BOTTOM)
    MR = Frame(M, width=100)  # Right Middle frame
    MR.pack(side=RIGHT, pady=10)
    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)

    # LABELS
    label_title = Label(Top, text="Contact System", bd=7, relief=GROOVE, fg="Black", bg="lightgreen",
                        font=("Calibri", 25, "bold"), pady=3)
    label_title.pack(fill=X)

    # BUTTONS
    Add_Button = Button(F, text='Add New Contact', font=('Calibri', 17, 'bold'), fg="black",
                        bg="lightgreen", command=MyNewContact).grid(row=0, column=0, ipadx=20, padx=30)

    Delete_Button = Button(F, text='Delete The Contact', font=('Calibri', 17, 'bold'), command=Delete,
                           fg="black", bg="lightgreen").grid(row=0, column=1, ipadx=20)

    Exit_Button = Button(F, text='Exit System', font=('Calibri', 17, 'bold'), command=Exit,
                         fg="black", bg="lightgreen").grid(row=0, column=2, ipadx=20, padx=30)

    # creating a tables in contact management system
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=(
    "Id", "First Name", "Middle Name", "Last Name", "Gender", "Age", "Home Address", "Phone Number"),
                        height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('Id', text="Id", anchor=W)
    tree.heading('First Name', text="First Name", anchor=W)
    tree.heading('Middle Name', text="Middle Name", anchor=W)
    tree.heading('Last Name', text="Last Name", anchor=W)
    tree.heading('Gender', text="Gender", anchor=W)
    tree.heading('Age', text="Age", anchor=W)
    tree.heading('Home Address', text="Home Address", anchor=W)
    tree.heading('Phone Number', text="phone Number", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=80)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=90)
    tree.column('#5', stretch=NO, minwidth=0, width=80)
    tree.column('#6', stretch=NO, minwidth=0, width=30)
    tree.column('#7', stretch=NO, minwidth=0, width=120)

    tree.pack()
    tree.bind('<Double-Button-1>', UpdateContact)

    # ============================INITIALIZATION==============================
    if __name__ == '__main__':
        Database()
    root.mainloop()


def func_for_file4():
    import datetime

    import tkinter.messagebox as mb
    from tkinter import ttk
    from typing import Any, Literal

    from tkcalendar import DateEntry  # pip install tkcalendar
    import sqlite3

    # Creating the universal font variables
    headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
    labelfont = ('Garamond', 14)
    entryfont = ('Garamond', 12)
    # Connecting to the Database where all information will be stored
    connector = sqlite3.connect('HostelManagement.db')
    cursor = connector.cursor()
    connector.execute(
        "CREATE TABLE IF NOT EXISTS HOSTEL_MANAGEMENT (STUDENT_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NAME TEXT, "
        "EMAIL TEXT, PHONE_NO TEXT, GENDER TEXT, DOB TEXT, STREAM TEXT) "
    )

    # Creating the functions
    def reset_fields():
        global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, stream_strvar
        for i in ['name_strvar', 'email_strvar', 'contact_strvar', 'gender_strvar', 'stream_strvar']:
            exec(f"{i}.set('')")
        dob.set_date(datetime.datetime.now().date())

    def reset_form():
        global tree
        tree.delete(*tree.get_children())
        reset_fields()

    def display_records():
        tree.delete(*tree.get_children())
        curr = connector.execute('SELECT * FROM HOSTEL_MANAGEMENT')
        data = curr.fetchall()
        for records in data:
            tree.insert('', END, values=records)

    def add_record():
        global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, stream_strvar
        name = name_strvar.get()
        email = email_strvar.get()
        contact = contact_strvar.get()
        gender = gender_strvar.get()
        DOB = dob.get_date()
        stream = stream_strvar.get()
        if not name or not email or not contact or not gender or not DOB or not stream:
            mb.showerror('Error!', "Please fill all the missing fields!!")
        else:
            try:
                connector.execute(
                    'INSERT INTO HOSTEL_MANAGEMENT (NAME, EMAIL, PHONE_NO, GENDER, DOB, STREAM) VALUES (?,?,?,?,?,?)',
                    (name, email, contact, gender, DOB, stream)
                )
                connector.commit()
                mb.showinfo('Record added', f"Record of {name} was successfully added")
                reset_fields()
                display_records()
            finally:
                mb.showerror('Wrong type', 'The type of the values entered is not accurate. Pls note that the contact '
                                           'field can only ''contain numbers')

    def remove_record():
        if not tree.selection():
            mb.showerror('Error!', 'Please select an item from the database')
        else:
            current_item = tree.focus()
            values = tree.item(current_item)
            selection = values["values"]
            tree.delete(current_item)
            connector.execute('DELETE FROM HOSTEL_MANAGEMENT WHERE STUDENT_ID=%d')
            connector.commit()
            mb.showinfo('Done', 'The record you wanted deleted was successfully deleted.')
            display_records()

    def view_record():
        global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, stream_strvar
        if not tree.selection():
            mb.showerror('Error!', 'Please select a record to view')
        else:
            current_item = tree.focus()
            values = tree.item(current_item)
            selection: str | list[str] | Literal[""] | list[Any] | bool = values["values"]

            name_strvar.set(selection[1])
            email_strvar.set(selection[2])
            contact_strvar.set(selection[3])
            gender_strvar.set(selection[4])
            date = datetime.date(int(selection[5][:4]), int(selection[5][5:7]), int(selection[5][8:]))
            dob.set_date(date)
            stream_strvar.set(selection[6])

    # Initializing the GUI window
    main = Tk()
    main.title('DataFlair Hostel Management System')
    main.geometry('1250x600')
    # Creating the background and foreground color variables
    lf_bg = 'MediumSpringGreen'  # bg color for the left_frame
    cf_bg = 'PaleGreen'  # bg color for the center_frame
    # Creating the StringVar or IntVar variables
    name_strvar = StringVar()
    email_strvar = StringVar()
    contact_strvar = StringVar()
    gender_strvar = StringVar()
    stream_strvar = StringVar()
    # Placing the components in the main window
    Label(main, text="HOSTEL MANAGEMENT SYSTEM", font=headlabelfont, bg='SpringGreen').pack(side=TOP, fill=X)
    left_frame = Frame(main, bg=lf_bg)
    left_frame.place(x=0, y=30, relheight=1, relwidth=0.2)
    center_frame = Frame(main, bg=cf_bg)
    center_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.2)
    right_frame = Frame(main, bg="Gray35")
    right_frame.place(relx=0.4, y=30, relheight=1, relwidth=0.6)
    # Placing components in the left frame
    Label(left_frame, text="Name", font=labelfont, bg=lf_bg).place(relx=0.375, rely=0.05)
    Label(left_frame, text="Contact Number", font=labelfont, bg=lf_bg).place(relx=0.175, rely=0.18)
    Label(left_frame, text="Email Address", font=labelfont, bg=lf_bg).place(relx=0.2, rely=0.31)
    Label(left_frame, text="Gender", font=labelfont, bg=lf_bg).place(relx=0.3, rely=0.44)
    Label(left_frame, text="Date of Birth (DOB)", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.57)
    Label(left_frame, text="Stream", font=labelfont, bg=lf_bg).place(relx=0.3, rely=0.7)
    Entry(left_frame, width=19, textvariable=name_strvar, font=entryfont).place(x=20, rely=0.1)
    Entry(left_frame, width=19, textvariable=contact_strvar, font=entryfont).place(x=20, rely=0.23)
    Entry(left_frame, width=19, textvariable=email_strvar, font=entryfont).place(x=20, rely=0.36)
    Entry(left_frame, width=19, textvariable=stream_strvar, font=entryfont).place(x=20, rely=0.75)
    OptionMenu(left_frame, gender_strvar, 'Male', "Female").place(x=45, rely=0.49, relwidth=0.5)
    dob = DateEntry(left_frame, font=("Arial", 12), width=15)
    dob.place(x=20, rely=0.62)
    Button(left_frame, text='Submit and Add Record', font=labelfont, command=add_record, width=18).place(relx=0.025,
                                                                                                         rely=0.85)
    # Placing components in the center frame
    Button(center_frame, text='Delete Record', font=labelfont, command=remove_record, width=15).place(relx=0.1,
                                                                                                      rely=0.25)
    Button(center_frame, text='View Record', font=labelfont, command=view_record, width=15).place(relx=0.1, rely=0.35)
    Button(center_frame, text='Reset Fields', font=labelfont, command=reset_fields, width=15).place(relx=0.1, rely=0.45)
    Button(center_frame, text='Delete database', font=labelfont, command=reset_form, width=15).place(relx=0.1,
                                                                                                     rely=0.55)
    # Placing components in the right frame
    Label(right_frame, text='Students Records', font=headlabelfont, bg='DarkGreen', fg='LightCyan').pack(side=TOP,
                                                                                                         fill=X)
    tree = ttk.Treeview(right_frame, height=100, selectmode=BROWSE,
                        columns=(
                            'Student ID', "Name", "Email Address", "Contact Number", "Gender", "Date of Birth",
                            "Stream"))
    X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
    Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
    X_scroller.pack(side=BOTTOM, fill=X)
    Y_scroller.pack(side=RIGHT, fill=Y)
    tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
    tree.heading('Student ID', text='ID', anchor=CENTER)
    tree.heading('Name', text='Name', anchor=CENTER)
    tree.heading('Email Address', text='Email ID', anchor=CENTER)
    tree.heading('Contact Number', text='Phone No', anchor=CENTER)
    tree.heading('Gender', text='Gender', anchor=CENTER)
    tree.heading('Date of Birth', text='DOB', anchor=CENTER)
    tree.heading('Stream', text='Stream', anchor=CENTER)
    tree.column('#0', width=0, stretch=NO)
    tree.column('#1', width=40, stretch=NO)
    tree.column('#2', width=140, stretch=NO)
    tree.column('#3', width=200, stretch=NO)
    tree.column('#4', width=80, stretch=NO)
    tree.column('#5', width=80, stretch=NO)
    tree.column('#6', width=80, stretch=NO)
    tree.column('#7', width=150, stretch=NO)
    tree.place(y=30, relwidth=1, relheight=0.9, relx=0)
    display_records()

    # Finalizing the GUI window
    main.update()
    main.mainloop()


def func_for_file5():
    # Importing the modules
    import tkinter
    import tkinter.ttk as ttk

    import sqlite3
    import tkinter.messagebox as tkMessageBox

    root = Tk()
    root.title("Staff Contact Management System")
    root.geometry("780x400+0+0")
    root.config(bg="light blue")

    # Variables required for storing the values
    f_name = StringVar()
    m_name = StringVar()
    l_name = StringVar()
    age = StringVar()
    home_address = StringVar()
    gender = StringVar()
    phone_number = StringVar()

    # Function for resetting the values
    def Reset():
        f_name.set("")
        m_name.set("")
        l_name.set("")
        gender.set("")
        age.set("")
        home_address.set("")
        phone_number.set("")

    # For creating the database and the table
    def Database():
        connectnn = sqlite3.connect("contactdataa.db")
        cursor = connectnn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `contactinformationn` (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, first_name TEXT, middle_name TEXT, last_name TEXT, gender TEXT, age TEXT, home_address TEXT, phone_number TEXT)")
        cursor.execute("SELECT * FROM `contactinformationn` ORDER BY `last_name` ASC")
        fetchinfo = cursor.fetchall()
        for data in fetchinfo:
            tree.insert('', 'end', values=(data))
        cursor.close()
        connectnn.close()

    # Function for exiting the system
    def Exit():
        O = tkinter.messagebox.askyesno("Contact Management System", "Do you want to exit the system")
        if O > 0:
            root.destroy()
        return

    # Insert query for inserting the value in database Table
    def Submit():
        if f_name.get() == "" or m_name.get() == "" or l_name.get() == "" or gender.get() == "" or age.get() == "" or home_address.get() == "" or phone_number.get() == "":
            msgg = tkMessageBox.showwarning('', 'Please Complete All the Fields', icon="warning")
        else:
            tree.delete(*tree.get_children())
        connectnn = sqlite3.connect("contactdataa.db")
        cursor = connectnn.cursor()

        cursor.execute(
            "INSERT INTO `contactinformationn` (first_name, middle_name, last_name, gender, age, home_address, phone_number ) VALUES(?, ?, ?, ?, ?, ?, ?)",
            (str(f_name.get()), str(m_name.get()), str(l_name.get()), str(gender.get()), int(age.get()),
             str(home_address.get()),
             int(phone_number.get())))

        connectnn.commit()
        cursor.execute("SELECT * FROM `contactinformationn` ORDER BY `last_name` ASC")
        fetchinfo = cursor.fetchall()

        for data in fetchinfo:
            tree.insert('', 'end', values=(data))
        cursor.close()
        connectnn.close()
        f_name.set("")
        m_name.set("")
        l_name.set("")
        gender.set("")
        age.set("")
        home_address.set("")
        phone_number.set("")

    # Update Query for updating the table in the database
    def Update():
        if gender.get() == "":
            msgg = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
        else:
            tree.delete(*tree.get_children())
        connectnn = sqlite3.connect("contactdataa.db")
        cursor = connectnn.cursor()
        cursor.execute(
            "UPDATE `contactinformation` SET `first_name` = ?, `middle_name` = ? , `last_name` = ?, `gender` =?, `age` = ?, `home_address` = ?, `phone_number` = ? WHERE `id` = ?",
            (str(f_name.get()), str(m_name.get()), str(l_name.get()), str(gender.get()), int(age.get()),
             str(home_address.get()),
             str(phone_number.get()), int(id)))
        connectnn.commit()
        cursor.execute("SELECT * FROM `contactinformationn` ORDER BY `last_name` ASC")
        fetchinfo = cursor.fetchall()
        for data in fetchinfo:
            tree.insert('', 'end', values=(data))
        gender1 = gender.get()
        if not gender1:
            tkMessageBox.showerror("Please select the gender")

        cursor.close()
        connectnn.close()

        f_name.set("")
        m_name.set("")
        l_name.set("")
        gender.set("")
        age.set("")
        home_address.set("")
        phone_number.set("")

    # Module for the update contact form window
    def UpdateContact(event):
        global id, UpdateWindow
        curItem = tree.focus()
        contents = (tree.item(curItem))
        item = contents['values']
        id = item[0]
        f_name.set("")
        m_name.set("")
        l_name.set("")
        gender.set("")
        age.set("")
        home_address.set("")
        phone_number.set("")

        f_name.set(item[1])
        m_name.set(item[2])
        l_name.set(item[3])

        age.set(item[5])
        home_address.set(item[6])
        phone_number.set(item[7])

        UpdateWindow = Toplevel()
        UpdateWindow.title("Staff Contact Information")
        UpdateWindow.geometry("500x520+0+0")
        UpdateWindow.resizable(0, 0)
        if 'Opennewwindow' in globals():
            Opennewwindow.destroy()

        # FRAMES
        # module is for the frame, labels, text entry, and button for update contact form window
        FormTitle = Frame(UpdateWindow)
        FormTitle.pack(side=TOP)
        ContactForm = Frame(UpdateWindow)
        ContactForm.pack(side=TOP, pady=10)
        RadioGroup = Frame(ContactForm)
        Male = Radiobutton(RadioGroup, text="Male", variable=gender, value="Male", font=('arial', 14)).pack(side=LEFT)
        Female = Radiobutton(RadioGroup, text="Female", variable=gender, value="Female", font=('arial', 14)).pack(
            side=LEFT)

        # LABELS
        label_title = Label(FormTitle, text="Update the Contact Informationn", font=('Arial', 17), bg="light green",
                            width=400)
        label_title.pack(fill=X)
        label_FirstName = Label(ContactForm, text="First Name", font=('Calibri', 14), bd=5)
        label_FirstName.grid(row=0, sticky=W)

        label_MiddleName = Label(ContactForm, text="Middle Name", font=('Calibri', 14), bd=5)
        label_MiddleName.grid(row=1, sticky=W)

        label_LastName = Label(ContactForm, text="Last Name", font=('Calibri', 14), bd=5)
        label_LastName.grid(row=2, sticky=W)

        label_Gender = Label(ContactForm, text="Gender", font=('Calibri', 14), bd=5)
        label_Gender.grid(row=3, sticky=W)

        label_Age = Label(ContactForm, text="Age", font=('Calibri', 14), bd=5)
        label_Age.grid(row=4, sticky=W)

        label_HomeAddress = Label(ContactForm, text=" Home Address", font=('Calibri', 14), bd=5)
        label_HomeAddress.grid(row=5, sticky=W)

        label_PhoneNumber = Label(ContactForm, text="Phone Number", font=('Calibri', 14), bd=5)
        label_PhoneNumber.grid(row=6, sticky=W)

        # TEXT ENTRY
        FirstName = Entry(ContactForm, textvariable=f_name, font=('Calibri', 14, 'bold'), bd=2, width=20,
                          justify='left')
        FirstName.grid(row=0, column=1)

        MiddleName = Entry(ContactForm, textvariable=m_name, font=('Calibri', 14, 'bold'), bd=2, width=20,
                           justify='left')
        MiddleName.grid(row=1, column=1)

        LastName = Entry(ContactForm, textvariable=l_name, font=('Calibri', 14, 'bold'), bd=2, width=20, justify='left')
        LastName.grid(row=2, column=1)

        RadioGroup.grid(row=3, column=1)

        Age = Entry(ContactForm, textvariable=age, font=('Calibri', 14, 'bold'), bd=2, width=20, justify='left')
        Age.grid(row=4, column=1)

        HomeAddress = Entry(ContactForm, textvariable=home_address, font=('Calibri', 14, 'bold'), bd=2, width=20,
                            justify='left')
        HomeAddress.grid(row=5, column=1)

        PhoneNumber = Entry(ContactForm, textvariable=phone_number, font=('Calibri', 14, 'bold'), bd=2, width=20,
                            justify='left')
        PhoneNumber.grid(row=6, column=1)

        #  Buttons
        ButtonUpdatContact = Button(ContactForm, text='Update', bd=2, font=('Calibri', 14, 'bold'), fg="black",
                                    bg="lightgreen", command=Update)
        ButtonUpdatContact.grid(row=8, columnspan=2, pady=10)

    # Delete query for deleting the value
    def Delete():
        if not tree.selection():
            msgg = tkMessageBox.showwarning('', 'Please Select the data!', icon="warning")
        else:
            msgg = tkMessageBox.askquestion('', 'Are You Sure You Want To Delete', icon="warning")
        if msgg == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            item = contents['values']
            tree.delete(curItem)
        connectnn = sqlite3.connect("contactdataa.db")
        cursor = connectnn.cursor()
        cursor.execute("DELETE FROM `contactinformationn` WHERE `id` = %d" % item[0])
        connectnn.commit()
        cursor.close()
        connectnn.close()

    # For creating the frame, labels, text entry, and button for add new contact form window
    def MyNewContact():
        global opennewwindow
        f_name.set("")
        m_name.set("")
        l_name.set("")
        gender.set("")
        age.set("")
        home_address.set("")
        phone_number.set("")

        Opennewwindow = Toplevel()
        Opennewwindow.title("Staff Contact Details")
        Opennewwindow.resizable(0, 0)
        Opennewwindow.geometry("500x500+0+0")
        if 'UpdateWindow' in globals():
            UpdateWindow.destroy()

        #############Frames####################
        FormTitle = Frame(Opennewwindow)
        FormTitle.pack(side=TOP)
        ContactForm = Frame(Opennewwindow)
        ContactForm.pack(side=TOP, pady=10)
        RadioGroup = Frame(ContactForm)
        Male = Radiobutton(RadioGroup, text="Male", variable=gender, value="Male", font=('Calibri', 14)).pack(side=LEFT)
        Female = Radiobutton(RadioGroup, text="Female", variable=gender, value="Female", font=('Calibri', 14)).pack(
            side=LEFT)
        # ===================LABELS==============================
        label_title = Label(FormTitle, text="Adding New Contacts", bd=12, fg="black", bg="Lightgreen",
                            font=("Calibri", 15, "bold"), pady=2)
        label_title.pack(fill=X)
        label_FirstName = Label(ContactForm, text="First Name", font=('Calibri', 14), bd=5)
        label_FirstName.grid(row=0, sticky=W)

        label_MiddleName = Label(ContactForm, text="Middle Name", font=('Calibri', 14), bd=5)
        label_MiddleName.grid(row=1, sticky=W)

        label_LastName = Label(ContactForm, text="Last Name", font=('Calibri', 14), bd=5)
        label_LastName.grid(row=2, sticky=W)

        label_Gender = Label(ContactForm, text="Gender", font=('Calibri', 14), bd=5)
        label_Gender.grid(row=3, sticky=W)

        label_Age = Label(ContactForm, text="Age", font=('Calibri', 14), bd=5)
        label_Age.grid(row=4, sticky=W)

        label_HomeAddress = Label(ContactForm, text="Home Address", font=('Calibri', 14), bd=5)
        label_HomeAddress.grid(row=5, sticky=W)

        label_PhoneNumber = Label(ContactForm, text="Phone Number", font=('Calibri', 14), bd=5)
        label_PhoneNumber.grid(row=6, sticky=W)

        # ===================ENTRY===============================
        FirstName = Entry(ContactForm, textvariable=f_name, font=('Calibri', 14, 'bold'), bd=3, width=20,
                          justify='left')
        FirstName.grid(row=0, column=1)

        MiddleName = Entry(ContactForm, textvariable=m_name, font=('Calibri', 14, 'bold'), bd=3, width=20,
                           justify='left')
        MiddleName.grid(row=1, column=1)

        LastName = Entry(ContactForm, textvariable=l_name, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
        LastName.grid(row=2, column=1)

        RadioGroup.grid(row=3, column=1)

        Age = Entry(ContactForm, textvariable=age, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
        Age.grid(row=4, column=1)

        HomeAddress = Entry(ContactForm, textvariable=home_address, font=('Calibri', 14, 'bold'), bd=3, width=20,
                            justify='left')
        HomeAddress.grid(row=5, column=1)

        PhoneNumber = Entry(ContactForm, textvariable=phone_number, font=('Calibri', 14, 'bold'), bd=3, width=20,
                            justify='left')
        PhoneNumber.grid(row=6, column=1)

        # ==================BUTTONS==============================
        ButtonAddContact = Button(ContactForm, text='Please Save', bd=5, font=('Calibri', 12, 'bold'), fg="black",
                                  bg="lightgreen", command=Submit)
        ButtonAddContact.grid(row=7, columnspan=2, pady=10)

    # module for whole frame window, labels and button of contact management system
    # ============================FRAMES======================================
    Top = Frame(root, width=600, bd=1)
    Top.pack(side=TOP)
    M = Frame(root, width=650, bg="light blue")
    M.pack(side=BOTTOM)
    F = Frame(width=7, height=8, bd=10, bg="light blue")
    F.pack(side=BOTTOM)
    MR = Frame(M, width=100)  # Right Middle frame
    MR.pack(side=RIGHT, pady=10)
    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)

    # LABELS
    label_title = Label(Top, text="Staff Contact System", bd=7, relief=GROOVE, fg="dark Blue", bg="lightgreen",
                        font=("Calibri", 25, "bold"), pady=3)
    label_title.pack(fill=X)

    # BUTTONS
    Add_Button = Button(F, text='Add New Contact', font=('Calibri', 17, 'bold'), fg="dark blue",
                        bg="lightgreen", command=MyNewContact).grid(row=0, column=0, ipadx=20, padx=30)

    Delete_Button = Button(F, text='Delete The Contact', font=('Calibri', 17, 'bold'), command=Delete,
                           fg="dark blue", bg="lightgreen").grid(row=0, column=1, ipadx=20)

    Exit_Button = Button(F, text='Exit System', font=('Calibri', 17, 'bold'), command=Exit,
                         fg="dark blue", bg="lightgreen").grid(row=0, column=2, ipadx=20, padx=30)

    # creating a tables in contact management system
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=(
    "Id", "First Name", "Middle Name", "Last Name", "Gender", "Age", "Home Address", "Phone Number"),
                        height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('Id', text="Id", anchor=W)
    tree.heading('First Name', text="First Name", anchor=W)
    tree.heading('Middle Name', text="Middle Name", anchor=W)
    tree.heading('Last Name', text="Last Name", anchor=W)
    tree.heading('Gender', text="Gender", anchor=W)
    tree.heading('Age', text="Age", anchor=W)
    tree.heading('Home Address', text="Home Address", anchor=W)
    tree.heading('Phone Number', text="phone Number", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=80)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=90)
    tree.column('#5', stretch=NO, minwidth=0, width=80)
    tree.column('#6', stretch=NO, minwidth=0, width=30)
    tree.column('#7', stretch=NO, minwidth=0, width=120)

    tree.pack()
    tree.bind('<Double-Button-1>', UpdateContact)

    # ============================INITIALIZATION==============================
    if __name__ == '__main__':
        Database()
    root.mainloop()


def func_for_file6():

    import random

    class Bill_App:
        def __init__(self, root):
            self.root = root
            self.root.geometry("1300x700+0+0")
            self.root.maxsize(width=1280, height=700)
            self.root.minsize(width=1280, height=700)
            self.root.title("MESS BILL")

            # ====================Variables========================#
            self.cus_name = StringVar()
            self.c_phone = StringVar()
            # For Generating Random Bill Numbers
            x = random.randint(1000, 9999)
            self.c_bill_no = StringVar()
            # Seting Value to variable
            self.c_bill_no.set(str(x))

            self.bath_soap = IntVar()
            self.face_cream = IntVar()
            self.face_wash = IntVar()
            self.hair_spray = IntVar()
            self.body_lotion = IntVar()
            self.rice = IntVar()
            self.daal = IntVar()
            self.food_oil = IntVar()
            self.wheat = IntVar()
            self.sugar = IntVar()
            self.maza = IntVar()
            self.coke = IntVar()
            self.frooti = IntVar()
            self.nimko = IntVar()
            self.biscuits = IntVar()
            self.total_cosmetics = StringVar()
            self.total_grocery = StringVar()
            self.total_other = StringVar()
            self.tax_cos = StringVar()
            self.tax_groc = StringVar()
            self.tax_other = StringVar()

            # ===================================
            bg_color = "#074463"
            fg_color = "YELLOW"
            lbl_color = 'WHITE'
            # Title of App
            title = Label(self.root, text="MESS BILL OF BITD", bd=12, relief=GROOVE, fg=fg_color, bg=bg_color,
                          font=("times new roman", 30, "bold"), pady=3).pack(fill=X)

            # ==========Student Details Frame==========#
            F1 = LabelFrame(text="STUDENT DETAILS", font=("time new roman", 12, "bold"), fg="gold", bg=bg_color,
                            relief=GROOVE, bd=10)
            F1.place(x=0, y=80, relwidth=1)

            # ===============Student Name===========#
            cname_lbl = Label(F1, text="Student Name", bg=bg_color, fg=fg_color,
                              font=("times new roman", 15, "bold")).grid(
                row=0, column=0, padx=10, pady=5)
            cname_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.cus_name)
            cname_en.grid(row=0, column=1, ipady=4, ipadx=30, pady=5)

            # =================Customer Phone==============#
            cphon_lbl = Label(F1, text="Phone No", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(
                row=0, column=2, padx=20)
            cphon_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_phone)
            cphon_en.grid(row=0, column=3, ipady=4, ipadx=30, pady=5)

            # ====================Customer Bill No==================#
            cbill_lbl = Label(F1, text="Bill No.", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold"))
            cbill_lbl.grid(row=0, column=4, padx=20)
            cbill_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_bill_no)
            cbill_en.grid(row=0, column=5, ipadx=30, ipady=4, pady=5)

            # ====================Bill Search Button===============#
            bill_btn = Button(F1, text="Enter", bd=7, relief=GROOVE, font=("times new roman", 12, "bold"), bg=bg_color,
                              fg=fg_color)
            bill_btn.grid(row=0, column=6, ipady=5, padx=60, ipadx=19, pady=5)

            # ==================Cosmetics Frame=====================#
            F2 = LabelFrame(self.root, text='COSMETICS', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                            font=("times new roman", 13, "bold"))
            F2.place(x=5, y=180, width=325, height=380)

            # ===========Frame Content===============#
            bath_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Bath Soap")
            bath_lbl.grid(row=0, column=0, padx=10, pady=20)
            bath_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.bath_soap)
            bath_en.grid(row=0, column=1, ipady=5, ipadx=5)

            # =======Face Cream
            face_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Face Cream")
            face_lbl.grid(row=1, column=0, padx=10, pady=20)
            face_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.face_cream)
            face_en.grid(row=1, column=1, ipady=5, ipadx=5)

            # ========Face Wash
            wash_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Face Wash")
            wash_lbl.grid(row=2, column=0, padx=10, pady=20)
            wash_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.face_wash)
            wash_en.grid(row=2, column=1, ipady=5, ipadx=5)

            # ========Hair Spray
            hair_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Hair Spray")
            hair_lbl.grid(row=3, column=0, padx=10, pady=20)
            hair_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.hair_spray)
            hair_en.grid(row=3, column=1, ipady=5, ipadx=5)

            # ============Body Lotion
            lot_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Body Lotion")
            lot_lbl.grid(row=4, column=0, padx=10, pady=20)
            lot_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.body_lotion)
            lot_en.grid(row=4, column=1, ipady=5, ipadx=5)

            # ==================Grocery Frame=====================#
            F2 = LabelFrame(self.root, text='GROCERY', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                            font=("times new roman", 13, "bold"))
            F2.place(x=330, y=180, width=325, height=380)

            # ===========Frame Content
            rice_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Rice")
            rice_lbl.grid(row=0, column=0, padx=10, pady=20)
            rice_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.rice)
            rice_en.grid(row=0, column=1, ipady=5, ipadx=5)

            # =======
            oil_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Food Oil")
            oil_lbl.grid(row=1, column=0, padx=10, pady=20)
            oil_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.food_oil)
            oil_en.grid(row=1, column=1, ipady=5, ipadx=5)

            # =======
            daal_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Daal")
            daal_lbl.grid(row=2, column=0, padx=10, pady=20)
            daal_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.daal)
            daal_en.grid(row=2, column=1, ipady=5, ipadx=5)

            # ========
            wheat_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Wheat")
            wheat_lbl.grid(row=3, column=0, padx=10, pady=20)
            wheat_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.wheat)
            wheat_en.grid(row=3, column=1, ipady=5, ipadx=5)

            # ============
            sugar_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Sugar")
            sugar_lbl.grid(row=4, column=0, padx=10, pady=20)
            sugar_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.sugar)
            sugar_en.grid(row=4, column=1, ipady=5, ipadx=5)

            # ==================Other Stuff=====================#

            F2 = LabelFrame(self.root, text='OTHERS', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                            font=("times new roman", 13, "bold"))
            F2.place(x=655, y=180, width=325, height=380)

            # ===========Frame Content
            maza_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Maza")
            maza_lbl.grid(row=0, column=0, padx=10, pady=20)
            maza_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.maza)
            maza_en.grid(row=0, column=1, ipady=5, ipadx=5)

            # =======
            cock_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Coke")
            cock_lbl.grid(row=1, column=0, padx=10, pady=20)
            cock_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.coke)
            cock_en.grid(row=1, column=1, ipady=5, ipadx=5)

            # =======
            frooti_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Frooti")
            frooti_lbl.grid(row=2, column=0, padx=10, pady=20)
            frooti_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.frooti)
            frooti_en.grid(row=2, column=1, ipady=5, ipadx=5)

            # ========
            cold_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Nimkos")
            cold_lbl.grid(row=3, column=0, padx=10, pady=20)
            cold_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.nimko)
            cold_en.grid(row=3, column=1, ipady=5, ipadx=5)

            # ============
            bis_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Biscuits")
            bis_lbl.grid(row=4, column=0, padx=10, pady=20)
            bis_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.biscuits)
            bis_en.grid(row=4, column=1, ipady=5, ipadx=5)

            # ===================Bill Aera================#
            F3 = Label(self.root, bd=10, relief=GROOVE)
            F3.place(x=960, y=180, width=325, height=380)
            # ===========
            bill_title = Label(F3, text="Bill Area", font=("Lucida", 13, "bold"), bd=7, relief=GROOVE)
            bill_title.pack(fill=X)

            # ============
            scroll_y = Scrollbar(F3, orient=VERTICAL)
            self.txt = Text(F3, yscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_y.config(command=self.txt.yview)
            self.txt.pack(fill=BOTH, expand=1)

            # ===========Buttons Frame=============#
            F4 = LabelFrame(self.root, text='BILL MENU', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                            font=("times new roman", 13, "bold"))
            F4.place(x=0, y=560, relwidth=1, height=145)

            # ===================
            cosm_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color,
                             text="Total Cosmetics")
            cosm_lbl.grid(row=0, column=0, padx=10, pady=0)
            cosm_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.total_cosmetics)
            cosm_en.grid(row=0, column=1, ipady=2, ipadx=5)

            # ===================
            gro_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Grocery")
            gro_lbl.grid(row=1, column=0, padx=10, pady=5)
            gro_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.total_grocery)
            gro_en.grid(row=1, column=1, ipady=2, ipadx=5)

            # ================
            oth_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Others Total")
            oth_lbl.grid(row=2, column=0, padx=10, pady=5)
            oth_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.total_other)
            oth_en.grid(row=2, column=1, ipady=2, ipadx=5)

            # ================
            cosmt_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Cosmetics Tax")
            cosmt_lbl.grid(row=0, column=2, padx=30, pady=0)
            cosmt_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.tax_cos)
            cosmt_en.grid(row=0, column=3, ipady=2, ipadx=5)

            # =================
            grot_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Grocery Tax")
            grot_lbl.grid(row=1, column=2, padx=30, pady=5)
            grot_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.tax_groc)
            grot_en.grid(row=1, column=3, ipady=2, ipadx=5)

            # ==================
            otht_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Others Tax")
            otht_lbl.grid(row=2, column=2, padx=10, pady=5)
            otht_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.tax_other)
            otht_en.grid(row=2, column=3, ipady=2, ipadx=5)

            # ====================
            total_btn = Button(F4, text="TOTAL", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7,
                               relief=GROOVE,
                               command=self.total)
            total_btn.grid(row=1, column=4, ipadx=20, padx=30)

            # ========================
            genbill_btn = Button(F4, text="GENERATE BILL", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7,
                                 relief=GROOVE, command=self.bill_area)
            genbill_btn.grid(row=1, column=5, ipadx=20)

            # ====================
            clear_btn = Button(F4, text="CLEAR", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7,
                               relief=GROOVE,
                               command=self.clear)
            clear_btn.grid(row=1, column=6, ipadx=20, padx=30)

            # ======================
            exit_btn = Button(F4, text="EXIT", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7,
                              relief=GROOVE,
                              command=self.exit)
            exit_btn.grid(row=1, column=7, ipadx=20)

        # Function to get total prices
        def total(self):
            # =================Total Cosmetics Prices
            self.total_cosmetics_prices = (
                    (self.bath_soap.get() * 40) +
                    (self.face_cream.get() * 140) +
                    (self.face_wash.get() * 240) +
                    (self.hair_spray.get() * 340) +
                    (self.body_lotion.get() * 260)
            )
            self.total_cosmetics.set("Rs. " + str(self.total_cosmetics_prices))
            self.tax_cos.set("Rs. " + str(round(self.total_cosmetics_prices * 0.05)))
            # ====================Total Grocery Prices
            self.total_grocery_prices = (
                    (self.wheat.get() * 100) +
                    (self.food_oil.get() * 180) +
                    (self.daal.get() * 80) +
                    (self.rice.get() * 80) +
                    (self.sugar.get() * 170)

            )
            self.total_grocery.set("Rs. " + str(self.total_grocery_prices))
            self.tax_groc.set("Rs. " + str(round(self.total_grocery_prices * 0.05)))
            # ======================Total Other Prices
            self.total_other_prices = (
                    (self.maza.get() * 20) +
                    (self.frooti.get() * 50) +
                    (self.coke.get() * 60) +
                    (self.nimko.get() * 20) +
                    (self.biscuits.get() * 20)
            )
            self.total_other.set("Rs. " + str(self.total_other_prices))
            self.tax_other.set("Rs. " + str(round(self.total_other_prices * 0.05)))

        # Function For Text Area
        def welcome_soft(self):
            self.txt.delete('1.0', END)
            self.txt.insert(END, "       Welcome To BITD MESS BILL\n")
            self.txt.insert(END, f"\nBill No. : {str(self.c_bill_no.get())}")
            self.txt.insert(END, f"\nStudent Name : {str(self.cus_name.get())}")
            self.txt.insert(END, f"\nPhone No. : {str(self.c_phone.get())}")
            self.txt.insert(END, "\n===================================")
            self.txt.insert(END, "\nProduct          Qty         Price")
            self.txt.insert(END, "\n===================================")

        # Function to clear the bill area
        def clear(self):
            self.txt.delete('1.0', END)

        # Add Product name , qty and price to bill area
        def bill_area(self):
            self.welcome_soft()
            if self.bath_soap.get() != 0:
                self.txt.insert(END,
                                f"\nBath Soap         {self.bath_soap.get()}           {self.bath_soap.get() * 40}")
            if self.face_cream.get() != 0:
                self.txt.insert(END,
                                f"\nFace Cream        {self.face_cream.get()}           {self.face_cream.get() * 140}")
            if self.face_wash.get() != 0:
                self.txt.insert(END,
                                f"\nFace Wash         {self.face_wash.get()}           {self.face_wash.get() * 240}")
            if self.hair_spray.get() != 0:
                self.txt.insert(END,
                                f"\nHair Spray        {self.hair_spray.get()}           {self.hair_spray.get() * 340}")
            if self.body_lotion.get() != 0:
                self.txt.insert(END,
                                f"\nBody Lotion       {self.body_lotion.get()}           {self.body_lotion.get() * 260}")
            if self.wheat.get() != 0:
                self.txt.insert(END, f"\nWheat             {self.wheat.get()}           {self.wheat.get() * 100}")
            if self.food_oil.get() != 0:
                self.txt.insert(END, f"\nFood Oil          {self.food_oil.get()}           {self.food_oil.get() * 180}")
            if self.daal.get() != 0:
                self.txt.insert(END, f"\nDaal              {self.daal.get()}           {self.daal.get() * 80}")
            if self.rice.get() != 0:
                self.txt.insert(END, f"\nRice              {self.rice.get()}           {self.rice.get() * 80}")
            if self.sugar.get() != 0:
                self.txt.insert(END, f"\nSugar             {self.sugar.get()}           {self.sugar.get() * 170}")
            if self.maza.get() != 0:
                self.txt.insert(END, f"\nMaza              {self.maza.get()}           {self.maza.get() * 20}")
            if self.frooti.get() != 0:
                self.txt.insert(END, f"\nFrooti            {self.frooti.get()}           {self.frooti.get() * 50}")
            if self.coke.get() != 0:
                self.txt.insert(END, f"\nCoke              {self.coke.get()}           {self.coke.get() * 60}")
            if self.nimko.get() != 0:
                self.txt.insert(END, f"\nNimko             {self.nimko.get()}           {self.nimko.get() * 20}")
            if self.biscuits.get() != 0:
                self.txt.insert(END, f"\nBiscuits          {self.biscuits.get()}           {self.biscuits.get() * 20}")
            self.txt.insert(END, "\n===================================")
            self.txt.insert(END,
                            f"\n                      Total : {self.total_cosmetics_prices + self.total_grocery_prices + self.total_other_prices + self.total_cosmetics_prices * 0.05 + self.total_grocery_prices * 0.05 + self.total_other_prices * 0.05}")

        # Function to exit
        def exit(self):
            self.root.destroy()

        # Function To Clear All Fields

    root = Tk()
    object = Bill_App(root)
    root.mainloop()


def func_for_file7():


    # GUI
    root = Tk()
    root.title("BITD CHAT")

    BG_GRAY = "#ABB2B9"
    BG_COLOR = "#17202A"
    TEXT_COLOR = "#EAECEE"

    FONT = "Helvetica 14"
    FONT_BOLD = "Helvetica 13 bold"

    # Send function
    def send():
        send = "You -> " + e.get()
        txt.insert(END, "\n" + send)

        user = e.get().lower()

        if (user == "hello"):
            txt.insert(END, "\n" + "Bot -> Hi there, how can I help?")

        elif (user == "hi" or user == "hii" or user == "hiiii"):
            txt.insert(END, "\n" + "Bot -> Hi there, what can I do for you?")

        elif (user == "how are you"):
            txt.insert(END, "\n" + "Bot -> fine! and you")

        elif (user == "fine" or user == "i am good" or user == "i am doing good"):
            txt.insert(END, "\n" + "Bot -> Great! how can I help you.")

        elif (user == "thanks" or user == "thank you" or user == "now its my time"):
            txt.insert(END, "\n" + "Bot -> My pleasure !")

        elif (user == "what do you sell" or user == "what kinds of items are there" or user == "have you something"):
            txt.insert(END, "\n" + "Bot -> We have coffee and tea")

        elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line"):
            txt.insert(
                END, "\n" + "Bot -> What did the buffalo say when his son left for college? Bison.! ")

        elif (user == "goodbye" or user == "see you later" or user == "see yaa"):
            txt.insert(END, "\n" + "Bot -> Have a nice day!")

        else:
            txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")

        e.delete(0, END)

    lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Chat Section Of BITD", font=FONT_BOLD, pady=10, width=20,
                   height=1).grid(
        row=0)

    txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
    txt.grid(row=1, column=0, columnspan=2)

    scrollbar = Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.974)

    e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
    e.grid(row=2, column=0)

    send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
                  command=send).grid(row=2, column=1)

    root.mainloop()


def func_for_file8():
    import tkinter as tk
    from tkinter.tix import Tk

    root = Tk()

    # specify size of window.
    root.geometry("550x310")

    # Create text widget and specify size.
    T = tk.Text(root, height=20, width=90)

    # Create label
    l = tk.Label(root, text="RULES AND REGULATION")
    l.config(font=("Courier", 14))

    Fact = """1. Application for admission to hostel shall be made in the prescribed form which can
    be had from the Hostel Office.

    2. Allotement of rooms shall be made by the Deputy Wardens under the orders of Warden.

    3. Students must occupy the rooms allotted to them and should not change/exchange rooms without 
    prior permission from the Deputy Warden/Hostel Authorities. Violations of this rule will result
    in the Expulsion of the student concerned from the hostel.

    4. Resident Member may be shifted from one room to another without assigning any reason by the
    Deputy Warden.

    5. Hostel Furniture shall not be removed from one room to another under any circumstances.
    Students are responsible for the care of furniture and fittings in their respective rooms. The
    cost of furniture and fittings will be recovered from them in case of any damage or loss along
    with the fine of Rs.1000/-.

    6. Students are not allowed to use extra electrical fitting in their rooms unless permitted by 
    the Hostel Authorities.

    7.All the rooms, doors and windows should be kept neat and tidy. A fine of Rs.2000 will be levied
    for disfiguring of doors, glass panels, Furniture and walls of rooms from the resident(s) of the
    room in addition to the amount needed for repairing and repainting the above.

    8. A Collective fine of Rs.3000 /-will be collected from the residents of the respective 
    wings/floors for disfiguring Veranda’s and Bathrooms in addition to the amount needed for 
    repairing the above.

    9. A Collective fine of Rs.5000 /-will be collected from the residents of respective blocks 
    for disfiguring the common rooms or damaging the public property of hostel blocks, in
    addition to the replacement cost.

    10. Students should keep the toilets and bathrooms clean, failing which a collective fine of 
    Rs.3000/- will  be collected from the residents of the respective wings/floors.

    11. Residents are instructed to switch off the lights and fans when they go out of  the rooms,
    to save electric power. A fine of Rs.250/- per day will be collected from the residents of 
    the rooms, who violate this instruction.

    12. Guests /Visitors are not permitted to enter any rooms allotted to the residents. Anyone 
    who violates helps to violate this rule will be levied a fine of Rs.1000/- and will be evicted 
    from the hostel by the hostel authorities.

    13. If any misuse of computers and mobile phones in hostel rooms is brought to notice of 
    Hostel authorities the respective resident(s) will be expelled from the hostel.

    14. Students should not arrange any functions or meeting within the hostel /collage campus or
    outside the campus, without prior permission from the Principal and Warden.

    15. Any student who is removed from the college will automatically cease to be a member of
    the hostel.

    16. Accommodation in the hostel will not be given to students who are not active boarders 
    in the hostel.

    17. No student should stay away from the hostel on any day without the prior permission of
    the concerned Deputy Warden/Associate Warden/Principal and Warden.

    18. Abnormal activities of any nature causing disturbance to neighbours should not be carried 
    out in the rooms.

    19. Students should not paste any posters /pictures etc on the walls, doors, windows and 
    shelves. Cut-outs should not be placed or brought in the hostel.

    20. Student should not keep large amount of cash or costly items like mobile phones, camera, 
    Electronic gadgets, jewellery etc. in their rooms. Hence complaint about loss or theft about 
    such costly items is discouraged.

    21. Married students are not eligible for hostel accommodation.

    22. Students should not keep Mopeds, Motor cycles, Scooters and cars in the hostel premises.

    23. Students should settle in their rooms at 9 pm at studies on normal days and at 10 pm on
    free night days (Saturdays and Sundays) & maintain silence. 

    24. Girl students should return to the hostel before 6.30 pm and boys before 8 pm on all days. 

    25. The hostel will be personally inspected by the Deputy Warden and other authorities 
    regularly. The residents will be subjected to sever disciplinary action if they fail to 
    follow above mentioned rules and regulations"""

    # Create an Exit button.
    b2 = tk.Button(root, text="Exit",
                   command=root.destroy)

    l.pack()
    T.pack()
    b2.pack()

    # Insert The Fact.
    T.insert(tk.END, Fact)

    tk.mainloop()

def func_for_file9():
    # import tkinter module


    # make a window
    window = Tk()
    window.title("BITD HOSTEL ROOM TYPES")
    # specify it's size
    window.geometry("700x600")

    # function to calculate the
    # price of all the orders
    def calculate():

        # dic for storing the
        # food quantity and price
        dic = {'single_seater': [e1, 1080],
               'double_seater': [e2, 2075],
               'triple_seater': [e3, 3150],
               'with_ac': [e4, 1200],
               'with_room_heater': [e5, 1170],
               'extra_light': [e6, 135]
               }
        total = 0
        for key, val in dic.items():
            if val[0].get() != "":
                total += int(val[0].get()) * val[1]

        label16 = Label(window,
                        text="Your Total Bill is - " + str(total),
                        font="times 18")

        # position it
        label16.place(x=20, y=490)
        label16.after(1000, label16.destroy)
        window.after(1000, calculate)

    label8 = Label(window,
                   text="BITD HOSTEL ROOM",
                   font="times 28 bold")
    label8.place(x=350, y=20, anchor="center")

    label1 = Label(window,
                   text="TYPES",
                   font="times 28 bold")

    label1.place(x=520, y=70)

    label2 = Label(window, text="Single Seater \
                  Rs 1180", font="times 18")

    label2.place(x=450, y=120)

    label3 = Label(window, text="Double Seater \
                Rs 2075", font="times 18")

    label3.place(x=450, y=150)

    label4 = Label(window, text="Triple Seater	 \
      Rs 3150", font="times 18")
    label4.place(x=450, y=180)

    label5 = Label(window, text="With AC \
                        Rs 1200", font="times 18")

    label5.place(x=450, y=210)

    label6 = Label(window, text="With Room Heater \
       Rs 1170", font="times 18")

    label6.place(x=450, y=240)

    label7 = Label(window, text="Extra Light \
                   Rs 135", font="times 18")

    label7.place(x=450, y=270)

    # billing section
    label9 = Label(window, text="Select the room type",
                   font="times 18")
    label9.place(x=115, y=70)

    label10 = Label(window,
                    text="Single Seater",
                    font="times 18")
    label10.place(x=20, y=120)

    e1 = Entry(window)
    e1.place(x=20, y=150)

    label11 = Label(window, text="Double Seater",
                    font="times 18")
    label11.place(x=20, y=200)

    e2 = Entry(window)
    e2.place(x=20, y=230)

    label12 = Label(window, text="Triple Seater",
                    font="times 18")
    label12.place(x=20, y=280)

    e3 = Entry(window)
    e3.place(x=20, y=310)

    label13 = Label(window,
                    text="With AC",
                    font="times 18")
    label13.place(x=20, y=360)

    e4 = Entry(window)
    e4.place(x=20, y=390)

    label14 = Label(window,
                    text="With Room Heater",
                    font="times 18")
    label14.place(x=250, y=120)

    e5 = Entry(window)
    e5.place(x=250, y=150)

    label15 = Label(window,
                    text="Extra Light",
                    font="times 18")

    label15.place(x=250, y=200)

    e6 = Entry(window)
    e6.place(x=250, y=230)

    # execute calculate function after 1 second
    window.after(1000, calculate)

    # closing the main loop
    window.mainloop()



def func_for_file10():
    # Python Program to search string in text using Tkinter



    # to create a window
    root = Tk()

    # root window is the parent window
    fram = Frame(root)

    # adding label to search box
    Label(fram, text='STUDENT:').pack(side=LEFT)

    # adding of single line text box
    edit = Entry(fram)

    # positioning of text box
    edit.pack(side=LEFT, fill=BOTH, expand=1)

    # setting focus
    edit.focus_set()

    # adding of search button
    butt = Button(fram, text='Find by Name')
    butt.pack(side=RIGHT)
    fram.pack(side=TOP)

    # text box in root window
    text = Text(root)

    # text input area at index 1 in text window
    text.insert('1.0', '''
    RAMYA                               GH-140
    RUCHI                               GH-132
    NAINIKA                             GH-345
    NEHA                                GH-564
    ANUPRIYA                            GH-218
    SUKRITI                             GH-864
    SHIVANI                             GH-686
    MEESHO                              GH-564
    PRIYA                               GH-845
    ANJALI                              GH-325
    HANSIKA                             GH-852
    AMIESHA                             GH-159
    MEGHA                               GH-753
    RIYA                                GH-741
    SIYA                                GH-951
    TANU                                GH-519
    NISHI                               GH-591
    AVNI                                GH-753
    AANAYA                              GH-843
    SHREE                               GH-841
    SANU                                GH-956
    NAVPRIT                             GH-241
    JAYA                                GH-746
    AMEYA                               GH-654
    SHRISTY                             GH-687
    ISHA                                GH-697
    SHREYA                              GH-452
    SHRUTI                              GH-467
    TANAYA                              GH-937''')
    text.pack(side=BOTTOM)

    # function to search string in text
    def find():
        # remove tag 'found' from index 1 to END
        text.tag_remove('found', '1.0', END)

        # returns to widget currently in focus
        s = edit.get()
        if s:
            idx = '1.0'
            while 1:
                # searches for desired string from index 1
                idx = text.search(s, idx, nocase=1,
                                  stopindex=END)
                if not idx: break

                # last index sum of current index and
                # length of text
                lastidx = '%s+%dc' % (idx, len(s))

                # overwrite 'Found' at idx
                text.tag_add('found', idx, lastidx)
                idx = lastidx

            # mark located string as red
            text.tag_config('found', foreground='red')
        edit.focus_set()

    butt.config(command=find)
    root.mainloop()

def func_for_file11():
    # importing the required modules

    # importing the messagebox module from the tkinter library
    from tkinter import messagebox
    # importing the sqlite3 module as sql
    import sqlite3 as sql

    # defining the function to add tasks to the list
    def add_task():
        # getting the string from the entry field
        task_string = task_field.get()
        # checking whether the string is empty or not
        if len(task_string) == 0:
            # displaying a message box with 'Empty Field' message
            messagebox.showinfo('Error', 'Field is Empty.')
        else:
            # adding the string to the tasks list
            tasks.append(task_string)
            # using the execute() method to execute a SQL statement
            the_cursor.execute('insert into tasks values (?)', (task_string,))
            # calling the function to update the list
            list_update()
            # deleting the entry in the entry field
            task_field.delete(0, 'end')

        # defining the function to update the list

    def list_update():
        # calling the function to clear the list
        clear_list()
        # iterating through the strings in the list
        for task in tasks:
            # using the insert() method to insert the tasks in the list box
            task_listbox.insert('end', task)

        # defining the function to delete a task from the list

    def delete_task():
        # using the try-except method
        try:
            # getting the selected entry from the list box
            the_value = task_listbox.get(task_listbox.curselection())
            # checking if the stored value is present in the tasks list
            if the_value in tasks:
                # removing the task from the list
                tasks.remove(the_value)
                # calling the function to update the list
                list_update()
                # using the execute() method to execute a SQL statement
                the_cursor.execute('delete from tasks where title = ?', (the_value,))
        except:
            # displaying the message box with 'No Item Selected' message for an exception
            messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

        # function to delete all tasks from the list

    def delete_all_tasks():
        # displaying a message box to ask user for confirmation
        message_box = messagebox.askyesno('Delete All', 'Are you sure?')
        # if the value turns to be True
        if message_box == True:
            # using while loop to iterate through the tasks list until it's empty
            while (len(tasks) != 0):
                # using the pop() method to pop out the elements from the list
                tasks.pop()
                # using the execute() method to execute a SQL statement
            the_cursor.execute('delete from tasks')
            # calling the function to update the list
            list_update()

        # function to clear the list

    def clear_list():
        # using the delete method to delete all entries from the list box
        task_listbox.delete(0, 'end')

    # function to close the application
    def close():
        # printing the elements from the tasks list
        print(tasks)
        # using the destroy() method to close the application
        guiWindow.destroy()

    # function to retrieve data from the database
    def retrieve_database():
        # using the while loop to iterate through the elements in the tasks list
        while (len(tasks) != 0):
            # using the pop() method to pop out the elements from the list
            tasks.pop()
            # iterating through the rows in the database table
        for row in the_cursor.execute('select title from tasks'):
            # using the append() method to insert the titles from the table in the list
            tasks.append(row[0])

        # main function

    if __name__ == "__main__":
        # creating an object of the Tk() class
        guiWindow = Tk()
        # setting the title of the window
        guiWindow.title("To-Do List ")
        # setting the geometry of the window
        guiWindow.geometry("665x400+550+250")
        # disabling the resizable option
        guiWindow.resizable(0, 0)
        # setting the background color to #B5E5CF
        guiWindow.configure(bg="#B5E5CF")

        # using the connect() method to connect to the database
        the_connection = sql.connect('listOfTasks.db')
        # creating the cursor object of the cursor class
        the_cursor = the_connection.cursor()
        # using the execute() method to execute a SQL statement
        the_cursor.execute('create table if not exists tasks (title text)')

        # defining an empty list
        tasks = []

        # defining frames using the tk.Frame() widget
        functions_frame = Frame(guiWindow, bg="black")

        # using the pack() method to place the frames in the application
        functions_frame.pack(side="top", expand=True, fill="both")

        # defining another label using the Label() widget
        task_label = Label(functions_frame, text="Enter the Task:",
                           font=("arial", "14", "bold"),
                           background="black",
                           foreground="white"
                           )
        # using the place() method to place the label in the application
        task_label.place(x=20, y=30)

        # defining an entry field using the Entry() widget
        task_field = Entry(
            functions_frame,
            font=("Arial", "14"),
            width=42,
            foreground="black",
            background="white",
        )
        # using the place() method to place the entry field in the application
        task_field.place(x=180, y=30)

        # adding buttons to the application using the Button() widget
        add_button = Button(
            functions_frame,
            text="Add Task",
            width=15,
            bg='#D4AC0D', font=("arial", "14", "bold"),
            command=add_task,

        )
        del_button = Button(
            functions_frame,
            text="Delete Task",
            width=15,
            bg='#D4AC0D', font=("arial", "14", "bold"),
            command=delete_task,
        )
        del_all_button = Button(
            functions_frame,
            text="Delete All Tasks",
            width=15,
            font=("arial", "14", "bold"),
            bg='#D4AC0D',
            command=delete_all_tasks
        )
        exit_button = Button(
            functions_frame,
            text="Exit",
            width=52,
            bg='#D4AC0D', font=("arial", "14", "bold"),
            command=close
        )
        # using the place() method to set the position of the buttons in the application
        add_button.place(x=18, y=80, )
        del_button.place(x=240, y=80)
        del_all_button.place(x=460, y=80)
        exit_button.place(x=17, y=330)

        # defining a list box using the tk.Listbox() widget
        task_listbox = Listbox(
            functions_frame,
            width=57,
            height=7,
            font="bold",
            selectmode='SINGLE',
            background="WHITE",
            foreground="BLACK",
            selectbackground="#D4AC0D",
            selectforeground="BLACK"
        )
        # using the place() method to place the list box in the application
        task_listbox.place(x=17, y=140)

        # calling some functions
        retrieve_database()
        list_update()
        # using the mainloop() method to run the application
        guiWindow.mainloop()
        # establishing the connection with database
        the_connection.commit()
        the_cursor.close()

def func_for_file12():

    import calendar

    def showCalender():
        gui = Tk()
        gui.config(background='grey')
        gui.title("Calender for the year")
        gui.geometry("550x600")
        year = int(year_field.get())
        gui_content = calendar.calendar(year)
        calYear = Label(gui, text=gui_content, font="Consolas 10 bold")
        calYear.grid(row=5, column=1, padx=20)
        gui.mainloop()

    if __name__ == '__main__':
        new = Tk()
        new.config(background='grey')
        new.title("Calender")
        new.geometry("250x140")
        cal = Label(new, text="Calender", bg='grey', font=("times", 28, "bold"))
        year = Label(new, text="Enter year", bg='dark grey')
        year_field = Entry(new)
        button = Button(new, text='Show Calender',
                        fg='Black', bg='Blue', command=showCalender)

        # putting widgets in position
        cal.grid(row=1, column=1)
        year.grid(row=2, column=1)
        year_field.grid(row=3, column=1)
        button.grid(row=4, column=1)
        new.mainloop()

def func_for_file13():
    # Python Program to search string in text using Tkinter



    # to create a window
    root = Tk()

    # root window is the parent window
    fram = Frame(root)

    # adding label to search box
    Label(fram, text='STUDENT:').pack(side=LEFT)

    # adding of single line text box
    edit = Entry(fram)

    # positioning of text box
    edit.pack(side=LEFT, fill=BOTH, expand=1)

    # setting focus
    edit.focus_set()

    # adding of search button
    butt = Button(fram, text='Find by Name')
    butt.pack(side=RIGHT)
    fram.pack(side=TOP)

    # text box in root window
    text = Text(root)

    # text input area at index 1 in text window
    text.insert('1.0', '''
   PARENT'S NAME                STUDENT'S NAME                CONTACT OF PARENT'S

   RAJENDRA KUMAR                   RAMYA                        678675646545
   ANKESH DEO                       RUCHI                        344657689090
   BALESHWAR SINGH                  NAINIKA                      567698797787
   UJJAWAL MAHAJAN                  NEHA                         243657687990
   ANKIT MALLIK                     ANUPRIYA                     123547689989
   AVINASH PAREKH                   SUKRITI                      344657689090
   SATISH SHARMA                    SHIVANI                      567698797787
   AANKESH MANGAL                   MEESHO                       243657687990
   VIRAT MALHOTRA                   PRIYA                        123547689989
   SACHIN JHA                       ANJALI                       344657689090
   GOPAL CHADHA                     HANSIKA                      567698797787
   ASHU AHLUWALIA                   AMIESHA                      243657687990
   ADITIYA BANERJEE                 MEGHA                        123547689989
   ARBIND BHATT                     RIYA                         344657689090
   AKHILESH KHANNA                  SIYA                         567698797787
   PRAVEEN GROVER                   TANU                         243657687990
   RITIK KAUR                       NISHI                        123547689989
   SANTOSH CHOPRA                   AVNI                         344657689090
   VIKASH DHAWAN                    AANAYA                       567698797787
   VISHWAJEET DIXIT                 SHREE                        243657687990
   JITENDRA DUBEY                   SANU                         123547689989
   ANUJ CHAUHAN                     NAVPRIT                      344657689090
   PANKAJ DAYAL                     JAYA                         567698797787
   KRISH GOSWAMI                    AMEYA                        243657687990
   SUMIT GOEL                       SHRISTY                      123547689989
   HARSH MAHAJAN                    ISHA                         344657689090
   PRAFUL SAXENA                    SHREYA                       567698797787
   FARHAN RAY                       SHRUTI                       243657687990
   IMRAN SHAH                       TANAYA                       123547689989''')
    text.pack(side=BOTTOM)

    # function to search string in text
    def find():
        # remove tag 'found' from index 1 to END
        text.tag_remove('found', '1.0', END)

        # returns to widget currently in focus
        s = edit.get()
        if s:
            idx = '1.0'
            while 1:
                # searches for desired string from index 1
                idx = text.search(s, idx, nocase=1,
                                  stopindex=END)
                if not idx: break

                # last index sum of current index and
                # length of text
                lastidx = '%s+%dc' % (idx, len(s))

                # overwrite 'Found' at idx
                text.tag_add('found', idx, lastidx)
                idx = lastidx

            # mark located string as red
            text.tag_config('found', foreground='red')
        edit.focus_set()

    butt.config(command=find)

    root.mainloop()

def func_for_file14():
    # Import Module


    # Create Object
    root = Tk()

    # Set geometry
    root.geometry('400x500')

    # Information List
    datas = []

    # Add Information
    def add():
        global datas
        datas.append([Name.get(), Number.get(), address.get(1.0, "end-1c")])
        update_book()

    # View Information
    def view():
        Name.set(datas[int(select.curselection()[0])][0])
        Number.set(datas[int(select.curselection()[0])][1])
        address.delete(1.0, "end")
        address.insert(1.0, datas[int(select.curselection()[0])][2])

    # Delete Information
    def delete():
        del datas[int(select.curselection()[0])]
        update_book()

    def reset():
        Name.set('')
        Number.set('')
        address.delete(1.0, "end")

    # Update Information
    def update_book():
        select.delete(0, END)
        for n, p, a in datas:
            select.insert(END, n)

    # Add Buttons, Label, ListBox
    Name = StringVar()
    Number = StringVar()

    frame = Frame()
    frame.pack(pady=10)

    frame1 = Frame()
    frame1.pack()

    frame2 = Frame()
    frame2.pack(pady=10)

    Label(frame, text='Name', font='arial 12 bold').pack(side=LEFT)
    Entry(frame, textvariable=Name, width=50).pack()

    Label(frame1, text='Phone No.', font='arial 12 bold').pack(side=LEFT)
    Entry(frame1, textvariable=Number, width=50).pack()

    Label(frame2, text='Address', font='arial 12 bold').pack(side=LEFT)
    address = Text(frame2, width=37, height=10)
    address.pack()

    Button(root, text="Add", font="arial 12 bold", command=add).place(x=100, y=270)
    Button(root, text="View", font="arial 12 bold", command=view).place(x=100, y=310)
    Button(root, text="Delete", font="arial 12 bold", command=delete).place(x=100, y=350)
    Button(root, text="Reset", font="arial 12 bold", command=reset).place(x=100, y=390)

    scroll_bar = Scrollbar(root, orient=VERTICAL)
    select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
    scroll_bar.config(command=select.yview)
    scroll_bar.pack(side=RIGHT, fill=Y)
    select.place(x=200, y=260)

    # Execute Tkinter
    root.mainloop()

def func_for_file15():
    ##QUANTITY##

    import tkinter as tk

    from tkinter import ttk
    from tkinter import BOTH, END, LEFT

    menu = {0: ['NOODLES', 45], 1: ['PIZZA', 135], 2: ['BURGER', 160],
            3: ['BISCUIT', 20], 4: ['COFFEE', 50], 5: ['SOFT-DRINK', 35],
            6: ['TEA', 15], 7: ['WATER', 20]}
    sb = []

    my_w = tk.Tk()
    my_w.geometry("1000x800")

    my_w.title("STRATERS AND DRINKS")
    my_w.columnconfigure(0, weight=8)
    my_w.columnconfigure(1, weight=2)
    my_w.rowconfigure(0, weight=1)
    my_w.rowconfigure(1, weight=12)  # change weight to 4
    my_w.rowconfigure(2, weight=1)

    frame_top = tk.Frame(my_w, bg='white')
    frame_bottom = tk.Frame(my_w, bg='white')

    frame_m_right = tk.Frame(my_w, bg='#f8fab4')
    frame_m_left = tk.Frame(my_w, bg='#bfedf2')

    # placing in grid
    frame_top.grid(row=0, column=0, sticky='WENS', columnspan=2)
    frame_m_left.grid(row=1, column=0, sticky='WENS')
    frame_m_right.grid(row=1, column=1, sticky='WENS')
    frame_bottom.grid(row=2, column=0, sticky='WENS', columnspan=2)
    trv = ttk.Treeview(frame_m_right, selectmode='browse')
    trv.grid(row=0, column=0, columnspan=2, padx=3, pady=2)

    # column identifiers
    trv["columns"] = ("1", "2", "3")
    trv.column("#0", width=80, anchor='w')
    trv.column("1", width=60, anchor='w')
    trv.column("2", width=50, anchor='c')
    trv.column("3", width=50, anchor='c')

    # Headings
    # respective columns
    trv.heading("#0", text="Item", anchor='w')
    trv.heading("1", text="Price", anchor='w')
    trv.heading("2", text="qty", anchor='c')
    trv.heading("3", text="Total", anchor='c')

    def my_reset():
        for item in trv.get_children():
            trv.delete(item)
        # for i in range(len(sb)):
        #    sb[i].config(textvariable=0)    # reset spinbox
        l1 = []
        for i in range(8):
            l1.append(tk.IntVar(value=0))
        for i in range(len(sb)):
            print(sb[i].config(textvariable=l1[i]))

        for w in frame_m_right.grid_slaves(1):
            w.grid_remove()
        for w in frame_m_right.grid_slaves(2):
            w.grid_remove()
        for w in frame_m_right.grid_slaves(3):
            w.grid_remove()

    def my_bill():
        total = 0
        for item in trv.get_children():
            trv.delete(item)
        for i in range(len(sb)):
            if (int(sb[i].get()) > 0):
                price = int(sb[i].get()) * menu[i][1]
                total = total + price
                my_str1 = (str(menu[i][1]), str(sb[i].get()), str(price))
                trv.insert("", 'end', iid=i, text=menu[i][0], values=my_str1)
        lr1 = tk.Label(frame_m_right, text='Total', font=font1)
        lr1.grid(row=1, column=0, sticky='nw')
        lr2 = tk.Label(frame_m_right, text=str(total), font=font1)
        lr2.grid(row=1, column=1, sticky='nw')
        lr21 = tk.Label(frame_m_right, text='Tax 10%', font=font1)
        lr21.grid(row=2, column=0, sticky='nw')
        tax = 0.1 * total
        lr22 = tk.Label(frame_m_right, text=str(tax), font=font1)
        lr22.grid(row=2, column=1, sticky='nw')
        lr31 = tk.Label(frame_m_right, text='Total', font=font2)
        lr31.grid(row=3, column=0, sticky='nw')
        final = total + tax
        lr32 = tk.Label(frame_m_right, text=str(final), font=font2)
        lr32.grid(row=3, column=1, sticky='nw')

    # Layout is over , sart placing buttons
    # path_image="G:\\My Drive\\testing\\plus2_restaurant_v1\\images\\"
    font1 = ('Times', 20, 'normal')
    font2 = ('Times', 32, 'bold')
    pdx, pdy = 40, 5
    # img_top = tk.PhotoImage(file = path_image+"restaurant-3.png")
    # bg=tk.PhotoImage(file=path_image+'bg.png')

    # c1 = tk.Canvas(frame_m_left,width=1000,height=500)
    # c1.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='nw',padx=0)
    # c1.create_image(0,0,image=bg,anchor='nw')

    # img_l1 = tk.Label(frame_top,  image=img_top)
    # img_l1.grid(row=0,column=0,sticky='nw',pady=1)

    # img_menu1=tk.PhotoImage(file=path_image+"food-item-1.png")
    # img_menu2=tk.PhotoImage(file=path_image+"food-item-2.png")
    # img_menu3=tk.PhotoImage(file=path_image+"food-item-3.png")
    # img_menu4=tk.PhotoImage(file=path_image+"food-item-4.png")
    # img_menu5=tk.PhotoImage(file=path_image+"food-item-5.png")
    # img_menu6=tk.PhotoImage(file=path_image+"food-item-6.png")
    # img_menu7=tk.PhotoImage(file=path_image+"food-item-7.png")
    # img_menu8=tk.PhotoImage(file=path_image+"food-item-8.png")

    menu1 = tk.Button(frame_m_left, text='NOODLES')
    menu1.grid(row=0, column=0, sticky='nw', padx=pdx, pady=pdy)
    menu2 = tk.Button(frame_m_left, text='PIZZA')
    menu2.grid(row=0, column=1, sticky='nw', padx=pdx, pady=pdy)
    menu3 = tk.Button(frame_m_left, text='BURGER')
    menu3.grid(row=0, column=2, sticky='nw', padx=pdx, pady=pdy)
    menu4 = tk.Button(frame_m_left, text='BISCUIT')
    menu4.grid(row=0, column=3, sticky='nw', padx=pdx, pady=0)
    sv1 = tk.IntVar()
    sb1 = tk.Spinbox(frame_m_left, from_=0, to_=5, font=font1, width=1, textvariable=sv1)
    sb1.grid(row=1, column=0, sticky='nw', padx=pdx, pady=0)
    sb.append(sb1)
    sv2 = tk.IntVar()
    sb2 = tk.Spinbox(frame_m_left, from_=0, to_=5, font=font1, width=1, textvariable=sv2)
    sb2.grid(row=1, column=1, sticky='nw', padx=pdx, pady=0)
    sb.append(sb2)
    sv3 = tk.IntVar()
    sb3 = tk.Spinbox(frame_m_left, from_=0, to_=5, font=font1, width=1, textvariable=sv3)
    sb3.grid(row=1, column=2, sticky='nw', padx=pdx, pady=0)
    sb.append(sb3)
    sv4 = tk.IntVar()
    sb4 = tk.Spinbox(frame_m_left, from_=0, to_=5, font=font1, width=1, textvariable=sv4)
    sb4.grid(row=1, column=3, sticky='nw', padx=pdx, pady=0)
    sb.append(sb4)
    menu5 = tk.Button(frame_m_left, text='COFFEE')
    menu5.grid(row=2, column=0, sticky='nw', padx=pdx, pady=pdy)
    menu6 = tk.Button(frame_m_left, text='SOFT-DRINK')
    menu6.grid(row=2, column=1, sticky='nw', padx=pdx, pady=pdy)
    menu7 = tk.Button(frame_m_left, text='TEA')
    menu7.grid(row=2, column=2, sticky='nw', padx=pdx, pady=pdy)
    menu8 = tk.Button(frame_m_left, text='WATER')
    menu8.grid(row=2, column=3, sticky='nw', padx=pdx, pady=pdy)
    sv5 = tk.IntVar()
    sb5 = tk.Spinbox(frame_m_left, from_=0, to_=5, font=font1, width=1, textvariable=sv5)
    sb5.grid(row=3, column=0, sticky='nw', padx=pdx, pady=pdy)
    sb.append(sb5)
    sv6 = tk.IntVar()
    sb6 = tk.Spinbox(frame_m_left, from_=0, to_=5, font=font1, width=1, textvariable=sv6)
    sb6.grid(row=3, column=1, sticky='nw', padx=pdx, pady=pdy)
    sb.append(sb6)
    sv7 = tk.IntVar()
    sb7 = tk.Spinbox(frame_m_left, from_=0, to_=5, font=font1, width=1, textvariable=sv7)
    sb7.grid(row=3, column=2, sticky='nw', padx=pdx, pady=pdy)
    sb.append(sb7)
    sv8 = tk.IntVar()
    sb8 = tk.Spinbox(frame_m_left, from_=0, to_=5, font=font1, width=1, textvariable=sv8)
    sb8.grid(row=3, column=3, sticky='nw', padx=pdx, pady=pdy)
    sb.append(sb8)
    b1 = tk.Button(frame_m_left, text='Get Bill', command=my_bill)
    b1.grid(row=4, column=1)
    b2 = tk.Button(frame_m_left, text='Confirm ( Reset)', command=my_reset)
    b2.grid(row=4, column=2)
    my_w.mainloop()

    # ============================INITIALIZATION==============================
    if __name__ == '__main__':
        Database()
    root.mainloop()


def main():
    # Decide what order you want to call these methods.
    func_for_file1()


if __name__ == '__main__':
    main()
