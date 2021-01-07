"""Írjon programot, amely bekéri két dolgozat elért pontszámait. 
A bekért pontszámokat a program átlagolja. 
Írjuk ki azt is, ki tért el leginkább az átlagtól.
# ups 2 dolgozatot külön kell bekérni, merthogy ha csak 2 szám, akkor nincs eltérés, mert csak a fele ?
Mentés: osztzat
"""
#Csányi Marianna
#2020.12.01
#esti szoft I.

print('Csányi Marianna, 2020.12.01, esti szoft I.')
print('Feladat 1310 megoldása:')          
print('2 dolgozat pontszámainak bekérése, átlagolás, eltérés')

pontszamok = []
szam = -2
while szam != -1:
    szam = int(input("Pontszám: "))
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
atlag = osszeg / darab;
print('Átlag: ', atlag)
print('Legkisebb: ', smin)
print('Legnagyobb: ', smax)

elteres1 = atlag - smin
elteres2 = smax - atlag

if elteres2 < elteres1:
	print('Legkisebb eltérés: ', elteres1)
elif elteres2 > elteres1:
	print('Legnagyobb eltérés: ', elteres2)

#----------- 2 dolgozat
pontszamok1 = []
szam1 = -2
while szam1 != -1:
    szam1 = int(input("Pontszám1: "))
    if szam1 != -1:
        pontszamok1.append(szam1)

osszeg1 = 0
smax1 = pontszamok1[0]
smin1 = pontszamok1[0]
for szam1 in pontszamok1:
    osszeg1 += szam1
    if szam1 > smax1:
        smax1 = szam1
    if szam1 < smin1:
        smin1 = szam1

darab1 = len(pontszamok1)
atlag1 = osszeg1 / darab1;
print('Átlag1: ', atlag1)
print('Legkisebb1: ', smin1)
print('Legnagyobb1: ', smax1)

elteres3 = atlag1 - smin1
elteres4 = smax1 - atlag1

if elteres4 < elteres3:
	print('Legkisebb eltérés1: ', elteres3)
elif elteres4 > elteres3:
	print('Legnagyobb eltérés1: ', elteres4)
