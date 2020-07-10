import random, os

print("welcome")
print("press ENTER to begin a game")
input()

for wd in range(1):
	os.system("cls")

Score = ["1","2","3","4","5","6","7","8","9","10","11","12"]

windata[wd] = ["1","2","3","4","5","6","7","8","9","10","11","12"]

Score = ["1",

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

"12"
]


windata = {}

rs = random.choice(Score)
r = random.randint(0,12)

windata = [rs,r]

	

print(f"""
вы получили {rs}!
ваш оппонент получил {r} очков

	""")

	

input()


for key in windata:
	plaScore = windata[key][0]
	opScore = windata[key][1]

if plaScore<opScore:
	print("you lost")
elif plaScore>opScore:
	print("you won")

input()

	


print(r)
input()
input("Press enter to exit...")