# Python Program to search string in text using Tkinter

from tkinter import *

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
