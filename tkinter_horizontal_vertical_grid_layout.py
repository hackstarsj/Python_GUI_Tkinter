from tkinter import Tk,Frame,Label

mainwindow=Tk()

mainframe=Frame(mainwindow,bg="red")
mainframe.pack(fill="both",expand=True)

label=Label(mainframe,text="Vertical Frame Example",bg="black",fg="white",padx=5,pady=5)
label.config(font=("Arial",18))
label.pack(fill="x")
#vertical layout with data
verticalFrame=Frame(mainframe,bg="blue")

item1=Label(verticalFrame,text="Item 1",bg="orange",padx=10,pady=10,fg="white")
item1.pack(fill="x",padx=10,pady=10)

item1=Label(verticalFrame,text="Item 2",bg="yellow",padx=10,pady=10,fg="black")
item1.pack(fill="x",padx=10,pady=10)

item1=Label(verticalFrame,text="Item 3",bg="green",padx=10,pady=10,fg="white")
item1.pack(fill="x",padx=10,pady=10)

verticalFrame.pack(fill="x")
#end vertical

#horizontal
label=Label(mainframe,text="Horizontal Frame Example",bg="black",fg="white",padx=5,pady=5)
label.config(font=("Arial",18))
label.pack(fill="x")
horizontal_frame=Frame(mainframe)

label1=Label(horizontal_frame,text="Item 1 in Horizontal",bg="red",fg="white",padx=10,pady=10)
label1.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")
label1=Label(horizontal_frame,text="Item 2 in Horizontal",bg="red",fg="white",padx=10,pady=10)
label1.grid(row=0,column=1,padx=10,pady=10,sticky="nsew")
label1=Label(horizontal_frame,text="Item 3 in Horizontal",bg="red",fg="white",padx=10,pady=10)
label1.grid(row=0,column=2,padx=10,pady=10,sticky="nsew")
label1=Label(horizontal_frame,text="Item 4 in Horizontal",bg="red",fg="white",padx=10,pady=10)
label1.grid(row=0,column=3,padx=10,pady=10,sticky="nsew")

horizontal_frame.grid_columnconfigure(0,weight=1)
horizontal_frame.grid_columnconfigure(1,weight=1)
horizontal_frame.grid_columnconfigure(2,weight=1)
horizontal_frame.grid_columnconfigure(3,weight=1)
horizontal_frame.pack(fill="x")

#end horizontal

#grid data
label=Label(mainframe,text="Grid Frame Example",bg="black",fg="white",padx=5,pady=5)
label.config(font=("Arial",18))
label.pack(fill="x")

grid_frame=Frame(mainframe)
for row in range(10):
    for column in range(10):
        label=Label(grid_frame,text="Item ",bg="red",fg="white",padx=5,pady=5)
        label.grid(row=row,column=column,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(column,weight=1)

grid_frame.pack(fill="x")



mainwindow.mainloop()