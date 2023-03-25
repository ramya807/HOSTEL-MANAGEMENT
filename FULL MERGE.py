from tkinter import *

import pyttsx3

engine = pyttsx3.init()


def func_for_file1():
    # All of the code from File 1 goes here.

    from PIL import ImageTk, Image
    roota = Tk()
    roota.title("GIRLS HOSTEL MANAGEMENT")  # Title of the application
    roota.geometry('400x500+400+100')  # Size of the screen

    #image = Image.open("C:\\Users\hp\Desktop\\Campus View of Birla Institute of Technology Extension Centre Deoghar_Campus-View.jpg")
    # Resize the image using resize() method
    #resize_image = image.resize((1400, 700))
    #img = ImageTk.PhotoImage(resize_image)
    # create label and add resize image
    ##label1 = Label(image=img)
    ##label1.image = img
   ## label1.pack()##

    Label(text='BIT GIRLS HOSTEL MANAGEMENT', fg='red', font=44).pack()  # text size and color of the topic

    Chooser = Menu()  # chooser is used for menubar
    itemone = Menu()  # itemone is display for the topics which comes under the my-profile
    itemone.add_command(label='Student Details', command=func_for_file3)  # topic one under my-profile
    itemone.add_command(label='Update Details')  # topic two under my-profile

    itemtwo = Menu()  # itemtwo is display for the topics which comes under the users
    itemtwo.add_command(label='User Info')
    itemtwo.add_command(label='Upload Photo')
    itemtwo.add_command(label='Add Friends')

    itemthree = Menu()  # itemthree is display for the topics which comes under the hostels
    itemthree.add_command(label='Staff Records', command=func_for_file7)
    itemthree.add_command(label='Student Records', command=func_for_file2)
    itemthree.add_command(label='Room Details')

    itemfour = Menu()  # itemfour is display for the topics which comes under the warden
    itemfour.add_command(label='Application List')
    itemfour.add_command(label='Room List')
    itemfour.add_command(label='Payment List')
    itemfour.add_command(label='Visitor')
    itemfour.add_command(label='Allocate Room')

    itemfive = Menu()  # itemfive is display for the topics which comes under the payment list
    itemfive.add_command(label='Initiate Payment', command=func_for_file4)
    itemfive.add_command(label='Authorized Payment', command=func_for_file4)
    itemfive.add_command(label='Modify Payment', command=func_for_file4)
    itemfive.add_command(label='Approve Payment', command=func_for_file4)
    itemfive.add_command(label='Send Payment List', command=func_for_file4)

    itemsix = Menu()  # itemsix is display for the topics which comes under the room list
    itemsix.add_command(label='Room Details')
    itemsix.add_command(label='Room Availability')
    itemsix.add_command(label='Update Details')

    itemseven = Menu()  # itemseven is display for the topics which comes under the visitor
    itemseven.add_command(label='Search Student')

    itemeight = Menu()
    itemeight.add_command(label='Data Dictionary', command=func_for_file5)

    itemnine = Menu()
    itemeight.add_command(label='Rules', command=func_for_file6)

    # Used to view in screen all the labels in menubar
    Chooser.add_cascade(label='My Profile', menu=itemone)
    Chooser.add_cascade(label='Users', menu=itemtwo)
    Chooser.add_cascade(label='Hostels', menu=itemthree)
    Chooser.add_cascade(label='Warden', menu=itemfour)
    Chooser.add_cascade(label='Payment List', menu=itemfive)
    Chooser.add_cascade(label='Room List', menu=itemsix)
    Chooser.add_cascade(label='Visitor', menu=itemseven)
    Chooser.add_cascade(label='Data Dictionary', menu=itemeight)
    Chooser.add_cascade(label='Rules', menu=itemnine)

    roota.config(menu=Chooser)
    roota.mainloop()


engine.say('GIRLS HOSTEL MANAGEMENT APPLICATION')
engine.runAndWait()


def func_for_file2():
    # ALl of the code from File 2 goes here.
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


def func_for_file3():
    # All code of third file goes here
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


