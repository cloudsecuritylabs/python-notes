import socket
network_socket = socket.socket()
result = network_socket.connect_ex(("ankanbasu.com", 80))
print(result)
# def port_scanner(host, port):
#     network_socket.connect_ex()