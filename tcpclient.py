import socket

SERVER="127.0.1.1"

PORT = 7777
HEADER = 64
FORMAT = "utf-8"
addr=(SERVER,PORT)
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(addr)

def sendmsg(msg):
    message= msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length +=b' '* (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    # print(client.recv(HEADER))
