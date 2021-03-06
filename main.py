ledPort='/dev/ttyUSB0'
lampIP='192.168.0.102'
useConsole=True
maxBrightness=255
def defaultMode():
	huewheel()
#------------------------------------------#

import serial
import psutil
from random import random
import sys
import os
from yeelight import Bulb
lamp = Bulb(lampIP)
from time import sleep
from colorama import Fore, Back

# time = 0
time = 0.02

ser = serial.Serial(ledPort, 9600)
sleep(0.3)

def huewheel():
	i = 0
	for i in range(maxBrightness):
		ser.write(b"g")
		ser.write(str(i).encode('ascii'))
		sleep(time)
	for i in range(maxBrightness):
		ser.write(b"b")
		ser.write(str(i).encode('ascii'))
		sleep(time)
	for i in range(maxBrightness):
		ser.write(b"g")
		ser.write(str(maxBrightness-i-1).encode('ascii'))
		sleep(time)
	while True:
		for i in range(maxBrightness):
			ser.write(b"g")
			ser.write(str(i).encode('ascii'))
			sleep(time)
		for i in range(maxBrightness):
			ser.write(b"b")
			ser.write(str(maxBrightness-i-1).encode('ascii'))
			sleep(time)
		for i in range(maxBrightness):
			ser.write(b"r")
			ser.write(str(i).encode('ascii'))
			sleep(time)
		for i in range(maxBrightness):
			ser.write(b"g")
			ser.write(str(maxBrightness-i-1).encode('ascii'))
			sleep(time)
		for i in range(maxBrightness):
			ser.write(b"b")
			ser.write(str(i).encode('ascii'))
			sleep(time)
		for i in range(maxBrightness):
			ser.write(b"r")
			ser.write(str(maxBrightness-i-1).encode('ascii'))
			sleep(time)

def clear():
	ser.write(b'a')
	ser.write(str(maxBrightness).encode('ascii'))

def fire(k):
	ser.write(b"r")
	ser.write(str(maxBrightness).encode('ascii'))
	while True:
		ser.write(b"g")
		ser.write(str(int(random()*30+1)).encode('ascii'))
		firetime=random()/k
		sleep(firetime)

def newYear():
	ntime=0.2
	while True:
		ser.write(b"r")
		ser.write(str(maxBrightness).encode('ascii'))
		sleep(ntime)
		ser.write(b"r0g")
		ser.write(str(maxBrightness).encode('ascii'))
		sleep(ntime)
		ser.write(b"g0b")
		ser.write(str(maxBrightness).encode('ascii'))
		sleep(ntime)
		ser.write(b"r")
		ser.write(str(maxBrightness).encode('ascii'))
		sleep(ntime)
		ser.write(b"r0g")
		ser.write(str(maxBrightness).encode('ascii'))
		sleep(ntime)
		ser.write(b"b0r")
		ser.write(str(maxBrightness).encode('ascii'))
		sleep(ntime)
		ser.write(b"b")
		ser.write(str(maxBrightness).encode('ascii'))
		sleep(ntime)

def linuxColor():
	ser.write(b"a0")
	for i in range(maxBrightness):
		ser.write(b"g")
		ser.write(str(i).encode('ascii'))
	for i in range(maxBrightness):
		ser.write(b"r")
		ser.write(str(i).encode('ascii'))

def LRlampToggle(Lamp, state):
	print("This is not for you(")

def cpuLoad():
	while True:
		load=int(round(psutil.cpu_percent()))
		load=load*2
		sleep(0.5)
		ser.write(b"r")
		ser.write(str(load).encode('ascii'))
		ser.write(b"g")
		ser.write(str(201-load).encode('ascii'))

