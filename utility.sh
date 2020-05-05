#!/bin/bash

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
		bash /home/gudenalek/sketchbook/leds.sh r0g33b85
		lookandfeeltool -a org.kde.breezedark.desktop
	elif [ $i -eq 2 ]
	then
		bash /home/gudenalek/sketchbook/leds.sh r0g255b100
		lookandfeeltool -a org.kde.breeze.desktop
	elif [ $i -eq 3 ]
	then
		bash /home/gudenalek/sketchbook/leds.sh r255g0b255
		lookandfeeltool -a Sweet
	elif [ $i -eq 4 ]
	then
		bash /home/gudenalek/sketchbook/leds.sh r255g0b0
		lookandfeeltool -a Soft_Glass
		latte-dock --replace&
	elif [ $i -eq 5 ]
	then
		bash /home/gudenalek/sketchbook/leds.sh r0g100b255
		lookandfeeltool -a com.github.vinceliuice.McMojave
	else
		bash /home/gudenalek/sketchbook/leds.sh $i
		clear
		echo "Enter color brightness"
		read i
		bash /home/gudenalek/sketchbook/leds.sh $i
		clear
	fi
done
