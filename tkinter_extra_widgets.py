from tkinter import Tk,Frame,BOTH,LEFT,Listbox,Button,ANCHOR,X,Text
from tkinter.ttk import Combobox,Progressbar

def getValue():
    print("Combo : "+str(combobox.get()))
    print("Text : "+str(textbox.get("1.0","end-1c")))
    print("List Box : "+str(listbox.get(ANCHOR)))

def onChangeValue(object):
    print("Value "+str(combobox.get()))

def IncreaseValue():
    progress['value']=progress['value']+1

def decreaseValue():
    progress['value']=progress['value']-1

window=Tk()
#window.geometry("400x300")
window.title("Extra Widgets")

#combobox
frame=Frame(window)
frame.pack(fill=X)

combobox=Combobox(frame)
items=(1,2,3,"Hello","World")
combobox['values']=items
combobox.current(1)
combobox.bind("<<ComboboxSelected>>",onChangeValue)
combobox.pack(side=LEFT)
#end combo box

#listbox
listbox=Listbox(frame)
listbox.insert(0,"Rahul")
listbox.insert(1,"Rajiv")
listbox.insert(2,"Aman")
listbox.insert(3,"Vishal")
listbox.pack(side=LEFT)

textbox=Text(frame)
textbox.pack(side=LEFT)

button_get_value=Button(frame,text="Get Value",command=getValue)
button_get_value.pack(side=LEFT)

frame2=Frame(window)
frame2.pack()

progress=Progressbar(frame2,length=100)
progress.pack(side=LEFT)
progress['value']=50

button1=Button(frame2,text="Increase",command=IncreaseValue)
button1.pack(side=LEFT)

button1=Button(frame2,text="Increase",command=decreaseValue)
button1.pack(side=LEFT)

window.mainloop()