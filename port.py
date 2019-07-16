#!/usr/bin/env python
import socket
import subprocess
import sys
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
    		if ifaceName == "wlp2s0":
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
print "Please wait, scanning remote host", IP
print "-" * 60
print baseIP
# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 65535)

# We also put in some error handling for catching errors

try:
    for port in range(1,444):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((IP, port))
        if result == 0:
            print "Port {}: 	 Open".format(port)
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

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total


