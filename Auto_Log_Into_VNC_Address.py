#!/usr/bin/env python3
#do not remove the line above this one as it designates the environment in which to run this script.
#
#be sure to have pip installed on station that will be running this script
#be sure to have pynput installed on station that will be running this script
#
#this script is created to run at the starting sequence of a raspberry pi B+ with
#a raspbian linux distro, which already would be setup to "auto login" to the desktop.
#
#file location depends on the user, but for this application it was found most convenient 
#to create a folder on the desktop filled with a shortcut to the desired program, a text
#document with the desired IP address typed out, and finally this .py file.
#
#
#
import pynput.mouse as MS
import pynput.keyboard as KB
import subprocess, sys
import time

mouse = MS.Controller()
keyboard = KB.Controller()

#time.sleep is a delay timer before continuing through the program
time.sleep(5)

#opens VNC viewer from the desktop shortcut
opener = "open" if sys.platform == "darwin" else "xdg-open"
subprocess.call([opener, '/home/pi/Desktop/realvnc-vncviewer.desktop'])

#time.sleep is a delay timer before continuing through the program
#wait a specified amount of time for the viewer to open
time.sleep(5)

#open IP address txt document on the desktop
text_file = open("/home/pi/Desktop/Auto_VNC/IP address", "r")

#txt document should ******ONLY CONTAIN THE IP ADDRESS OF THE STATION******
#which this station(in this case HMI) is intended to connect with
HMI_address = text_file.read()

#close IP address txt document
text_file.close()

#this for loop simulates the key strokes of whatever is writen in the IP address text document.
for i in HMI_address:
    keyboard.press(i)
    keyboard.release(i)


print(HMI_address)

time.sleep(1)

keyboard.press(KB.Key.enter)
keyboard.release(KB.Key.enter)


#the following is a simple "mouse jiggle" to allow the VNC to reconnect to a lost connection
while 1==1:
    time.sleep(30)
    mouse.move(1, 0)
    mouse.move(0, 1)
    mouse.move(-1, 0)
    mouse.move(0, -1)
