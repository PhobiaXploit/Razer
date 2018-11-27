#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import os
import sys
os.system("clear")

print("""\033[91m
\t  ______ _______ ______ _______  ______
\t |_____/ |_____|  ____/ |______ |_____/
\t |    \_ |     | /_____ |______ |    \_
\033[0m""")
if len(sys.argv) != 3:
    print("\t [!] Usage : " +sys.argv[0]+" -l list.txt")
    exit()
    
lst = sys.argv[2]
if len(str(lst)) > 0:
    if os.path.isfile(lst):
        ls = open(lst, 'r')
    else:
        exit(" [!] List Tidak Ditemukan")
while True:
    suc = open('Result.txt', 'a')
    host = ls.readline().replace('\n', '')
    if not host:
        break
    if not host.startswith('http'):
        host = 'http://' + host
        print(' \033[097m[*] Checking ~> '+ host)
        try:
            r = requests.get(host)     
        except:
            print(' \033[91m[!] Server Null Response\n')
            pass
            continue
        if r.status_code == 404:
            print(' \033[32;1m[*] Vulnerabiltiy Take Over \n\033[0m')
            suc.write(host+'\n')
        else:
            print(' \033[91m[!] Not Vulnerability Take Over \n')                     
