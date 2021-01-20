
from scapy.all import *
from scapy.layers.inet import *

ICMP_CODE_ECHO_REQUEST ='8' #https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml#icmp-parameters-types

def print_packets(pkt):
    packet =(pkt[IP][ICMP].type)
    if ICMP_CODE_ECHO_REQUEST in str(packet): # 8 means Echo-Request
        print(pkt[IP].src)

def print_src_MAC(pkt):
    print(pkt[Ether].src)

sniff(filter='icmp', prn=print_packets)

#sniff(filter='ether', prn=print_src_MAC)