# Enchantment A1
Python script to practice w/RaspberryPi: open a program and simulate key strokes.
the "Auto_VNC" folder should be on the desktop

create a shortcut on the desktop for VNC Viewer

the "IP address" text file shoud ONLY containt the IP
address of the station that is desired to be controlled.

in order for the raspberry pi to auto run the
"Auto_Log_Into_VNC_Address.py" script at startup. go to the
following instructions

1: go to folder location

	/home/pi/.config/lxsession/LXDE-pi

2: open plain text document named
	autostart

3: add the following text before the line that reads "@xscreensaver -no-splash"

	@/home/pi/Desktop/Auto_VNC/Auto_Log_Into_VNC_Address.py

4:save plain text document and reboot the raspberry pi from the
"start menu" drop down. IF YOU REBOOT BY REMOVING POWER THE SAVED
STATE WILL NOT KEEP.

5:after reboot has succedded close any windows that may be open.

6: open the command prompt.

7: go to the scripts directory with command

	cd /home/pi/Desktop/Auto_VNC

8: enter the following command to allow the linux shell
to recognize that the script is an executable file

	chmod +x Auto_Log_Into_VNC_Address.py

9: close the command prompt and open it again

10: type the following command

	pip3 install pynput

11: once pip successfully installs pynput close the command prompt again

12: be sure that the raspberry pi has a static ip address
and reboot the R.Pi from the "start menu"

if the vnc viewer loads properly the work is complete
the pi can be rebooted in any fashion and still boot
up the VNC hmi mimic automatically.
