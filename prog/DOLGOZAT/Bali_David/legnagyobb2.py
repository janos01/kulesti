#Adott három valós szám. Határozzuk meg közölük a legynagyobbat! A három számot kérjük be a felhasználóktól!

intr_1 = "A programot készítette Bali Dávid."
intr_2 = "2020.11.30, Szoft. 1/E"
intr_3 = "A program három szám közül határozza meg a legnagyobbat"

def intr():
	print("=======================================================")
	print("{:^55}".format(intr_1))
	print("{:^55}".format(intr_2))
	print("{:^55}".format(intr_3))
	print("=======================================================\n")
intr()

szam_1 = int(input("Adja meg az első számot: "))
szam_2 = int(input("Adja meg a második számot: "))
szam_3 = int(input("Adja meg a harmadik számot: "))

if szam_1 > szam_2 and szam_1 > szam_3:
	print(f"Az első szám ({szam_1}) a legnagyobb.")

elif szam_2 > szam_1 and szam_2 > szam_3:
	print(f"A második szám ({szam_2}) a legnagyobb.")

elif szam_3 > szam_1 and szam_3 > szam_2:
	print(f"A harmadik szám ({szam_3}) a legnagyobb.")

elif szam_1 == szam_2 > szam_3:
	print(f"Az első és a második szám ({szam_1}) megegyezik, míg a harmadik kisebb.")

elif szam_2 == szam_3 > szam_1:
	print(f"A második és a harmadik szám ({szam_2}) megegyezik, míg az első kisebb.")
	
elif szam_1 == szam_3 > szam_2:
	print(f"Az első és a harmadik szám ({szam_1}) megegyezik, míg a második kisebb.")

elif szam_1 == szam_2 == szam_3:
	print(f"Az összes szám megegyezik ({szam_1})")

else:
	print("Valami hiba történt, próbálkozzon újra.")
