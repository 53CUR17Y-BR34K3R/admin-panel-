#!/usr/bin/env python
# -*- coding: UTF-8 -*-
R = '\033[31m' # red
G = '\033[32m' # green
from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("malludarkattackers.txt","r");
	link = raw_input("Enter Site Name \n(ex : example.com or www.example.com ): ")
	print "\n\nAvilable links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "Admin Panel Founded => ",req_link
 
def Credit():
        
	Space(9); print  (G +     'Admin Panel Finder'
	Space(9); print"        Script by 1RF4N "
	Space(9); print"      MALLU DARK ATTACKERS"
Credit()
findAdmin()
