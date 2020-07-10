import random
import os

p1 = 0 
p2 = 0

while True:
	os.system("cls")

	p1 = random.randint(1,12)
	p2 = random.randint(1,12)

	print(f"""
		Раунд начался!
		Броски игроков!
		Игрок1: {p1}
		Игрок2: {p2}
		Игрок №{1 if p1>p2 else 2} выбросил больше!

		{"Первый" if p1>p2 else "Второй"} игрок победил
	""")
	
	input()


