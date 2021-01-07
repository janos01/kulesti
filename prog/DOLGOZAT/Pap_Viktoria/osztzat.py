Név= 'Pap Viktória, '
Osztály= 'Szoftverfejlesztő-esti, '
Dátum= '2020.11.27, '
Feladat='1310- dolgozat pontszámait bekéri, átlagtól eltérést néz'
print(Név, Osztály, Dátum)

első = int(input(" Első pontszám: "))
második = int(input(" Második pontszám: "))
átlag=(első+második)/2

print("Átlag: ", átlag)


if (átlag - első) >= (átlag- második):
	print ("Első pontszám tér el leginkább az átlagtól")
elif (átlag - első) <=  (átlag- második):
	print ("Második pontszám tér el leginkább az átlagtól")





