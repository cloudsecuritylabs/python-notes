# read the file

http_response_304 = []
with open("access.log.20170101.txt", "r") as logfile:
    for line in logfile:
        splitted = line.split()
        http_response = splitted[-2]
        if http_response == "304":
            http_response_304.append(http_response)

print(len(http_response_304))
