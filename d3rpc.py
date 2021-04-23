#
from pypresence import Presence
from pypresence import Client
from tkinter import *
import time

time = time.time()
client_id = '835127760849993798'        #Discord client ID
RPC = Presence(client_id)
Connected = False

#Classes
ClassList = [
    '--Select--',
    'Barbarian',
    'Crusader',
    'Demon Hunter',
    'Monk',
    'Necromancer',
    'Witch Doctor',
    'Wizard'
]

#Class Index Dictionary
ClassIndexList = {
    '--Select--': 0,
    'Barbarian': 1,
    'Crusader': 2,
    'Demon Hunter': 3,
    'Monk': 4,
    'Necromancer': 5,
    'Witch Doctor': 6,
    'Wizard': 7
}

#Genders not used
GenderList = [
    'Male',
    'Female'
]

#MalePortraitImages
PortraitListMale = [
    '--Select--',
    'barbarian_male',
    'crusader_male',
    'demon_hunter_male',
    'monk_male',
    'necromancer_male',
    'witch_doctor_male',
    'wizard_male',
]

#FemalePortraitImages
PortraitListFemale = [
    '--Select--',
    'barbarian_female',
    'crusader_female',
    'demon_hunter_female',
    'monk_female',
    'necromancer_female',
    'witch_doctor_female',
    'wizard_female'
]

#Difficulties
DiffList = [
    '--Select--',
    'Normal',
    'Hard',
    'Expert',
    'Master',
    'T1',
    'T2',
    'T3',
    'T4',
    'T5',
    'T6',
    'T7',
    'T8',
    'T9',
    'T10',
    'T11',
    'T12',
    'T13',
    'T14',
    'T15',
    'T16'
]

#Activities
ActivityList = [
    '--Select--',
    'Nephalem Rift',
    'Greater Rift',
    'Bounties',
    'Town',
    'Chilling'
]


win = Tk()
win.geometry('200x400')
win.resizable(False, False)
win.iconbitmap('d3rpc.ico')
win.title('D3RPC - The dumb manual Diablo 3 rich presence.')
can = Canvas(win, bg='#21252B', height=400, width=200) #21252B dark #282C34 light
can.place(relx=0.5, rely=0.5, anchor=CENTER)


chosenClass = StringVar()
chosenClass.set(ClassList[0])
chosenDiff = StringVar()
chosenDiff.set(DiffList[0])
chosenActivity = StringVar()
chosenActivity.set(ActivityList[0])
chosenGenderFemale = StringVar()
chosenGenderFemale.set(PortraitListFemale[1])
chosenGenderMale = StringVar()
chosenGenderMale.set(PortraitListMale[1])

bgdiablo = PhotoImage(file='diablo.png')
labelDiablo = Label(win, image=bgdiablo)
labelDiablo.place(relx=0.5, rely=0.5, anchor=CENTER)

#Character Class Picker
labelClass = Label(win, text='Class', fg='#8EB2BF', bg='#21252B').pack()
character_classes = OptionMenu(win, chosenClass, *ClassList)
character_classes.config(fg='#8EB2BF', bg='#414855', activebackground='#414855', activeforeground='white', borderwidth=0, highlightthickness=0, relief='flat')
character_classes['menu'].config(fg='#8EB2BF', bg='#414855', relief='flat', borderwidth='0')
character_classes.pack()



#Character Gender Picker for portraits
labelGender = Label(win, text='Gender', fg='#8EB2BF', bg='#21252B').pack()
Gender = IntVar()
character_genders = Checkbutton(win,fg='#8EB2BF', bg='#21252B',activebackground='#21252B', activeforeground='white', text='Is character Female?', variable=Gender, onvalue=1, offvalue=0).pack()



#Difficulty Picker
labelDifficulty = Label(win, text='Difficulty', fg='#8EB2BF', bg='#21252B').pack()
difficulty_levels = OptionMenu(win, chosenDiff, *DiffList)
difficulty_levels.config(fg='#8EB2BF', bg='#414855', activebackground='#414855', activeforeground='white', borderwidth=0, highlightthickness=0, relief='flat')
difficulty_levels['menu'].config(fg='#8EB2BF', bg='#414855', relief='flat')
difficulty_levels.pack()


#Activity Picker
labelActivities = Label(win, text='Activity', fg='#8EB2BF', bg='#21252B').pack()
activities = OptionMenu(win, chosenActivity, *ActivityList)
activities.config(fg='#8EB2BF', bg='#414855', activebackground='#414855', activeforeground='white', borderwidth=0, highlightthickness=0, relief='flat')
activities['menu'].config(fg='#8EB2BF', bg='#414855', relief='flat')
activities.pack()


def UpdatePresence():
    global Connected
    if not Connected:
        try:
            RPC.connect()
            print('Connected.')
            Connected = True
        except:
            print('Could not connect.')
            Connected = False
            
    if (Gender.get() == 1):
        RPC.update(details='{}'.format(chosenActivity.get()), state='Difficulty: '+ str('{}'.format(chosenDiff.get())), large_image='d3logo', large_text='D3RPC by SuperZoops', small_image='{}'.format(PortraitListFemale[ClassIndexList[chosenClass.get()]]), small_text='{}'.format(chosenClass.get()), start=time)
    elif (Gender.get() == 0):
        RPC.update(details='{}'.format(chosenActivity.get()), state='Difficulty: '+ str('{}'.format(chosenDiff.get())), large_image='d3logo', large_text='D3RPC by SuperZoops', small_image='{}'.format(PortraitListMale[ClassIndexList[chosenClass.get()]]), small_text='{}'.format(chosenClass.get()), start=time)

def StopPresence():
    global Connected
    if Connected:
        RPC.close()
        Connected = False


UpdateRPC = Button(win,fg='#8EB2BF', bg='#414855', text='Update Presence', command=UpdatePresence)
UpdateRPC.config(highlightthickness=0, relief='flat', activebackground='#414855', activeforeground='white', borderwidth=0)
UpdateRPC.place(relx=0.5, y=375, anchor=CENTER)
StopRPC = Button(win,fg='#8EB2BF', bg='#414855', text='Stop Presence', command=StopPresence)
StopRPC.config(highlightthickness=0, relief='flat', activebackground='#414855', activeforeground='white', borderwidth=0)
StopRPC.place(relx=0.5, y=345, anchor=CENTER)


win.mainloop()