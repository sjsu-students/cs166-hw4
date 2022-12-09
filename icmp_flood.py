# import sys to get command line arguments
import sys

# import scapy to get access to IP, UDP, etc.
from scapy.all import *

# define a function to create a random IP address
def randomIP():
    # generate random numbers between 0 and 255 and join them to create the ip
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    # return the ip
    return ip


# define a function to generate a random port number
def randPort():
    # get a random number between 0 and 64000 to use as port number
    x = random.randint(0, 64000)
    # return the port number
    return x


# extract the destination ip address from command line args
dest_ip_address = sys.argv[1]
# extract the destination port number from command line args
dest_port = int(sys.argv[2])
# extract the given packet count from command line args
pkt_count = int(sys.argv[3])

# loop as many times as there were packets requested
for i in range(0, pkt_count):
    # generate a random source ip address
    src_ip = randomIP()
    # generate a random source port address
    src_port = randPort()

    # construct the packet using the scapy provided IP object
    packet = IP(src=str(src_ip), dst=dest_ip_address)
    # construct the packet by using the overriden div operator with a scapy provided ICMP object
    pkt = packet / ICMP()
    # send the UDP packet
    send(pkt)
