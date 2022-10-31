ports = [80, 443, 21, 23, 3389, 445, 139, 22, 123, 53, 88]

for port in ports:
    if port == 3389:
        pass
        # print(f"found {port}")
    else:
        print(f"currnet {port} Continue search...")

