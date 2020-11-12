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
atlag = osszeg / darab

print('Átlag: ', atlag)
print('Legkisebb: ', legkisebb(pontszamok))
print('Legnagyobb: ', legnagyobb(pontszamok))





