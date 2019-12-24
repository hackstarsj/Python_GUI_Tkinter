from tkinter import Tk,simpledialog,filedialog,colorchooser,messagebox,Frame,Button

def ShowDialogs(method):
    if method==1:
        ret=messagebox.showinfo("Info Title","This is Info Message")
        print(ret)
    if method == 2:
        ret = messagebox.showwarning("Warning Title", "This is Warning Message")
        print(ret)
    if method == 3:
        ret = messagebox.showerror("Error Title", "This is Error Message")
        print(ret)
    if method == 4:
        ret = messagebox.askquestion("Question Title", "This is Question Message")
        print(ret)
    if method == 5:
        ret = messagebox.askyesno("Yes No Title", "This is Yes No Dialog Message")
        print(ret)
    if method == 6:
        ret = messagebox.askyesnocancel("Yes No Cancel Title", "This is Yes No Cancel Dialog Message")
        print(ret)
    if method == 7:
        ret = messagebox.askokcancel("Ok Cancel Title", "This is Ok Cancel Dialog Message")
        print(ret)
    if method == 8:
        ret = messagebox.showinfo("Retry Title", "This is Retry Cancel Dialog Message")
        print(ret)
    if method == 9:
        ret = filedialog.askopenfilename()
        print(ret)
    if method == 10:
        ret = filedialog.askopenfilenames()
        print(ret)
    if method == 11:
        ret = filedialog.asksaveasfile()
        ret.write("Demo Data in File")
        ret.close()
        print(ret)
    if method == 12:
        ret = colorchooser.askcolor()
        print(ret)
    if method == 13:
        ret = simpledialog.askstring("String Title","This Is Simple String Input",parent=window)
        print(ret)
    if method == 14:
        ret = simpledialog.askinteger("Integer Title","This Is Simple Integer Input",parent=window,minvalue=0,maxvalue=100)
        print(ret)
    if method == 15:
        ret = simpledialog.askfloat("Float Title","This Is Simple Float Input",parent=window,minvalue=0.0,maxvalue=100.0)
        print(ret)


window=Tk()
window.title("Dialog Box Example")

frame=Frame(window,bg="#1B2631")
frame.pack(fill="both",expand=True)

button1=Button(frame,text="Info Dialog",padx=10,pady=10,bg="#C0392B",fg="white",command=lambda:ShowDialogs(1))
button1.grid(row=0,column=0,sticky="nsew",padx=10,pady=10)

button2=Button(frame,text="Warning Dialog",padx=10,pady=10,bg="#C0392B",fg="white",command=lambda:ShowDialogs(2))
button2.grid(row=0,column=1,sticky="nsew",padx=10,pady=10)

button3=Button(frame,text="Error Dialog",padx=10,pady=10,bg="#C0392B",fg="white",command=lambda:ShowDialogs(3))
button3.grid(row=0,column=2,sticky="nsew",padx=10,pady=10)

button4=Button(frame,text="Question Dialog",padx=10,pady=10,bg="#C0392B",fg="white",command=lambda:ShowDialogs(4))
button4.grid(row=0,column=3,sticky="nsew",padx=10,pady=10)

# ===================================================
button5=Button(frame,text="Yes No Dialog",padx=10,pady=10,bg="#C0392B",fg="white",command=lambda:ShowDialogs(5))
button5.grid(row=1,column=0,sticky="nsew",padx=10,pady=10)

button6=Button(frame,text="Yes No Cancel Dialog",padx=10,pady=10,bg="#C0392B",fg="white",command=lambda:ShowDialogs(6))
button6.grid(row=1,column=1,sticky="nsew",padx=10,pady=10)

button7=Button(frame,text="Ok Cancel Dialog",padx=10,pady=10,bg="#C0392B",fg="white",command=lambda:ShowDialogs(7))
button7.grid(row=1,column=2,sticky="nsew",padx=10,pady=10)

button8=Button(frame,text="Retry Cancel Dialog",padx=10,pady=10,bg="#C0392B",fg="white",command=lambda:ShowDialogs(8))
button8.grid(row=1,column=3,sticky="nsew",padx=10,pady=10)

# =================================================
button9=Button(frame,text="File Choose Dialog",padx=10,pady=10,bg="#C0392B",fg="white",command=lambda:ShowDialogs(9))
button9.grid(row=2,column=0,sticky="nsew",padx=10,pady=10)

button10=Button(frame,text="Multi File Choose Dialog",padx=10,pady=10,bg="#C0392B",fg="white",command=lambda:ShowDialogs(10))
button10.grid(row=2,column=1,sticky="nsew",padx=10,pady=10)

button10=Button(frame,text="File Save Dialog",padx=10,pady=10,bg="#C0392B",fg="white",command=lambda:ShowDialogs(11))
button10.grid(row=2,column=2,sticky="nsew",padx=10,pady=10)

button11=Button(frame,text="Color Pick Dialog",padx=10,pady=10,bg="#C0392B",fg="white",command=lambda:ShowDialogs(12))
button11.grid(row=2,column=3,sticky="nsew",padx=10,pady=10)

# ========================================================
button12=Button(frame,text="String Input Dialog",padx=10,pady=10,bg="#C0392B",fg="white",command=lambda:ShowDialogs(13))
button12.grid(row=3,column=0,sticky="nsew",padx=10,pady=10)

button13=Button(frame,text="Integer Input Dialog",padx=10,pady=10,bg="#C0392B",fg="white",command=lambda:ShowDialogs(14))
button13.grid(row=3,column=1,sticky="nsew",padx=10,pady=10)

button14=Button(frame,text="Float Input Dialog",padx=10,pady=10,bg="#C0392B",fg="white",command=lambda:ShowDialogs(15))
button14.grid(row=3,column=2,sticky="nsew",padx=10,pady=10)

# ========================================================

frame.grid_columnconfigure(0,weight=1)
frame.grid_columnconfigure(1,weight=1)
frame.grid_columnconfigure(2,weight=1)
frame.grid_columnconfigure(3,weight=1)

window.mainloop()

