# Beadandó: 0412-es feladat
# Készítette: Mertz Gábor
# 2020. december 3.
# Külker Szoftver esti 1.
# feladat: Adott három valós szám. Határozzuk meg közölük a legynagyobbat!
# A három számot kérjük be a felhasználóktól! 

print ('Készítette: Mertz Gábor')
print ('Badandó, 0412-es feladat')
print ('Kérek 3 valós számot, kiírom a legnagyobbat.')

a = float(input ('Első szám: '))
b = float(input ('Második szám: '))
c = float(input ('Harmadik szám: '))

if a>b and a>c :
	print ('A legnagyobb  szám', a)
	
if b>a and b>c :
	print ('A legnagyobb  szám', b)
	
if c>a and c>b :
	print ('A legnagyobb  szám', c)
