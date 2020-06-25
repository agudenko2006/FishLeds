import serial
from random import random
import sys
from yeelight import Bulb
lamp = Bulb("192.168.0.102")
from time import sleep
from colorama import Fore, Back

# time = 0
time = 0.02

ser = serial.Serial('/dev/ttyUSB0', 9600)
sleep(0.3)

def huewheel():
	i = 0
	for i in range(255):
		ser.write(b"g")
		ser.write(str(i).encode('ascii'))
		sleep(time)
	for i in range(255):
		ser.write(b"b")
		ser.write(str(i).encode('ascii'))
		sleep(time)
	for i in range(255):
		ser.write(b"g")
		ser.write(str(255-i-1).encode('ascii'))
		sleep(time)
	while True:
		for i in range(255):
			ser.write(b"g")
			ser.write(str(i).encode('ascii'))
			sleep(time)
		for i in range(255):
			ser.write(b"b")
			ser.write(str(255-i-1).encode('ascii'))
			sleep(time)
		for i in range(255):
			ser.write(b"r")
			ser.write(str(i).encode('ascii'))
			sleep(time)
		for i in range(255):
			ser.write(b"g")
			ser.write(str(255-i-1).encode('ascii'))
			sleep(time)
		for i in range(255):
			ser.write(b"b")
			ser.write(str(i).encode('ascii'))
			sleep(time)
		for i in range(255):
			ser.write(b"r")
			ser.write(str(255-i-1).encode('ascii'))
			sleep(time)
def clear():
	ser.write(b'a255')
def fire(k):
	ser.write(b"r255")
	while True:
		ser.write(b"g")
		ser.write(str(int(random()*30+1)).encode('ascii'))
		firetime=random()/k
		sleep(firetime)
def newYear():
	ntime=0.2
	while True:
		ser.write(b"r255")
		sleep(ntime)
		ser.write(b"r0g255")
		sleep(ntime)
		ser.write(b"g0b255")
		sleep(ntime)
		ser.write(b"r255")
		sleep(ntime)
		ser.write(b"r0g255")
		sleep(ntime)
		ser.write(b"b0r255")
		sleep(ntime)
		ser.write(b"b255")
		sleep(ntime)
def linuxColor():
	ser.write(b"a0")
	for i in range(255):
		ser.write(b"g")
		ser.write(str(i).encode('ascii'))
	for i in range(255):
		ser.write(b"r")
		ser.write(str(i).encode('ascii'))

if sys.argv[1] == 'on':
	clear()
elif sys.argv[1] == 'off':
	ser.write(b'a0')
elif sys.argv[1] == 'yeelight':
	lamp.toggle()
elif sys.argv[1] == '--help':
	print(Fore.WHITE, 'on - leds on\noff - leds off\nyeelight - toggle main lamp\nled_menu - menu')
elif sys.argv[1] == 'led_menu':
	print(Fore.GREEN, 'Modes:')
	print(Fore.BLUE, ' huewheel')
	print(Fore.YELLOW, ' fire')
	print(Fore.YELLOW, ' linux (yellow)')
	print(Fore.RED, ' new year')
	print(Fore.WHITE, ' clear')
	print(Fore.BLACK, Back.RED, 'off')
	print(Fore.RESET, Back.RESET,'select one: ')
	startFX=input()
	if startFX == 'huewheel':
		huewheel()
	elif startFX == 'clear':
		clear()
	elif startFX == 'fire':
		fire(2)
	elif startFX == 'new year':
		newYear()
	elif startFX == 'linux':
		linuxColor()
	elif startFX == 'off':
		ser.write(b'a0')