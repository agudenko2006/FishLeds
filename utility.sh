#!/bin/bash
port="/dev/ttyUSB0"
stty -F $port 9600

clear
echo "FizhLeds"
# sleep 1s
clear
# echo "Hit CTRL+C to exit"
# sleep 1s
while true
do
	clear
	echo "r - red"
	echo "g - green"
	echo "b - blue"
	echo "c - hue wheel"
	echo "a - all"
	echo "1 - dark mode"
	echo "2 - light mode"
	echo "3 - sweet theme"
	echo "4 - SoftGlass theme"
	echo "5 - MacOS theme"
	echo "0 - exit"
	read i
	if [ $i -eq 0 ]
	then
		exit 0
	elif [ $i -eq 1 ]
	then
		echo -ne r0g33b85 > $port 
		lookandfeeltool -a org.kde.breezedark.desktop
	elif [ $i -eq 2 ]
	then
		echo -ne r0g255b100 > $port 
		lookandfeeltool -a org.kde.breeze.desktop
	else
		echo -ne $i > $port 
		clear
		echo "Enter color brightness"
		read i
		echo -ne $i > $port 
		clear
	fi
done
