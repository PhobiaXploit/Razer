#!/usr/bin/python

import os,sys,requests

os.system("clear") 
# Color
blgelap='\033[94m'
blterang='\033[96m'
ungu='\033[95m'
merah='\033[91m'
ijmuda='\033[32m'
kuning='\033[33m' 

print("""
\t\033[33m  ______ _______ ______ _______  ______
\t |_____/ |_____|  ____/ |______ |_____/
\t |    \_ |     | /_____ |______ |    \_
""")
if len(sys.argv) != 2:
    print("Usage : "+sys.argv[0]+" example.com")
    exit()

lst = open('list-shell.txt', 'r')

while True:
    suc = open('result-shell.txt', 'a')
    host = sys.argv[1]
    lstt = lst.readline().replace('\n', '')
    if not host:
        break
    if not host.startswith('http'):
        host = 'http://' + host
        try:
            r = requests.get(host+'/'+lstt)
        except:
            print("[!] Gagal Konek Ke Server . . .")
            pass
            continue
        if r.status_code == 200:
            print(host+'/'+lstt+'~> [FOUND]')
            suc.write(host+'/'+lstt+'\n')
        else:
            print(host+'/'+lstt+'~> [NOT]') 
