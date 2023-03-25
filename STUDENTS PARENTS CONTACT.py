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
