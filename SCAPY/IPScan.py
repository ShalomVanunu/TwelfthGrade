
from scapy.all import *
from scapy.layers.inet import *

"""
the target of this program is to Scan all the IP Segment 
and show what is UP and answer PING request

similiar to command
NAMP -sP 192.168.1.1/24
"""

ip_segment = '192.168.1.'


for i in range(1,255):
    ip_address = ip_segment+str(i)
    ip_packet = (IP(dst=ip_address) / ICMP())
    # answer is the corect way to know if the DESTINATION is UP
    answer, noanswer = sr(ip_packet, timeout=0.1)
    try:
        if answer[0][1].src == ip_address:

            print(answer[0][1].src)


    except:
        pass