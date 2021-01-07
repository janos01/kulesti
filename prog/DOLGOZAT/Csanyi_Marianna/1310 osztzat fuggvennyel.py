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
print('Feladat 1310 megoldása függvénnyel:')          
print('2 dolgozat pontszámainak bekérése, átlagolás, eltérés')

pontszamok = []  
szam = -2  
while szam != -1:  
    szam = int(input("Pontszám(-1 végjelig): "))  
    if szam != -1: 
        pontszamok.append(szam)  

osszeg = 0
for szam in pontszamok:           
    osszeg += szam                 

def legnagyobb(pontszamok):
    smax = pontszamok[0]
    for szam in pontszamok:
        if szam > smax:            
            smax = szam
    return smax                    

def legkisebb(pontszamok):
    smin = pontszamok[0]
    for szam in pontszamok:
        if szam < smin:  
            smin = szam
    return smin

darab = len(pontszamok)  
atlag = osszeg / darab;

print('Átlag: ', atlag)
print('Legrosszabb: ', legkisebb(pontszamok))
print('Legjobb: ', legnagyobb(pontszamok))

elteres1 = atlag - legkisebb(pontszamok)
elteres2 = legnagyobb(pontszamok) - atlag

if elteres2 < elteres1:
	print('Legkisebb elteres: ', elteres1)
elif elteres2 > elteres1:
	print('Legnagyobb elteres: ', elteres2)

#-----------------2 dolgozat

pontszamok1 = []  
szam1 = -2  
while szam1 != -1:   
    szam1 = int(input("Pontszám1(-1 végjelig): "))  
    if szam1 != -1:  
        pontszamok1.append(szam1)  

osszeg1 = 0
for szam1 in pontszamok1:  
    osszeg1 += szam1 

def legnagyobb(pontszamok1):
    smax = pontszamok1[0]
    for szam1 in pontszamok1:
        if szam1 > smax:  
            smax = szam1
    return smax
    
def legkisebb(pontszamok1):
    smin = pontszamok1[0]
    for szam1 in pontszamok1:
        if szam1 < smin:  
            smin = szam1
    return smin


darab1 = len(pontszamok1)  
atlag1 = osszeg1 / darab1;
print('Átlag1: ', atlag1)
print('Legrosszabb1: ', legkisebb(pontszamok1))
print('Legjobb1: ', legnagyobb(pontszamok1))

elteres3 = atlag1 - legkisebb(pontszamok1)
elteres4 = legnagyobb(pontszamok1) - atlag1

if elteres4 < elteres3:
	print('Legkisebb elteres1: ', elteres3)
elif elteres4 > elteres3:
	print('Legnagyobb elteres1: ', elteres4)