def func_for_file5():
    # Importing the modules
    import tkinter
    import tkinter.ttk as ttk

    import sqlite3
    import tkinter.messagebox as tkMessageBox

    root = Tk()
    root.title("DATA DICTIONARY")
    root.geometry("780x400+0+0")
    root.config(bg="Pink")

    # Variables required for storing the values
    name = StringVar()
    type = StringVar()
    mode = StringVar()
    description = StringVar()

    # Function for resetting the values
    def Reset():
        name.set("")
        type.set("")
        mode.set("")
        description.set("")

    # For creating the database and the table
    def Database():
        cconnectn = sqlite3.connect("ccontactdata.db")
        cursor = cconnectn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `ccontactinformation` (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT, type TEXT, mode TEXT, description TEXT)")
        cursor.execute("SELECT * FROM `ccontactinformation` ORDER BY `last_name` ASC")
        fetchinfo = cursor.fetchall()
        for data in fetchinfo:
            tree.insert('', 'end', values=(data))
        cursor.close()
        cconnectn.close()

    # Function for exiting the system
    def Exit():
        O = tkinter.messagebox.askyesno("Contact Management System", "Do you want to exit the system")
        if O > 0:
            root.destroy()
        return

    # Insert query for inserting the value in database Table
    def Submit():
        if name.get() == "" or type.get() == "" or mode.get() == "" or description.get() == "":
            msgg = tkMessageBox.showwarning('', 'Please Complete All the Fields', icon="warning")
        else:
            tree.delete(*tree.get_children())
        cconnectn = sqlite3.connect("ccontactdata.db")
        cursor = cconnectn.cursor()

        cursor.execute("INSERT INTO `ccontactinformation` (name, type, mode, description ) VALUES( ?, ?, ?, ?)",
                       (str(name.get()), str(type.get()), str(mode.get()), str(description.get())))

        cconnectn.commit()
        cursor.execute("SELECT * FROM `ccontactinformation` ORDER BY `last_name` ASC")
        fetchinfo = cursor.fetchall()

        for data in fetchinfo:
            tree.insert('', 'end', values=(data))
        cursor.close()
        cconnectn.close()
        name.set("")
        type.set("")
        mode.set("")
        description.set("")

    # Update Query for updating the table in the database
    def Update():
        if name.get() == "":
            msgg = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
        else:
            tree.delete(*tree.get_children())
        cconnectn = sqlite3.connect("ccontactdata.db")
        cursor = cconnectn.cursor()
        cursor.execute(
            "UPDATE `ccontactinformation` SET `name` = ?, `type` = ?, `mode` = ?, `description` = ? WHERE `id` = ?",
            (str(name.get()), str(type.get()), str(mode.get()),
             str(description.get()), int(id)))
        cconnectn.commit()
        cursor.execute("SELECT * FROM `ccontactinformation` ORDER BY `last_name` ASC")
        fetchinfo = cursor.fetchall()
        for data in fetchinfo:
            tree.insert('', 'end', values=(data))

        cursor.close()
        cconnectn.close()

        name.set("")
        type.set("")
        mode.set("")
        description.set("")

    # Module for the update contact form window
    def UpdateContact(event):
        global id, UpdateWindow
        curItem = tree.focus()
        contents = (tree.item(curItem))
        item = contents['values']
        id = item[0]
        name.set("")
        type.set("")
        mode.set("")
        description.set("")

        name.set(item[1])
        type.set(item[2])
        mode.set(item[3])
        description.set(item[4])

        UpdateWindow = Toplevel()
        UpdateWindow.title("DATA DICTIONARY")
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

        # LABELS
        label_title = Label(FormTitle, text="Update the Contact Information", font=('Arial', 17), bg="light green",
                            width=400)
        label_title.pack(fill=X)
        label_Name = Label(ContactForm, text="Name", font=('Calibri', 14), bd=5)
        label_Name.grid(row=0, sticky=W)

        label_Type = Label(ContactForm, text="type", font=('Calibri', 14), bd=5)
        label_Type.grid(row=4, sticky=W)

        label_Mode = Label(ContactForm, text=" Mode", font=('Calibri', 14), bd=5)
        label_Mode.grid(row=5, sticky=W)

        label_Description = Label(ContactForm, text="description", font=('Calibri', 14), bd=5)
        label_Description.grid(row=6, sticky=W)

        # TEXT ENTRY
        Name = Entry(ContactForm, textvariable=name, font=('Calibri', 14, 'bold'), bd=2, width=20, justify='left')
        Name.grid(row=0, column=1)

        Type = Entry(ContactForm, textvariable=type, font=('Calibri', 14, 'bold'), bd=2, width=20, justify='left')
        Type.grid(row=4, column=1)

        Mode = Entry(ContactForm, textvariable=mode, font=('Calibri', 14, 'bold'), bd=2, width=20,
                     justify='left')
        Mode.grid(row=5, column=1)

        Description = Entry(ContactForm, textvariable=description, font=('Calibri', 14, 'bold'), bd=2, width=20,
                            justify='left')
        Description.grid(row=6, column=1)

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
        cconnectn = sqlite3.connect("ccontactdata.db")
        cursor = cconnectn.cursor()
        cursor.execute("DELETE FROM `ccontactinformation` WHERE `id` = %d" % item[0])
        cconnectn.commit()
        cursor.close()
        cconnectn.close()

    # For creating the frame, labels, text entry, and button for add new contact form window
    def MyNewContact():
        global opennewwindow
        name.set("")
        type.set("")
        mode.set("")
        description.set("")

        Opennewwindow = Toplevel()
        Opennewwindow.title("DATA DICTIONARY")
        Opennewwindow.resizable(0, 0)
        Opennewwindow.geometry("500x500+0+0")
        if 'UpdateWindow' in globals():
            UpdateWindow.destroy()

        #############Frames####################
        FormTitle = Frame(Opennewwindow)
        FormTitle.pack(side=TOP)
        ContactForm = Frame(Opennewwindow)
        ContactForm.pack(side=TOP, pady=10)

        # ===================LABELS==============================
        label_title = Label(FormTitle, text="Adding New Contacts", bd=12, fg="black", bg="Lightgreen",
                            font=("Calibri", 15, "bold"), pady=2)
        label_title.pack(fill=X)
        label_Name = Label(ContactForm, text="Name", font=('Calibri', 14), bd=5)
        label_Name.grid(row=0, sticky=W)

        label_Type = Label(ContactForm, text="Type", font=('Calibri', 14), bd=5)
        label_Type.grid(row=4, sticky=W)

        label_Mode = Label(ContactForm, text="Mode", font=('Calibri', 14), bd=5)
        label_Mode.grid(row=5, sticky=W)

        label_Description = Label(ContactForm, text="Description", font=('Calibri', 14), bd=5)
        label_Description.grid(row=6, sticky=W)

        # ===================ENTRY===============================
        Name = Entry(ContactForm, textvariable=name, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
        Name.grid(row=0, column=1)

        Type = Entry(ContactForm, textvariable=type, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
        Type.grid(row=4, column=1)

        Mode = Entry(ContactForm, textvariable=mode, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
        Mode.grid(row=5, column=1)

        Description = Entry(ContactForm, textvariable=description, font=('Calibri', 14, 'bold'), bd=3, width=20,
                            justify='left')
        Description.grid(row=6, column=1)

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
    label_title = Label(Top, text="DATA DICTIONARY", bd=7, relief=GROOVE, fg="Black", bg="lightgreen",
                        font=("Calibri", 25, "bold"), pady=3)
    label_title.pack(fill=X)

    # BUTTONS
    Add_Button = Button(F, text='Add New Data', font=('Calibri', 17, 'bold'), fg="black",
                        bg="lightgreen", command=MyNewContact).grid(row=0, column=0, ipadx=20, padx=30)

    Delete_Button = Button(F, text='Delete The Data', font=('Calibri', 17, 'bold'), command=Delete,
                           fg="black", bg="lightgreen").grid(row=0, column=1, ipadx=20)

    Exit_Button = Button(F, text='Exit System', font=('Calibri', 17, 'bold'), command=Exit,
                         fg="black", bg="lightgreen").grid(row=0, column=2, ipadx=20, padx=30)

    # creating a tables in contact management system
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Id", "Name", "Type", "Mode", "Description"),
                        height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('Id', text="Id", anchor=W)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Type', text="Type", anchor=W)
    tree.heading('Mode', text="Mode", anchor=W)
    tree.heading('Description', text="Description", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=80)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=90)

    tree.pack()
    tree.bind('<Double-Button-1>', UpdateContact)

    # ============================INITIALIZATION==============================
    if __name__ == '__main__':
        Database()
    root.mainloop()


def func_for_file6():
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


def func_for_file7():
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


def main():
    # Decide what order you want to call these methods.
    func_for_file1()


if __name__ == '__main__':
    main()
