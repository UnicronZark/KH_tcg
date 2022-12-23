from tkinter import *
from threading import Thread
import time

def mainLoop(w):
    w.mainloop()

def hostingGui(sq, tkq, window, hostB, connectB):
    sq.put("host")
    hostB.forget()
    connectB.forget()

    hostingText = tkq.get()
    hostLabel = Label(window, text=hostingText)
    hostLabel.pack()
    window.update()

    print(tkq.get())

    

def connectToIP(sq, tkq, window, conE):
    IP = conE.get()
    window.destroy()
    sq.put(IP)

def connectingGui(sq, tkq, window, hostB, connectB):
    sq.put("connect")
    hostB.forget()
    connectB.forget()

    conLabel = Label(window, text="Enter Code")
    conLabel.pack(side="left")
    conE = Entry(window)
    conE.pack(side="left")
    conB = Button(window, text="Connect", command=lambda: connectToIP(sq, tkq, window, conE))
    conB.pack(side="left")

def changingGui(sq, tkq):
    window = tkq.get()

    hostB = Button(window, text="Host", command=lambda: hostingGui(sq, tkq, window, hostB, connectB))
    hostB.pack()  
    connectB = Button(window, text="Connect", command=lambda: connectingGui(sq, tkq, window, hostB, connectB))
    connectB.pack()


def openGui(tkq):

    window = Tk()

    window.title("KHTCG")

    tkq.put(window)
    window.mainloop()