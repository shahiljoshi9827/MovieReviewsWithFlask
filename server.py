import socket
server_socket = socket.socket()
ip = socket.gethostbyname(socket.gethostname())
port =1234
server_socket.bind((ip,port))
server_socket.listen()
print("Server is listening to theri client")
client_socket,client_addr = server_socket.accept()
print("Got Connected With Client")
while True:
    smsg = input("Server --> ")
    client_socket.send(smsg.encode())
    if smsg.strip().lower() == "bye":
        print("Socket was closed by You!!!")
        client_socket.close()
        server_socket.close()
        break
    msg = client_socket.recv(1024)
    if msg.decode().lower().strip() == 'bye':
        print("Socket was closed by the Client")
        break
        client_socket.close()
        server_socket.close()
    else:
        print("Client --> ",msg.decode())
        
