import tkinter as tk
from tkinter.tix import Tk

root = Tk()

# specify size of window.
root.geometry("550x310")

# Create text widget and specify size.
T = tk.Text(root, height = 20, width = 90)

# Create label
l = tk.Label(root, text ="RULES AND REGULATION")
l.config(font =("Courier", 14))

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
b2 = tk.Button(root, text ="Exit",
               command = root.destroy)

l.pack()
T.pack()
b2.pack()

# Insert The Fact.
T.insert(tk.END, Fact)

tk.mainloop()
