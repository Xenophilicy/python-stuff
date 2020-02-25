import socket
import time

HOST = "127.0.0.1"
PORT = 45000

def createSocket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def runClient(HOST):
    print("Connecting to host...")
    #try:
    sock = createSocket()
    sock.connect((HOST,PORT))
    print(f"Connected to host {HOST}, {PORT}...")
    msg = input("Enter string to send:\n>>")
    #try:
    ping = time.monotonic()
    sock.sendall(msg.encode("utf-8"))
    print("Sent data successfully...")
    data = sock.recv(1024)
    delta = round(time.monotonic() - ping,2)*1000
    print(f"Received response in {delta} ms")
    #except Exception:
    #    print("Sending message failed!")
    #except Exception:
    #    print("Error connecting to host!")

runClient(HOST)
input("Press Enter to continue...")