#Soucsek Roxána, esti szoft.
print("Soucsek Roxána, esti szoft., 2020")
print("Ez a program két dolgozat pontjait átlagolja.")

pontszamok = []
szam = 0
while szam != -1:
	szam=int(input('Pontszám:'))
	if szam != -1:
		pontszamok.append(szam)



osszeg = 0
smax = pontszamok[0]
smin = pontszamok[0]
for szam in pontszamok:
	osszeg += szam
	if szam > smax:
		smax = szam
	if szam < smin:
		smin = szam
		
darab = len(pontszamok) 
atlag = osszeg / darab

print("A pontszámok átlaga:", atlag)
