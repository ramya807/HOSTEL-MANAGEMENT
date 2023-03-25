from tkinter import *


roota = Tk()
roota.title("GIRLS HOSTEL MANAGEMENT")  # Title of the application
roota.geometry('500x500+400+100')  # Size of the screen
Label(text='BIT GIRLS HOSTEL MANAGEMENT', fg='red', font=44).pack()  # text size and color of the topic


Chooser = Menu()  # chooser is used for menubar
itemone = Menu()  # itemone is display for the topics which comes under the my-profile
itemone.add_command(label='Student Details')  # topic one under my-profile
itemone.add_command(label='Update Details')  # topic two under my-profile

itemtwo = Menu()  # itemtwo is display for the topics which comes under the users
itemtwo.add_command(label='User Info')
itemtwo.add_command(label='Upload Photo')
itemtwo.add_command(label='Add Friends')

itemthree = Menu()  # itemthree is display for the topics which comes under the hostels
itemthree.add_command(label='Staff Records')
itemthree.add_command(label='Student Records')
itemthree.add_command(label='Room Details')

itemfour = Menu()  # itemfour is display for the topics which comes under the warden
itemfour.add_command(label='Application List')
itemfour.add_command(label='Room List')
itemfour.add_command(label='Payment List')
itemfour.add_command(label='Visitor')
itemfour.add_command(label='Allocate Room')

itemfive = Menu()  # itemfive is display for the topics which comes under the payment list
itemfive.add_command(label='Initiate Payment')

itemsix = Menu()  # itemsix is display for the topics which comes under the room list
itemsix.add_command(label='Room Details')
itemsix.add_command(label='Room Availability')
itemsix.add_command(label='Update Details')

itemseven = Menu()  # itemseven is display for the topics which comes under the visitor
itemseven.add_command(label='Search Student')

# Used to view in screen all the labels in menubar
Chooser.add_cascade(label='My Profile', menu=itemone)
Chooser.add_cascade(label='Users', menu=itemtwo)
Chooser.add_cascade(label='Hostels', menu=itemthree)
Chooser.add_cascade(label='Warden', menu=itemfour)
Chooser.add_cascade(label='Payment List', menu=itemfive)
Chooser.add_cascade(label='Room List', menu=itemsix)
Chooser.add_cascade(label='Visitor', menu=itemseven)

roota.config(menu=Chooser)
roota.mainloop()
