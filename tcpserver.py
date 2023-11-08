import socket
import sys
import threading

HOST=socket.gethostbyname(socket.gethostname())
PORT=7777
ADDR = (HOST,PORT)
HEADER =64
FORMAT="utf-8"
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)






def handle_client(connection,addr):
    print("NEW CONNECTION: {addr} connected")
    connected = True
    while connected:
        msg_length=connection.recv(HEADER).decode(FORMAT)
        print(msg_length)
        if msg_length:
            msg_length=int(msg_length)
            msg=connection.recv(msg_length).decode(FORMAT)
            # print(msg)
            if msg=="DISCONNECTED":
                connected=False
            print(f"{addr} : {msg}")
            # connection.send("MESSAGE RECEIVED".encode(FORMAT))
    connection.close()
def start():
    server.listen()
    print("SERVER IS LISTENING {}".format(server))
    while True:
        connection, addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(connection,addr)) 
        thread.start()
        # print(f"ACTIVE CONNECTIONS {threading.activeCount-1}")



start()
print("SERVER IS LISTENING ")
