from tkinter import Tk,Label,NORMAL,ACTIVE,DISABLED,FLAT,SUNKEN,RAISED,GROOVE,RIDGE

window=Tk()
label=Label(window,text="Hello GUI Tkinter Left",width=20,height=5,state=NORMAL)
label.pack(side="left",padx=10,pady=10)
label2=Label(window,text="Hello GUI Tkinter Right",width="20",height="5",state=ACTIVE)
label2.pack(side="right")
label3=Label(window,text="Hello GUI Tkinter Top",width="20",height="5",state=DISABLED)
label3.pack(side="top")
label4=Label(window,text="Hello GUI Tkinter Bottom",fg="yellow",bg="black",width=20,height=3)
label4.pack(side="bottom",padx=20,pady=20)

label5=Label(window,text="Border Decorate SUNSKEN",bg="red",fg="white",width=30,height=5,relief=SUNKEN,bd=1,cursor="tcross")
label5.pack(padx=5,pady=5)
label6=Label(window,text="Border Decorate FLAT",bg="red",fg="white",width=30,height=5,relief=FLAT,bd=2,cursor="hand2")
label6.pack(padx=5,pady=5)
label7=Label(window,text="Border Decorate RAISED",bg="red",fg="white",width=30,height=5,relief=RAISED,bd=3,cursor="heart")
label7.pack(padx=5,pady=5)
label8=Label(window,text="Border Decorate GROOVE",bg="red",fg="white",width=30,height=5,relief=GROOVE,bd=4,cursor="pencil")
label8.pack(padx=5,pady=5)
label9=Label(window,text="Border Decorate RIDGE",bg="red",fg="white",width=30,height=5,relief=RIDGE,bd=5,cursor="tcross")
label9.pack(padx=5,pady=5)



window.mainloop()