ports = [80, 443, 21, 23, 22] # list

#length
print(len(ports))

print(ports[3])
# append
ports.append(3389)
print(ports)

# updating an index
ports[1] = 445
print(ports)

# deletion
del ports[5]
print(ports)

ports.clear()
print(ports)





# port = () # tuple
#
# set = {"key"}
#
# dictionary = {"key":10}