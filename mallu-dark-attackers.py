#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import urllib.request
R = "\033[1;31;40m" # red
G = "\033[1;32;40m" # green
Y = "\033[1;33;40m" # yellow
B = "\033[1;34;40m" # blue
intro = """

           _____    ______ _           _           
     /\   |  __ \  |  ____(_)         | |          
    /  \  | |__) | | |__   _ _ __   __| | ___ _ __ 
   / /\ \ |  ___/  |  __| | | '_ \ / _` |/ _ \ '__|
  / ____ \| |      | |    | | | | | (_| |  __/ |   
 /_/    \_\_|      |_|    |_|_| |_|\__,_|\___|_|   
 
############ By IRF4 ############
"""
print(Y + intro)
        
with open("malludarkattackers.txt",'r') as f:
    link = input("[+] enter site name without http/s: ")
    print(B + "[+] Checking..! \n")
    count = 0
    for links in f:    
        sub_link = f.readline()
        if sub_link is not None:
            req_link = "http://" + link + "/" + sub_link
            try:  
               urllib.request.urlopen(req_link)
               print(G + f"[*] Admin panel is: {req_link}")
            except:
                pass
            print(f"\033[1;36;40m Processing {count} of 670", end="\r")
            count += 1
        else:
            print(R + "[!] Something went wrong with wordlist... ")
    print("[!] Finished Exiting... ")
