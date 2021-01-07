# Beadandó dolgozat
# Készítette: Mertz Gábor
# szoftver programozó 1. évf. A.
# Dátum: 2020. december 10.
# 1310-es szit.hu feladat
# feladat értelmezés: dolgozatonként számol átlagot a tanulókra
# a tanulók dolgozat átlagaihoz nézi az eltérést
# azonos mértékű eltérés esetén az elsőt írja ki legnagyobbnak

print('készítette:Mertz Gábor 2020. december 10.')
print('Dolgozat átlagoló program')
print('Számtani átlagot számol, pozitív egész számok és nulla az input pont')
print ('------------------')


print('Kérem a pontszámokat dolgozatonként! -1 végjelig')
pont1=0
pont2=0
atlag=0
atlagok=[]
pontszamok1=[]
pontszamok2=[]
atlagokAtlaga=0

pont1=int(input('Első dolgozat:'))
pont2=int(input('Masodik dolgozat:'))
while pont1 != -1 :
		atlag=(pont1 + pont2) / 2
		atlagok.append(atlag)
		pont1=int(input('Első dolgozat:'))
		pont2=int(input('Masodik dolgozat:'))
		
# print(atlagok)

sorszam=0
atlag=0
osszeg=0
for atlag in atlagok:
	sorszam=sorszam+1
	osszeg=osszeg+atlag
	
atlagokAtlaga=osszeg/sorszam

# print(atlagokAtlaga)

elteres=0
sorszam=0
maxElteres=0
elteresSorszam=1
# azonos értékek esetére 1 a kezdőérték

for atlag in atlagok:
	sorszam=sorszam+1
	elteres=abs(atlagokAtlaga-atlag)
	if elteres > maxElteres:
		maxElteres=elteres
		elteresSorszam=sorszam
		
print ('A legnagyobb elteres:', maxElteres)
print ('A legnagyobb eltérés ennél a dolgozatnál:',elteresSorszam)

print ('-------- program vége ----------')



