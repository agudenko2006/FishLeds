#!/bin/bash
port="/dev/ttyUSB0"
stty -F $port 9600

echo -ne $1 > $port 