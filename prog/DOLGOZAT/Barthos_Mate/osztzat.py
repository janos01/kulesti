#Barthos Máté, 2020.12.07 esti szoftverfejlesztés
print ("Barthos Máté, 2020.12.07, esti")

#két dolgozat pontszámainak bekérése
doga1=int(input('elso dolgozat pontszáma: '))
doga2=int(input('masodik dolgozat pontszáma: '))

#dolgozat átlagai
atlag=(doga1+doga2)/2

#dolgozatok átlagtól való eltérésének kiiaratása
#felesleges múvelet, mert két dolgozat esetén ugyanakkora lesz az eltérés
if abs(doga1-atlag)>abs(doga2-atlag):
	print("az első dolgozat tér el jobban az átlagtól")
elif abs(doga1-atlag)<abs(doga2-atlag):
	print("a második dolgozat tér el jobban az átlagtól")
else:
	print("ugyanakkora az eltérés.")


