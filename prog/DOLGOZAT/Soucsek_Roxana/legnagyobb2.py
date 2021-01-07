#Soucsek Roxána, esti szoft.
print("Soucsek Roxána, esti szoft., 2020")
print("Ez a program 3 valós szám közül meghatározza a legnagyobbat.")



szamok = []

szam1 = int(input('Első szám:'))
	while szam1  != -1:
	if szam1 > -1:
		szamok.append(szam1)

szam2 = int(input("Kérem a második számot:"))
	while szam2  != -1:
	if szam2 > -1:
		szamok.append(szam2)


szam3 = int(input("Kérem a harmadik számot:"))
	while szam3  != -1:
	if szam3 > -1:
		szamok.append(szam3)
		
smax = szamok[0]

for szam in szamok:
	osszeg += szam
	if szam > smax:
		smax = szam
	if szam < smin:
		smin = szam

def legnagyobb(szamok):
	smax = szamok[0]
	for szam in szamok:
		if szam > smax:
			smax = szam
	return smax

print("Legnagyobb szám: ", smax)
