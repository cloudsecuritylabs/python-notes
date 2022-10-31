# Task
'''
1. read the arp table
2. look for one mac address associated with multiple IPs
3. ignore headers and broadcast address
# simulate attack using static route
arp -s 157.55.85.220   00-aa-00-62-c6-09
arp -s 157.55.85.219   00-aa-00-62-c6-09
# https://www.online-python.com/9Xyv4jNSDB --> one simple solution
# https://www.online-python.com/WOP906jRT7 --> OOP based solution
'''

import os
# A python class to detect ARP Spoofing
class MacSpoofDetector:
    mac_ip_dict = {}
    def read_arp(self):
        return os.popen("arp -a").read()

    def parse_arp(self, result):
        output = []
        for l in result.splitlines():
            output.append(l.split())
        return output

    def load_data_to_dict(self, splitted_data):
        for item in splitted_data:
            # data clean up, ignore list that does not have right MAC to IP information
            # ignore broadcast address as well
            if len(splitted_data) == 3 and item[1] != 'ff-ff-ff-ff-ff-ff':
                IP = item[0]
                MAC = item[1]
                if MAC in self.mac_ip_dict.keys():
                    if IP not in self.mac_ip_dict[MAC]:
                        self.mac_ip_dict[MAC].append(IP)
                else:
                    self.mac_ip_dict[MAC] = []
                    self.mac_ip_dict[MAC].append(IP)

    def is_spoofing(self):
        for key, value in self.mac_ip_dict.items():
            if len(value) > 1:
                return True
        return False

spoof_doctor = MacSpoofDetector()
arp_table = spoof_doctor.read_arp()
data = spoof_doctor.parse_arp(arp_table)
spoof_doctor.load_data_to_dict(data)
print(f'Is spoofing going on? {spoof_doctor.is_spoofing()}')