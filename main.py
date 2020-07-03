import serial
import psutil
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
def cpuLoad():
	while True:
		load=int(round(psutil.cpu_percent()))
		load=load*2
		sleep(0.5)
		ser.write(b"r")
		ser.write(str(load).encode('ascii'))
		ser.write(b"g")
		ser.write(str(201-load).encode('ascii'))

if sys.argv[1] == 'on':
	clear()
elif sys.argv[1] == 'off':
	ser.write(b'a0')
elif sys.argv[1] == 'rgb':
	ser.write(b"r")
	ser.write(str(sys.argv[2]).encode('ascii'))
	ser.write(b"g")
	ser.write(str(sys.argv[3]).encode('ascii'))
	ser.write(b"b")
	ser.write(str(sys.argv[4]).encode('ascii'))
elif sys.argv[1] == 'yeelight':
	if sys.argv[2] == 'toggle':
		lamp.toggle()
	else:
		lamp.set_color_temp(int(sys.argv[2]))
elif sys.argv[1] == '--help':
	print(Fore.WHITE, 'on - leds on\noff - leds off\nled_menu - menu')
	print(Fore.WHITE, 'rgb (0 - 255) (0 - 255) (0 - 255) - set leds color to...\nyeelight toggle - toggle main lamp\nyeelight (value) - change color temperature')
elif sys.argv[1] == 'led_menu':
	print(Fore.GREEN, 'Modes:')
	print(Fore.BLUE, ' huewheel')
	print(Fore.CYAN, ' cpu (CPU load)')
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
	elif startFX == 'cpu':
		cpuLoad()
	elif startFX == 'off':
		ser.write(b'a0')
