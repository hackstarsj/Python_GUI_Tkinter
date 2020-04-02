from tkinter import Tk,Label,Button,Frame,simpledialog
from tkinter.ttk import Progressbar
from PIL import Image,ImageTk
import requests
import re
import os
import threading

def PassUrlData():
    url=simpledialog.askstring("Enter Url","Please Enter Your Download URL")
    downloadThread=threading.Thread(target=lambda:addDownloadItem(url))
    downloadThread.start()

def getStandardSize(size):
    itme=['bytes','KB','MB','GB','TB']
    for x in itme:
        if size < 1024.0:
            return  "%3.1f %s" % (size,x)
        size/=1024.0
    return size

def addDownloadItem(url):


    if url!=None:
        req=requests.get(url,stream=True)

        if "Content-Length" in req.headers:
            total_size=req.headers['Content-Length']
        else:
            total_size=None



        if "Content-Disposition" in req.headers.keys():
            fname=re.findall("filename=(.+)",req.headers["Content-Disposition"])[0]
        else:
            fname=url.split("/")[-1]

        fname.replace(" ","")
        frame2=Frame(frame,bg="#E67E22")
        img=Image.open("file_icon.png")
        render=ImageTk.PhotoImage(img)

        label=Label(frame2,image=render,bg="#E67E22")
        label.image=render
        label.grid(row=0,column=0,rowspan=2)

        title=Label(frame2,text=fname,padx=5,bg="#E67E22",fg="white",anchor="w")
        title.config(font=("Arial","15"))
        title.grid(row=0,column=1,sticky="nsew")

        progress=Progressbar(frame2)
        progress['value']=0
        progress.grid(row=1,column=1,sticky="nsew")

        labelPercentage=Label(frame2,text="0 %",padx="5",anchor="w",bg="#E67E22",fg="white")
        labelPercentage.grid(row=0,column=2)
        labelsize=Label(frame2,text="0 KB",padx="5",anchor="w",bg="#E67E22",fg="white")
        labelsize.grid(row=1,column=2)

        frame2.pack(fill="x")
        frame2.columnconfigure(1,weight=1)

        with open(fname,"wb") as fileobj:
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    fileobj.write(chunk)
                    current_size=os.path.getsize(fname)
                    labelsize.config(text=str(getStandardSize(current_size)))

                    if total_size!=None:
                        percentg=round((int(current_size)/int(total_size))*100)
                        labelPercentage.config(text=str(percentg)+" %")
                        progress['value']=percentg
                    else:
                        percentg="Infinte"
                        progress.config(mode="indeterminate")
                        progress.start()
                        labelPercentage.config(text=str(percentg)+" %")




        if total_size!=None:
            current_size=os.path.getsize(fname)
            labelsize.config(text=str(getStandardSize(current_size)))
            labelPercentage.config(text=str(percentg) + " %")
            percentg=round((int(current_size)/int(total_size))*100)
            progress['value']=percentg
        else:
            current_size=os.path.getsize(fname)
            labelsize.config(text=str(getStandardSize(current_size)))
            labelPercentage.config(text="100 %")
            progress['value'] = 100






window=Tk()
window.geometry("800x500")
frame=Frame(window,bg="#212F3C")
frame.pack(fill="both",expand=True)


rowframe=Frame(frame,bg="#F4D03F")
button=Button(rowframe,text="Add Download URL",bg="#27AE60",fg="white",padx=10,pady=10,activebackground="#1F618D",activeforeground="white",command=PassUrlData)
button.grid(row=0,column=0,sticky="nsew",padx=10,pady=10)
button1=Button(rowframe,text="Exit Program",bg="#C0392B",fg="white",padx=10,pady=10,activebackground="#1F618D",activeforeground="white")
button1.grid(row=0,column=1,sticky="nsew",padx=10,pady=10)
rowframe.grid_columnconfigure(0,weight=1)
rowframe.grid_columnconfigure(1,weight=1)

rowframe.pack(fill="x")

window.mainloop()