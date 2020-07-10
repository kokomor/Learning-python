import os
import random 

def ri(max,min = 0):
	return random.randint(min,max)

def rAndPrint():
	temp = ri(60)
	print(f"выпало {temp}")

def p(text):
	print(str(text))

rAndPrint()

p("billy djin  v kuvshin")

brosok = ri(60)
p(f"Вы бросили и вам выпaло {brosok}")

min = int(input("введите минимальное число:"))
max = int(input("введите максимальное число"))

p(ri(max,min))







guardedList = (1,2,3,4,5,6,7,8,9,10)
p(guardedList[ri(9)])



































input()
