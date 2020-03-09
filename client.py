import socket
client_socket = socket.socket()
ip = socket.gethostbyname(socket.gethostname())
port =1234
client_socket.connect((ip,port))
print("Got Connected With Server")
while True:
    smsg = client_socket.recv(1024)
    if smsg.decode().lower().strip() == 'bye':
        print("Socket was closed by the server")
        break
        client_socket.close()
    else:
        print("Server --> ",smsg.decode())
        msg = input("Client --> ")
        client_socket.send(msg.encode())
        if msg.strip().lower() == "bye":
            print("Socket was closed by You!!!")
            client_socket.close()
            break