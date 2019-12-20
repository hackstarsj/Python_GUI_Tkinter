from tkinter import Tk,Menu,Menubutton,Frame,LEFT,W,X,RAISED,IntVar,StringVar,DISABLED

window=Tk()

def openFile():
    print("Open")

def newFile():
    print("New")

def exitMenu():
    print("Exit")

def delFile():
    print("Delete")

def closeFile():
    print("Close")

def exitFile():
    print("Exit")

def submenu1_fun():
    print("submenu1_fun")

def togglePhpFun():
    print("PHP : "+str(variablephp.get()))

def togglePythonFun():
    print("Python "+str(variablepython.get()))

def toggleJavaFun():
    print("Java "+str(variablejava.get()))

def toggleRadio():
    print("Radio : "+str(radio_val.get()))

frame=Frame(window,relief=RAISED,borderwidth=1)
frame.pack(fill=X)

#First Menu
first_menu=Menubutton(frame,text="File")
first_menu.pack(padx=3,pady=3,side=LEFT)
first_menu.menu=Menu(first_menu,tearoff=False)
first_menu.menu.add_command(label="New",command=newFile)
first_menu.menu.add_command(label="Open",command=openFile)
first_menu.menu.add("separator")
first_menu.menu.add_command(label="Exit",command=exitMenu)
first_menu['menu']=first_menu.menu

#second Menu
second_menu=Menubutton(frame,text="Edit")
second_menu.pack(padx=3,pady=3,side=LEFT)
second_menu.menu=Menu(second_menu,tearoff=False)
second_menu.menu.add_command(label="DELETE ALL",command=delFile)
second_menu.menu.add_command(label="CLOSE",command=closeFile)
second_menu.menu.add("separator")
second_menu.menu.add_command(label="Exit",command=exitFile)
second_menu['menu']=second_menu.menu


#adding submenu
thirdmenu=Menubutton(frame,text="Submenu")
thirdmenu.pack(padx=3,pady=3,side=LEFT)

thirdmenu.menu=Menu(thirdmenu,tearoff=False)

thirdmenu.menu.submenu1=Menu(thirdmenu.menu,tearoff=False)
thirdmenu.menu.submenu1.add_command(label="Submenu Menu 1",command=submenu1_fun)
thirdmenu.menu.submenu1.add_command(label="Submenu Menu 2")
thirdmenu.menu.submenu1.add_command(label="Submenu Menu 3")
thirdmenu.menu.add_cascade(label="Submenu 1",menu=thirdmenu.menu.submenu1)

thirdmenu.menu.submenu2=Menu(thirdmenu.menu,tearoff=False)
thirdmenu.menu.submenu2.add_command(label="Submenu Menu 4")
thirdmenu.menu.submenu2.add_command(label="Submenu Menu 5")
thirdmenu.menu.submenu2.add_command(label="Submenu Menu 6")
thirdmenu.menu.add_cascade(label="Submenu 2",menu=thirdmenu.menu.submenu2)
thirdmenu['menu']=thirdmenu.menu
#end submenu


#adding check menu

fourth_menu=Menubutton(frame,text="Checkbox")
fourth_menu.pack(padx=3,pady=3,side=LEFT)

fourth_menu.menu=Menu(fourth_menu,tearoff=False)
variablephp=IntVar()
variablepython=IntVar()
variablejava=IntVar()
fourth_menu.menu.add_checkbutton(label="Show PYTHON",offvalue=0,onvalue=1,variable=variablepython,command=togglePythonFun)
fourth_menu.menu.add_checkbutton(label="Show PHP",offvalue=0,onvalue=1,variable=variablephp,command=togglePhpFun)
fourth_menu.menu.add_checkbutton(label="Show JAVA",offvalue=0,onvalue=1,variable=variablejava,command=toggleJavaFun)
fourth_menu['menu']=fourth_menu.menu
#end check menu

#radio menu
radio_val=StringVar()
fifth_menu=Menubutton(frame,text="Radio Menu")
fifth_menu.pack(side=LEFT,padx=3,pady=3)
fifth_menu.menu=Menu(fifth_menu,tearoff=False)
fifth_menu.menu.add_radiobutton(label="Show All",value="ShowAll",variable=radio_val,command=toggleRadio)
fifth_menu.menu.add_radiobutton(label="Show None",value="ShowNone",variable=radio_val,command=toggleRadio)
fifth_menu['menu']=fifth_menu.menu

sixth_menu=Menubutton(frame,text="Disabled Menu")
sixth_menu.pack(side=LEFT,padx=3,pady=3)
sixth_menu.menu=Menu(sixth_menu,tearoff=False)
sixth_menu.menu.add_command(label="Disabled Item",state=DISABLED)
sixth_menu['menu']=sixth_menu.menu

window.mainloop()