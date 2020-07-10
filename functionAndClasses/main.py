import myModule
from myModule import *

class Tank(object):
	def __init__(self,name,w,barrels,power):
		self.name = name
		self.weight = w
		self.barrels = barrels
		self.power = power*barrels
		self.speed = toFixed(70-(w/power),1)

	def shoot(self):
		distance = ri(self.power*4,(self.power*6)+ri(-self.power,self.power))

		print(f"Tank {self.name} shot on {distance*1000} meters")

	def info(self):
		print(f"""
			<=== {self.name} ===>
			Weight: {self.weight} T
			Barrels: x{self.barrels}
			Power: {self.power} p.
			Speed: {self.speed} Km/h
		""")


zhalizyaka = Tank("zhalizyaka",15,2,3)
zhalizyaka.info()
zhalizyaka.shoot()

input()