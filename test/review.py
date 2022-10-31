dictionary = {"ports": [80, 443, 22, 21]}
dictionary["ports"].append([3389, 123])
for key, value in dictionary.items():
    print(value)