def menuAndConsoleArguments():
	if useConsole == True:
		if sys.argv[1] == 'on':
			defaultMode()
		elif sys.argv[1] == 'off':
			ser.write(b'a0')
		elif sys.argv[1] == 'rgb':
			ser.write(b"r")
			ser.write(str(sys.argv[2]).encode('ascii'))
			ser.write(b"g")
			ser.write(str(sys.argv[3]).encode('ascii'))
			ser.write(b"b")
			ser.write(str(sys.argv[4]).encode('ascii'))
		elif sys.argv[1] == 'r':
			ser.write(b"r")
			ser.write(str(sys.argv[2]).encode('ascii'))
		elif sys.argv[1] == 'g':
			ser.write(b"g")
			ser.write(str(sys.argv[2]).encode('ascii'))
		elif sys.argv[1] == 'b':
			ser.write(b"b")
			ser.write(str(sys.argv[2]).encode('ascii'))
		elif sys.argv[1] == 'onL':
			LRlampToggle('L', 'on')
		elif sys.argv[1] == 'offL':
			LRlampToggle('L', 'off')
		elif sys.argv[1] == 'onR':
			LRlampToggle('R', 'on')
		elif sys.argv[1] == 'offR':
			LRlampToggle('R', 'off')
		elif sys.argv[1] == 'onAll':
			LRlampToggle('R', 'on')
			LRlampToggle('L', 'on')
			lamp.turn_on()
		elif sys.argv[1] == 'offAll':
			LRlampToggle('R', 'off')
			LRlampToggle('L', 'off')
			lamp.turn_off()
		elif sys.argv[1] == 'yeelight':
			if sys.argv[2] == 'toggle':
				lamp.toggle()
			else:
				lamp.set_color_temp(int(sys.argv[2]))
		elif sys.argv[1] == '--help':
			print(Fore.WHITE, 'on - leds on\noff - leds off\nled_menu - menu')
			print(Fore.WHITE, 'rgb (0 - 255) (0 - 255) (0 - 255) - set leds color to...\nyeelight toggle - toggle main lamp\nyeelight (value) - change color temperature')
		elif sys.argv[1] == 'led_menu':
			menu()
	else:
		menu()
		menuAndConsoleArguments()
def menu():
	ser.write(b"a0")
	os.system("clear")
	print(Fore.GREEN, 'Modes:')
	print(Fore.BLUE, ' huewheel')
	print(Fore.CYAN, ' cpu (CPU load)')
	print(Fore.YELLOW, ' fire')
	print(Fore.YELLOW, ' linux (yellow)')
	print(Fore.YELLOW, ' yeelight toggle')
	print(Fore.YELLOW, ' yeelight color')
	print(Fore.RED, ' new year')
	print(Fore.WHITE, ' clear')
	print(Fore.RED, ' r',Fore.GREEN,'g',Fore.BLUE,'b')
	print(Fore.BLACK, Back.RED, 'off')
	print(Fore.RESET, Back.RESET,'select one: ')
	startFX=input()
	if startFX == 'huewheel':
		try:
			huewheel()
		except KeyboardInterrupt:
			pass
		menuAndConsoleArguments()
	elif startFX == 'clear':
		clear()
	elif startFX == 'fire':
		try:
			fire(2)
		except KeyboardInterrupt:
			pass
		menuAndConsoleArguments()
	elif startFX == 'new year':
		try:
			newYear()
		except KeyboardInterrupt:
			pass
		menuAndConsoleArguments()
	elif startFX == 'linux':
		linuxColor()
	elif startFX == 'yeelight toggle':
		lamp.toggle()
	elif startFX == 'yeelight color':
		lamp.set_color_temp(int(input()))
	elif startFX == 'cpu':
		try:
			cpuLoad()
		except KeyboardInterrupt:
			pass
		menuAndConsoleArguments()
	elif startFX == 'off':
		ser.write(b'a0')
	elif startFX == 'rgb':
		print('red: ')
		color=input()
		ser.write(b"r")
		ser.write(str(color).encode('ascii'))
		print('green: ')
		color=input()
		ser.write(b"g")
		ser.write(str(color).encode('ascii'))
		print('blue: ')
		color=input()
		ser.write(b"b")
		ser.write(str(color).encode('ascii'))
		try:
			while True:
				sleep(1)
		except KeyboardInterrupt:
			pass
menuAndConsoleArguments()
