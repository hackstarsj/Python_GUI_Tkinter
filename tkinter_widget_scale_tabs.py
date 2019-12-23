from tkinter import Scale,Tk,Frame,Label
from tkinter.ttk import Notebook,Entry

def getValue(value):
    print(value)

def getValue2(value):
    print(scale2.get())



window=Tk()
window.title("Scale,Tabs,Table Example")
window.geometry("600x400")

scale1=Scale(window,label="Simple Scale",from_=0,to=100,command=getValue,fg="white",bg="green",activebackground="red",troughcolor="orange")
scale1.pack(fill="x")

scale2=Scale(window,label="Simple Scale Horizontal",from_=0,to=100,command=getValue2,fg="white",bg="green",activebackground="red",troughcolor="orange",orient="horizontal")
scale2.pack(fill="x")

frame2=Frame(window)
frame2.pack(fill="both")

tablayout=Notebook(frame2)

#tab1
tab1=Frame(tablayout)
tab1.pack(fill="both")

#input box Table
for row in range(5):
    for column in range(6):
        if row==0:
            label = Entry(tab1, text="Heading : " + str(column))
            label.config(font=('Arial',14))
            label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
            tab1.grid_columnconfigure(column, weight=1)
        else:
            label=Entry(tab1,text="Row : "+str(row)+" , Column : "+str(column))
            label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
            tab1.grid_columnconfigure(column,weight=1)

tablayout.add(tab1,text="TAB 1")

#tab2
tab1=Frame(tablayout)
tab1.pack(fill="both")

#adding table into tab

for row in range(5):
    for column in range(6):
        if row==0:
            label = Label(tab1, text="Heading : " + str(column), bg="white", fg="black", padx=3,
                          pady=3)
            label.config(font=('Arial',14))
            label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
            tab1.grid_columnconfigure(column, weight=1)
        else:
            label=Label(tab1,text="Row : "+str(row)+" , Column : "+str(column),bg="black",fg="white",padx=3,pady=3)
            label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
            tab1.grid_columnconfigure(column,weight=1)

tablayout.add(tab1,text="TAB 1")

tablayout.pack(fill="both")

window.mainloop()