#!/usr/bin/python
# Coded By GeoMetriX
# Thanks To clown hacktivism & api access
import os
import urllib2
import json

print ("System Running in" os.system(uname -a))
print("            #####################################################")
print("            #                                                   #")
print("            #               GEOMETRIX IP TRACKER                #")
print("            #                 cl0wn hacktivism                  #")
print("            #          http://clownhacktivismteam.org           #")
print("            #                                                   #")
print("            #####################################################")
print("")

while True:
		ip=raw_input("Your Target ip:")
		url = "http://ip-api.com/json/"
		response = urllib2.urlopen(url + ip)
		data = response.read()
		values = json.loads(data)

		
		print("")
		print("")
		print("")
		print("+============[Tracked]============+")
		print(" IP: " + values['query'])
		print(" City: " + values['city'])
		print(" As: " + values['as'])
		print(" Country: " + values['country'])
		print(" Status: " + values['status'])
		print(" Region: " + values['region'])
		print(" Time Zone: " + values['timezone'])
		print("+============[Tracked]============+")
		print("")
		print(" Thanks for ip-api.com for api access!")

		
		break

##############################################################################
