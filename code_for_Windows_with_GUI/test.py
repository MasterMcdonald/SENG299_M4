"""
client clode
Druft Author: Haotian Shen, Zelan Xiang
Editor: Zelan Xiang
GUI: Zelan Xiang
"""
import socket
import threading
from ScrolledText import ScrolledText
from Tkinter import *
def send(messages):
    """
    the sending method
    """
    #TD.insert(END, "[You]: " + messages)
    input_split = messages.split(" ")
    if len(input_split) > 1:
        msg = str(input_split[1:])
    if input_split[0] == "/quit":
        S.close()
        quit()
    elif input_split[0] == "/create":
        action = '01'
    elif input_split[0] == "/delete":
        action = '02'
    elif input_split[0] == "/join":
        action = '03'
    elif input_split[0] == "/block":
        action = '04'
    elif input_split[0] == "/unblock":
        action = '05'
    elif input_split[0] == "/set_alias":
        action = '06'
    else:
        action = '00'
        msg = input_split[0:]
        msg = reduce((lambda x, y: x+' '+y), msg)
        TD.insert(END, "[You]: "+msg)
    message = action + msg
    S.send(message)
    TI.delete("0.0", "end")

def recieve():
    """
    recieve method
    """
    try:
        data = S.recv(1024)
        if data:
            TD.insert(END, data)
        else:
            TD.insert(END, 'disconnect')
    except socket.error:
        pass

def info():
    """
    This is a info
    """
    info_m = '***This is chat system ***\n ***It is not perfect, but it works, mostly.***\n'
    TD.insert(END, info_m)

HOST = socket.gethostname()
PORT = 10000
ADDRESS = (HOST, PORT)
MSG = ''
S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
S.connect(ADDRESS)

TOPP = Tk()
TOPP.title('Chatus')
MB = Menu(TOPP)
FM = Menu(MB, tearoff=0)
#FM.add_command(label='Start', command=lambda: recieve())
FM.add_command(label='Exit', command=TOPP.quit)
MB.add_cascade(label='Main', menu=FM)

HE = Menu(MB, tearoff=0)
HE.add_command(label='Info', command=lambda: info())
MB.add_cascade(label='Help', menu=HE)

TD = ScrolledText(TOPP, width=37, height=15, font=('Arial', 13), fg='black', bg='white')
TD.pack(expand=1, padx=5, pady=5, side=TOP)
FR = Frame(TOPP)

TI = ScrolledText(FR, width=25, height=5, font=('Arial', 13), fg='black', bg='white')
TI.pack(expand=1, padx=5, pady=5, side=RIGHT)

FRL = Frame(FR)
SB = Button(FRL, text='SEND', width=10, height=2, font=('Arial', 13, "bold"),
            fg='white', bg='DarkOrange', command=lambda: send(TI.get("0.0", "end")))
SB.pack(side=TOP)
SB2 = Button(FRL, text='REFRESH', width=10, height=2, font=('Arial', 13, "bold"),
            fg='white', bg='DarkOrange', command=lambda: recieve())
SB2.pack(side=BOTTOM)
FRL.pack(side=LEFT)
FR.pack(side=BOTTOM)

TOPP.config(menu=MB)
TOPP.mainloop()
