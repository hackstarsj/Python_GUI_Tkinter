from tkinter import Tk,Button,Label,Entry,LEFT,StringVar,W,N,E,S,Frame,Radiobutton,Checkbutton,IntVar,ACTIVE

window=Tk()
usernameval=StringVar()
passwordval=StringVar()

def sumbmitForm():
    print("Username : "+usernameval.get())
    print("Password : "+passwordval.get())
    print("Gender : "+value_radio.get())
    if val_1.get()==1:
        print("PHP : Yes")
    else:
        print("PHP : No")

    if val_2.get()==1:
        print("JAVA : Yes")
    else:
        print("JAVA : No")

    if val_3.get()==1:
        print("PYTHON : Yes")
    else:
        print("PYTHON : No")
    print("Submit")

label_username=Label(window,text="Username : ").pack(padx=15,pady=5,anchor=W)

username=Entry(window,textvariable=usernameval).pack(padx=15,pady=5,anchor=W)

#for setting default value
usernameval.set("Hello")

label_password=Label(window,text="Password : ").pack(padx=15,pady=5,anchor=W)
password=Entry(window,textvariable=passwordval).pack(padx=15,pady=5,anchor=W)
passwordval.set("World")


value_radio=StringVar()
radio_male=Radiobutton(window,text="Male",value="M",variable=value_radio,indicatoron=0,width=10).pack(padx=15,pady=5,anchor=W)
radio_female=Radiobutton(window,text="Female",value="F",variable=value_radio,indicatoron=0,width=10).pack(padx=15,pady=5,anchor=W)

#hiding radio button circle use indicatoron=0
value_radio.set("M")

val_1=IntVar()
val_2=IntVar()
val_3=IntVar()

check_button_1=Checkbutton(window,text="PHP",variable=val_1).pack()
check_button_2=Checkbutton(window,text="JAVA",variable=val_2).pack()
check_button_3=Checkbutton(window,text="Python",variable=val_3).pack()
val_1.set(1)


submit=Button(window,text="Submit",command=sumbmitForm).pack(padx=15,pady=5,anchor=W)


window.mainloop()