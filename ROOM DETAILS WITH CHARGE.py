# import tkinter module
from tkinter import *

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
			total += int(val[0].get())*val[1]

	label16 = Label(window,
					text="Your Total Bill is - "+str(total),
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
