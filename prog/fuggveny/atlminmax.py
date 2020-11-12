# Nagy János, 2020-11-12, esti szoft1

print('Nagy János, 2020-11-12, esti szoft1')
print('A feladat 1307 megoldása')
print('Pontszámok bekérése tömbbe, átlagolás')
print('----------------------------------')


pontszamok = []
szam = -2
while szam != -1:
    szam = int(input('Szám: '))
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





