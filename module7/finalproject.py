import os
from collections import Counter
outputfile = "arptable.txt"

def get_arp_table():
    os.system("arp -a >" + outputfile)

def get_ip_mac_dictionary():
    arpdict = dict()
    get_arp_table()
    with open("arptable.txt", "r") as arptable:
        for line in arptable:
            #do not print lines with the same
            if "ff-ff-ff-ff-ff-ff" not in line:
                splitted = (line.split())
                if len(splitted) == 3:
                    ip_address = splitted[0]
                    mac_address = splitted[1]
                    arpdict[ip_address] = mac_address
    return arpdict

def spoofing_check():
    result = get_ip_mac_dictionary()
    mac_list =[]
    for ip, mac in result.items():
        mac_list.append(mac)

    mac_set = set(mac_list)

    if len(mac_set) != len(mac_list):
        print("spoofing detected")

    counts = Counter(result.values())
    # print(counts)

    spoofed_mac = ""
    for k,v in counts.items():
        if v > 1:
            spoofed_mac = k
            print(f'spoofed mac address is {k}')

    # give me the IPs associated with spoofing
    for ip,mac in result.items():
        if mac == spoofed_mac:
            print(f'ip under attack {ip}')

def main():
    get_arp_table()
    get_ip_mac_dictionary()
    spoofing_check()