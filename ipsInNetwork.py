#!/usr/bin/env python
import socket
import subprocess
#import sys
from datetime import datetime
from netifaces import interfaces, ifaddresses, AF_INET

# Clear the screen
subprocess.call('clear', shell=True)

# print ip of all modes
# print subprocess.Popen(["python","ip.py"],stdout=subprocess.PIPE).communicate()[0]


# get private ip
def get_ip():
	for ifaceName in interfaces():
    		addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
    		if ifaceName == "wlp2s0" or ifaceName == "wlan0":
    			return ' '.join(addresses)
    	

# determine the ip
IP  = get_ip()


# DETERMINE BASE IP

# find length of ip
length = len(IP)

# find the location of last dot
if IP[length-2] == ".":
	dot = length - 2
elif IP[length-3] == ".":
	dot = length - 3
else:
	dot = length - 4

# get the base ip	
count = 0
baseIP = ''
	
while count != (dot+1) :
	baseIP += IP[count]
 	count += 1



# Print a nice banner for nmap results
# print "-" * 60
# print "Please wait, scanning using nmap"
# print "-" * 60

# use nmap to display the open ports
# print subprocess.Popen(["nmap","-p-",IP],stdout=subprocess.PIPE).communicate()[0]

# Print a nice banner with information on which host we are about to scan
print "-" * 60
print "Please wait, scanning through remote host", IP
print "-" * 60
# print baseIP
# Check what time the scan started
t1 = datetime.now()

# We also put in some error handling for catching errors
#print socket.AF_INIT
ports = [22,23,53,67,68,69,80,443,4343,8080]
old_ips = ['tadat','tadat','tada']
new_ips = []
temp = []
def findPort(i):
	IP = baseIP + str(i)
	#print IP
	try:
    		for port in ports:
    				#print port  
        			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sock.settimeout(.1)
        			result = sock.connect_ex((IP, port))
        			if result == 0:
        					print IP
        	    				print "Port {}: 	 Open".format(port)
        	    				new_ips.append(IP)
        	    		if port == 8080 and result == 0:
        	    			print " "
        			sock.close()

	except KeyboardInterrupt:
    		print "You pressed Ctrl+C"
    		sys.exit()

	except socket.gaierror:
    		print 'Hostname could not be resolved. Exiting'
    		sys.exit()

	except socket.error:
    		print "Couldn't connect to server"
    		sys.exit()
    	
# checking ports of all ips

for i in range (0,256):
	findPort(i)

	
length = len(new_ips)

i = 0
j = 0
while j < length:
	count = new_ips.count(new_ips[i])
	while count > 1:
		new_ips.pop(i)
		j+=1
		count = new_ips.count(new_ips[i])
	if count == 1:
		i+=1
	j+=1

def Cloning(li1): 
    li_copy = li1[:] 
    return li_copy 

temp = Cloning(old_ips)

for new_ip in new_ips:
	count = old_ips.count(new_ip)
	if count == 0 :
		print "IP {} newly connected".format(new_ip)
		temp.append(new_ip)

for old_ip in old_ips:
	count = new_ips.count(old_ip)
	if count == 0 :
		print "IP {} disconnected".format(new_ip)
		temp.remove(old_ip)


# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total
