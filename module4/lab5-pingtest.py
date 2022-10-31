# ping using OS module
# identify if we have connectivity
import os
os.system("ping 8.8.8.8 > ping_result.txt")
# parse a file
with open("ping_result.txt", "r") as pingfile:
    for line in pingfile:
        if "ms" in line:
            print("Internet is available")
            break
        elif "unavailable" in line:
            print("Internet is not available")
        else:
            continue
