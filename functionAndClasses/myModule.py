import os
import sys
import random

def ri(min,max):
	return random.randint(min,max)

def pe(text):
	print(text,end="")

def c():
	os.system("cls")

def toFixed(value,chars):
	return (f'%.{chars}f' %value)


