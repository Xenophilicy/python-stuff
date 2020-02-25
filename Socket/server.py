import socket

HOST = "127.0.0.1"
PORT = 45000

def bindSocket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Binding socket...")
    try:
        sock.bind((HOST, PORT))
        print("Socket bound successfully...")
        return sock
    except Exception:
        print("Socket binding failed!")
        return False

def sockListen(sock):
        #try:
        sock.listen()
        print(f"Listening on port {PORT}...")
        clientConn, addr = sock.accept()
        print("Accepted new connection...")
        try:
            with clientConn:
                print(f"Connected to client {addr[0]}, {addr[1]}")
                while True:
                    data = clientConn.recv(1024)
                    if not data:
                        break
                    print(f"Received: {data.decode()}")
                    clientConn.send(data)
        except ConnectionResetError:
            print("Error: Connection was reset!")
            sockListen(sock)
            #except Exception:
            #    print("Error begin listening!")

sock = bindSocket()
if not socket == False:
    sockListen(sock)
input("Press Enter to continue...")