import os
import datetime
os.system("arp -a")

# ping test lab -> what technique we used
# store result

# with open("ping_result.txt", "r") as pingfile:
#     for line in pingfile:
#         if "ms" in line:
#             print("Internet is available")
#             break
#         elif "unavailable" in line:
#             print("Internet is not available")
#         else:
#             continue


## parse result to create a dictionary data structure (ip:mac //mac:ip)

## you ask the dict for duplicate