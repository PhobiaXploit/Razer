#!/usr/bin/python

import os,sys,requests

os.system("clear")

print("""\033[33m
\t  ______ _______ ______ _______  ______
\t |_____/ |_____|  ____/ |______ |_____/
\t |    \_ |     | /_____ |______ |    \_
""")
if len(sys.argv) != 2:
    print("Usage : " +sys.argv[0]+" example.com")
    exit()

lst = open('admin-list.txt', 'r')

while True:
    suc = open('found-admin.txt', 'a')
    host = sys.argv[1] 
    lstt = lst.readline().replace('\n', '')
    if not host:
        break
    if not host.startswith('http'):
        host = 'http://' + host
        try:
            r = requests.get(host+'/'+lstt)
        except:
            print("[!] Check Your Connection . . .")
            pass
            continue
        if r.status_code == 404:
            print(host+'/'+lstt+'~> [NOT]')
        else:
            print(host+'/'+lstt+'~> [FOUND]') 
            suc.write(host+'/'+lstt+'\n')   
