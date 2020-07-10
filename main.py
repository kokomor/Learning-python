print("Hello world!")

name = input("как тебя зовут? ")
age  = int(input("сколько тебе лет? "))
name2= "Данила"

print("Привет, "+ name + "!")
print(f"Твой возраст - {age}")

if age<10: 
	print("ты ребенок")
elif age>10 and age<18:
	print("ты подросток")
elif age>120:
	print("ты МЁРТВ")
elif age>60 and age<120:
	print("ты пожилой")
else:
	print("ты совершеннолетний")

for i in range(10):
	print(i)

i = 0
while i<10:
	i+=1
	print(i)

while True:
	print("ШАГ")
	
	if input("STOP?")=="да":
		break

input("press ENTER for quit...")
