import socket
try:
     mysocket = socket.socket()
     server_ip = '127.0.0.1'
     server_port = 1234
     server_details = (server_ip , server_port)
     mysocket.connect(server_details)
     print("connection establish...")
     while True:
         serverData = mysocket.recv(2048).decode()
         print("server : {}".format(serverData))
         if serverData == "exit":
             print("connection as closed by server")
             mysocket.close()
             break
         sendData = input("client : ")
         mysocket.send(sendData.encode())
         if sendData == "exit":
             print("connection as closed by client")
             mysocket.close()
             break
except Exception as e:
 print(e)