#Írjon programot, amely bekéri két dolgozat elért pontszámait. 
#A bekért pontszámokat a program átlagolja. Írjuk ki azt is, ki tért el leginkább az átlagtól.

#Készítette Bali Dávid, 2020.11.30, Szoft. 1/E

intr_1 = "A programot készítette Bali Dávid."
intr_2 = "2020.11.30, Szoft. 1/E"
intr_3 = "A program két dolgozat pontszámait hasonlítja össze."
intr_4 = "Majd kiírja azok átlagát, és megállapítja, melyik"
intr_5 = "tért el jobban az átlagtól." 

def intr():
	print("=======================================================")
	print("{:^55}".format(intr_1))
	print("{:^55}".format(intr_2))
	print("{:^55}".format(intr_3))
	print("{:^55}".format(intr_4))
	print("{:^55}".format(intr_5))
	print("=======================================================\n")
intr()

dolgozat_1 = int(input("Adja meg az első dolgozat elért pontszámat: "))
dolgozat_2 = int(input("Adja meg a második dolgozat elért pontszámait: "))


def atlag(dolgozat_1, dolgozat_2):
	atlag = (dolgozat_1 + dolgozat_2) / 2
	return atlag

atlag = atlag(dolgozat_1, dolgozat_2)
int(atlag)

if dolgozat_1 + atlag > dolgozat_2 + atlag:
	kulonbseg_1 = dolgozat_1 - atlag
	int(kulonbseg_1)
	print("\nAz első dolgozat tér el jobban az átlagtól összesen {} elért ponttal.\nAz átlag {} pont, míg a különbség {} pont.".format (dolgozat_1, atlag, kulonbseg_1))

elif dolgozat_1 + atlag < dolgozat_2 + atlag:
	kulonbseg_2 = dolgozat_2 - atlag
	int(kulonbseg_2)
	print("\nA második dolgozat tér el jobban az átlagtól összesen {} elért ponttal.\nAz átlag {} pont, míg a különbség {} pont.".format (dolgozat_2, atlag, kulonbseg_2))

else:
	print("A dolgozatok pontszáma megegyezik")
