import random
import os

print("welcome to the game of bones")
print("Rules: who got more Score than opponent wins. Good luck!")
print("press ENTER to begin a game, if you are ready to this)")
input()

Score = (0,12)
wd = [0,12]
plaScore = wd
opScore = wd


for wd in range(1):
	os.system("cls")

	Score = [
	"1",

	"0",

	"2",

	"3",

	"4",

	"5",

	"6",

	"7",

	"8",

	"9",

	"10",

	"11",

	"12",
]

	windata = {}

	rs = random.choice(Score)
	r = random.randint(0,12)

	windata = [rs,r]

	

	print(f"""
		player #1 got {rs}!
		 player #2 got{r} очков

	""")

	

	input()


for key in windata:
	plaScore = wd[key][0]
	opScore = wd[key][1]

if plaScore<opScore:
	print("you lost")
elif plaScore>opScore:
	print("you won")

input()

	


print(r)
input()
input("Press enter to exit...")