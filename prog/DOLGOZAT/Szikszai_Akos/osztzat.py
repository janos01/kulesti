#Szikszai Ákos, 2020-11-27, Esti Szoft1

print('Szikszai Ákos, 2020-11-27, Esti Szoft1')
print('Feladat 1310')
print('Bekérjük két dolgozat eredményét és kiírjuk az átlaguk, és az átlagtól való eltérését')

szam1 = int(input('Első dolgozat pontszáma: '))
szam2 = int(input('Második Dolgozat pontszáma: '))
osszeg = szam1 + szam2
atlag = osszeg / 2
print ('A dolgozatok átlagpontszáma: ' ,atlag)

eredmeny1 = szam1 - atlag
eredmeny2 = szam2 - atlag

if eredmeny1 > eredmeny2:
	print ('Az első dolgozat tér el jobban az átlagtól! Az átlagtól való eltérés: ', eredmeny1)
if eredmeny2 > eredmeny1:
	 print('A második dolgozat pontszáma tér el jobban az átlagtól! Az átlagtól való eltérés: ', eredmeny2)
