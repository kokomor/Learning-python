import random, os

swordNames = [
	"меч орка",
	"elfs sword",
	"6x4",
	"m9"
]
inventory = {}

for i in range(10):
	os.system("cls")

	rs = random.choice(swordNames)
	r = random.randint(0,100)

	inventory[i] = [rs,r]
	

	print(f"""
		вы получили {rs}!
		у этого меча {r} фа

	""")

	input()

#=================================================================
for key in inventory:
	sName = inventory[key][0]
	sStr = inventory[key][1]
	print(f"""
		меч №{key}:
		{sName}
		фа: {sStr}
	""")

print(r)
input("Press enter to exit...")