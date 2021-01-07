#Szitás-Kiss Vanda 2020.12.01. Programozási alapok. Szoftverfejlesztő-és tesztelő esti 13 osztály. 1310-es feladat
print("Szitás-Kiss Vanda, 2020.12.01. Programozási alapok.")

dolgozat1 = int(input("Első dolgozat érdemjegye:"))
dolgozat2 = int(input("Második dolgozat érdemjegye:"))

atlag = (dolgozat1 + dolgozat2) / 2
if atlag < dolgozat1:
	elter1 = dolgozat1 - atlag
else:
	elter1 = atlag - dolgozat1
	
if atlag < dolgozat2:
	elter2 = dolgozat2 - atlag
else:
	elter2 = atlag - dolgozat2

if elter1 > elter2:
	print("Az első dolgozat és az átlag között nagyobb az eltérés.")
elif elter1 < elter2:
	print("A második dolgozat és az átlag között nagyobb az eltérés.")
else:
	print("Az átlag és a dogozat pontszáma közti különbség mindkét dolgozatnál ugyanannyi.")


print("A két dolgozat átlaga:", atlag)


