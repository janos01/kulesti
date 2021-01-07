#Szikszai Ákos, 2020-11-27, Esti Szoft1

print('Szikszai Ákos, 2020-11-27, Esti Szoft1')
print('Feladat 0412')
print('Bekérünk három valós számot, és a program kiírja a legnagyobbat')

bekertszamok = []


szam1 = int(input('Első szám: '))
bekertszamok.append(szam1)
szam2 = int(input('Második szám: '))
bekertszamok.append(szam2)
szam3 = int(input('Harmadik szám: '))
bekertszamok.append(szam3)


maximum = max(bekertszamok)
print('A legnagyobb szám: ' ,maximum)

