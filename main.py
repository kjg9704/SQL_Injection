import tkinter
import requests

# url = 'https://webhacking.kr/challenge/bonus-1/index.php'
# url = 'http://104.197.42.200/member/login_ok.php'
# cookies = {'PHPSESSID': 'd42rp6qqm5fhj3dmn3830g74pq'}


# Error based SQL Injection
def errorInjection():
    # 창 화면 설정
    window = tkinter.Toplevel(mainWindow)
    window.title("SQL Injection Tools")
    window.geometry("480x400+100+100")
    window.resizable(False, False)

    label2 = tkinter.Label(window, text="이름 입력")
    label2.pack()

    name = tkinter.StringVar()
    textbox = tkinter.Entry(window, width=12, textvariable=name)
    textbox.pack()

    labelNew = tkinter.Label(window, text="")
    labelNew.pack()

    # 창 내에 존재하는 테두리
    labelframe2 = tkinter.LabelFrame(window, padx=100, pady=5)
    labelframe2.place(x=30, y=110)

    getDBbtn = tkinter.Button(window, text="Get Databases", command=getDB, width=11, height=1)
    getDBbtn.place(x=360, y=228)

    urlLabel = tkinter.Label(window, text="URL")
    urlLabel.place(x=30, y=230)

    urlbox = tkinter.Entry(window, width=40, state="disabled")
    urlbox.place(x=70, y=230)
    #
    # Get Tables Button
    getTbtn = tkinter.Button(window, text="Get Tables", command=getDatabase, width=11)
    getTbtn.place(x=360, y=258)

    dbLabel = tkinter.Label(window, text="Database")
    dbLabel.place(x=30, y=260)

    dbTbox = tkinter.Entry(window, width=37, state="disabled")
    dbTbox.place(x=90, y=260)
    #
    # Get Columns Button
    getCbtn = tkinter.Button(window, text="Get Columns", command=getDatabase, width=11)
    getCbtn.place(x=360, y=288)

    tablLabel = tkinter.Label(window, text="Table Name")
    tablLabel.place(x=30, y=290)

    tableTbox = tkinter.Entry(window, width=34, state="disabled")
    tableTbox.place(x=110, y=290)
    #
    # Get Dump Button
    getDbtn = tkinter.Button(window, text="Dump", command=getDatabase, width=11)
    getDbtn.place(x=360, y=318)

    columnLabel = tkinter.Label(window, text="Column's Name")
    columnLabel.place(x=30, y=320)

    columnTbox = tkinter.Entry(window, width=31, state="disabled")
    columnTbox.place(x=130, y=320)

    window.mainloop()

global name
global label2
label2.configure(foreground='blue')
global labelNew
labelNew.configure(name.get())

    # # Radio Button
    # RadioVariety_1 = tkinter.StringVar()
    # RadioVariety_1.set("미선택")
    # CheckVariety_1 = tkinter.IntVar()
    # CheckVariety_2 = tkinter.IntVar()
    # CheckVariety_3 = tkinter.IntVar()
    #
    # # 라벨 프레임(창 내 테두리)에 담겨져 있는 체크 버튼
    # checkbutton1 = tkinter.Checkbutton(labelframe2, text="Using ByPass WAF", variable=CheckVariety_1)
    # checkbutton2 = tkinter.Checkbutton(labelframe2, text="Using RandomAgent", variable=CheckVariety_2)
    # checkbutton3 = tkinter.Checkbutton(labelframe2, text="Enable This Option", variable=CheckVariety_3)
    #
    # # 체크 버튼 생성 및 위치 조정
    # checkbutton1.pack()
    # checkbutton2.pack()
    # checkbutton3.pack()




def getDatabase():
    labelNew.configure(text='' + name.get())


def blindInjection():

    # 창 화면 설정
    window = tkinter.Toplevel(mainWindow)
    window.title("SQL Injection Tools")
    window.geometry("480x400+100+100")
    window.resizable(False, False)

    # Label Frame Settings
    labelframe = tkinter.LabelFrame(window, padx=100, pady=5)
    labelframe.place(x=30, y=110)

    # Get Databases Button
    getDBbtn = tkinter.Button(window, text="Get Databases", width=11, height=1)
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

    # Get Columns Button
    getCMbtn = tkinter.Button(window, text="Get Columns", command=getDatabase, width=11)
    getCMbtn.place(x=360, y=288)

    tableLabel = tkinter.Label(window, text="Table Name")
    tableLabel.place(x=30, y=290)

    tableTbox = tkinter.Entry(window, width=34, state="disabled")
    tableTbox.place(x=110, y=290)

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
    checkbutton3=tkinter.Checkbutton(labelframe, text="Enable This Option", variable=CheckVariety_3)

    # Button Settings
    checkbutton1.pack()
    checkbutton2.pack()
    checkbutton3.pack()

    window.mainloop()

def timeInjection():
    abc = 1

def stackedInjection():
    abc = 1

mainWindow = tkinter.Tk()
mainWindow.title("SQL Injection Tools")
mainWindow.resizable(False, False)

blindInjectionBtn = tkinter.Button(mainWindow, text="Blind SQL Injection", command=blindInjection)
blindInjectionBtn.grid(row=0, column=0)
errorInjectionBtn = tkinter.Button(mainWindow, text="Error Based SQL Injection", command=errorInjection)
errorInjectionBtn.grid(row=0, column=1)
timeInjectionBtn = tkinter.Button(mainWindow, text="Time Based SQL Injection", command=timeInjection)
timeInjectionBtn.grid(row=1, column=0)
stackedInjectionBtn = tkinter.Button(mainWindow, text="Error Based SQL Injection", command=stackedInjection)
stackedInjectionBtn.grid(row=1, column=1)

mainWindow.mainloop()