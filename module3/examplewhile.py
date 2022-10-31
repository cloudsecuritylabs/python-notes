# want to ask the user for a port
ports = []
while True:
    port = int(input("Please enter a port number:  or enter 999 to exit"))
    if port == 999:
        break
    else:
        ports.append(port)
        print(ports)