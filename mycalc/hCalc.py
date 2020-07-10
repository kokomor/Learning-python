x = int(input("первое число"))
y = int(input("второе число"))
znak = input("выберите знак действия\nЗнак (+,-,*,/): ")

if znak in ['+','-','*','/']:
	print(f"{x}{znak}{y}=",end="")
	if znak == '+':
		print(x + y)
	elif znak == '-':
		print(x - y)
	elif znak == '*':
		print(x * y)
	elif znak == '/':
		print(x / y)
else:
	print ("Вернитесь в ДЕТСАД, это не тот знак!")

input()


