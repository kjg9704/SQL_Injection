import tkinter

window = tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("480x400+100+100")
window.resizable(True, True)


def getDatabase():
    labelNew.configure(text='' + name.get())

# Label Frame Settings
labelframe = tkinter.LabelFrame(window, padx=100, pady=5)
labelframe.place(x=30, y=150)

labelframe2 = tkinter.LabelFrame(window, padx=100, pady=5)
labelframe2.place(x=30, y=110)


#
# Get Databases Button
getDBbtn = tkinter.Button(window, text="Get Databases", command=getDatabase, width=11, height=1)
getDBbtn.place(x=360, y=228)

urlLabel = tkinter.Label(window, text="URL")
urlLabel.place(x=30, y=230)

urlTbox = tkinter.Entry(window, width=40, state="disabled")
urlTbox.place(x=70, y=230)
#
# Get Tables Button
getTBbtn = tkinter.Button(window, text="Get Tables", command=getDatabase, width=11)
getTBbtn.place(x=360, y=258)

dbLabel = tkinter.Label(window, text="Database")
dbLabel.place(x=30, y=260)

dbTbox = tkinter.Entry(window, width=37, state="disabled")
dbTbox.place(x=90, y=260)
#
# Get Columns Button
getCMbtn = tkinter.Button(window, text="Get Columns", command=getDatabase, width=11)
getCMbtn.place(x=360, y=288)

tableLabel = tkinter.Label(window, text="Table Name")
tableLabel.place(x=30, y=290)

tableTbox = tkinter.Entry(window, width=34, state="disabled")
tableTbox.place(x=110, y=290)
#
# Get Dump Button
getDPbtn = tkinter.Button(window, text="Dump", command=getDatabase, width=11)
getDPbtn.place(x=360, y=318)

columnLabel = tkinter.Label(window, text="Column's Name")
columnLabel.place(x=30, y=320)

columnTbox = tkinter.Entry(window, width=31, state="disabled")
columnTbox.place(x=130, y=320)

# Radio Button
RadioVariety_1 = tkinter.StringVar()
RadioVariety_1.set("미선택")
CheckVariety_1=tkinter.IntVar()
CheckVariety_2=tkinter.IntVar()
CheckVariety_3=tkinter.IntVar()

checkbutton1=tkinter.Checkbutton(labelframe, text="Using ByPass WAF", variable=CheckVariety_1)
checkbutton2=tkinter.Checkbutton(labelframe, text="Using RandomAgent", variable=CheckVariety_2)
checkbutton3=tkinter.Checkbutton(labelframe2, text="Enable This Option", variable=CheckVariety_3)

# Button Settings
checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()



window.mainloop()