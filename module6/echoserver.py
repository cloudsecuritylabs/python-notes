import socket
try:
     mysocket = socket.socket()
     mysocket.bind(('0.0.0.0', 1234))
     mysocket.listen(1)
     print("waiting for connection...")
     c, addr = mysocket.accept()
     print("client that connected details are -> {}".format(addr))
     while True:
         sendData = input("server : ")
         c.send(sendData.encode())
         if sendData == "exit":
             c.close()
             break
         rcvData = c.recv(1024).decode()
         print("client : {}".format(rcvData))
         if rcvData == "exit":
             print("connection as closed by client".encode())
             c.close()
             break
except Exception as e:
     print(e)