import socket
from tkinter import *

def hosting(sq, tkq):
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    s = socket.socket()
    s.bind((hostname, 5000))

    hostingText = IPAddr + "\nwaiting for connection"

    tkq.put(hostingText)

    s.listen(2)
    conn, address = s.accept()

    tkq.put("close")

    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection

def connecting(sq, tkq):
    IPAddr = sq.get()
    port = 5000
    client = socket.socket()
    client.connect((IPAddr, port))
    
    print("did I at least make it here?")

    message = input(" -> ") # taking input
    while message.lower().strip() != "bye":
        client.send(message.encode()) #send message
        data = client.recv(1024).decode()

        print("Recieved from server: " + data)

        message = input(" -> ")

    client.close()

def gettingStarted(sq, tkq):
    type = sq.get()
    if(type == "host"):
        hosting(sq, tkq)
    elif(type == "connect"):
        connecting(sq, tkq)
    else:
        print("should never get here ")
        return