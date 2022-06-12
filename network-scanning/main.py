from scapy.all import *

# read capture
packet = rdpcap("http.cap")
p = packet[3]
p.show()

# building new packet
p = IP(dst="8.8.8.8") / TCP(dport=53)
# dport = detination port
p[TCP].dport = 35
p.show()
