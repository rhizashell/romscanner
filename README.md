RomScanner 0.1 Alpha
====================

Description
===========

RomScanner scans your router to see if it's vulnerable to configuration disclosure.
<br>If successful, hackers could compromise your router.

Vulnerable Routers
===================

- Billion 5200
- ZyXEL P-660HW T1 V2
- Huawei EchoLife HG520s
- TP Link W8901G

How to use RomScanner
=====================

Simply download romscanner.py
<br>locate the file with your terminal
<br>type: python romscanner.py
<br>You will be prompted to enter an IP address of the target.
<br>If the exploit is successfull it will download the rom-0 file.
<br>You can upload the rom-0 file and extract the admin password at http://198.61.167.113/zynos/

Credits
=======

 - Written by Rhiza, 
 - requires Python 2.7
 - Doesn't require any third party modules
