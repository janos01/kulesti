#Frantal Attila, 2020.11.27. , Szoft I/1/E
print('Frantal Attila, 2020.11.27. ,  Szoft I/1/E\n')

feladat="""Feladat 1310:
Írjon programot, amely bekéri két dolgozat elért pontszámait. 
A bekért pontszámokat a program átlagolja. 
Írjuk ki azt is, ki tért el leginkább az átlagtól.
---------------------------------------------------------------------"""
#A két dolgozatot nem biztos, hogy ugyanannyian írták meg, ezért külön ciklusban kérem be a pontszámaikat.
#A két dolgozat átlagának nincs köze egymáshoz, hiszen a maximálisan elérhető pontszámuk sem biztos, hogy egyezik. Ezért külön átlagolom a két dolgozat pontjait.

print(feladat)

dolgozat1 = []	#ebben tárolom az első dolgozat pontjait
dolgozat2 = []	#ebben tárolom a második dolgozat pontjait
osszeg1 = 0	#ebben tárolom az első dolgozat pontjainak összegét (átlaghoz kell majd)
osszeg2 = 0	#ebben tárolom a második dolgozat pontjainak összegét (átlaghoz kell majd)

#Az első dolgozat pontszámainak bekérése. Negatív pontszám a végjel.
print('\nAdd meg az első dolgozat pontszámait, negatív számra vége a bekéréseknek.\n')
i = True #ciklus feltétel változója
sorsz1 = 1 #ennyiszer fut a ciklus (futásonként növelem 1-gyel)
while i:
	pont1 = int(input('Az első dolgozat ' + str(sorsz1)+ '. pontszáma: '))
	if pont1 >= 0:
		dolgozat1.append(pont1)
		osszeg1 += pont1
		sorsz1 += 1
	else:
		i = False

#A második dolgozat pontszámainak bekérése. Negatív pontszám a végjel.
print('\nAdd meg a második dolgozat pontszámait, negatív számra vége a bekéréseknek.\n')
n = True #ciklus feltétel változója
sorsz2 = 1 #ennyiszer fut a ciklus (futásonként növelem 1-gyel)
while n:
	pont2 = int(input('A második dolgozat ' + str(sorsz2)+ '. pontszáma: '))
	if pont2 >= 0:
		dolgozat2.append(pont2)
		osszeg2 += pont2
		sorsz2 += 1
	else:
		n = False

atlag1 = [osszeg1 / len(dolgozat1)] #Az első dolgozat potjainak átlaga, azért listában tárolom, mert így minden kiíratott eredmény kapcsos zárójelben lesz
atlag2 = [osszeg2 / len(dolgozat2)] #A második dolgozat potjainak átlaga, azért listában tárolom, mert így minden kiíratott eredmény kapcsos zárójelben lesz

maxdelta1 = 0 #Átlagtól való maximális eltérés
maxelem1 = [] #Az átlagtól legmesszebb eső elem(ek) (több is lehet, pl: 15,11,8,12 esetén a 15 és a 8 is 3,5-re esik az átlagtól. Vagy ha mindenki ugyanannyit ért el.)
maxindex1 = [] #Az átlagtól legmesszebb eső elem(ek) helye(i) /Nem a listában lévő indexe!!!/
for j in range(len(dolgozat1)):
	if maxdelta1 == abs(dolgozat1[j] - atlag1[0]):
		maxelem1.append(dolgozat1[j])
		maxindex1.append(j+1)
	elif maxdelta1 < abs(dolgozat1[j] - atlag1[0]):
		maxdelta1 = abs(dolgozat1[j] - atlag1[0])
		maxelem1.clear()
		maxelem1.append(dolgozat1[j])
		maxindex1.clear()
		maxindex1.append(j+1)

maxdelta2 = 0 #Átlagtól való maximális eltérés
maxelem2 = []  #Az átlagtól legmesszebb eső elem(ek) (több is lehet, pl: 15,11,8,12 esetén a 15 és a 8 is 3,5-re esik az átlagtól. Vagy ha mindenki ugyanannyit ért el.)
maxindex2 = [] #Az átlagtól legmesszebb eső elem(ek) helye(i) /Nem a listában lévő indexe!!!/
for k in range(len(dolgozat2)):
	if maxdelta2 == abs(dolgozat2[k] - atlag2[0]):
		maxelem2.append(dolgozat2[k])
		maxindex2.append(k+1)
	elif maxdelta2 < abs(dolgozat2[k] - atlag2[0]):
		maxdelta2 = abs(dolgozat2[k] - atlag2[0])
		maxelem2.clear()
		maxelem2.append(dolgozat2[k])
		maxindex2.clear()
		maxindex2.append(k+1)

print('\nAz eredmény kiíratása')
print(100*'-') #csak tagolás miatt
print('{:68}'.format('Az első dolgozat pontszámai:'), dolgozat1)
print('{:68}'.format('Az első dolgozat potjainak átlaga:'), atlag1)
print('{:68}'.format('Az első dolgozatban az átlagtól legmesszebb eső elem(ek):'), maxelem1)  #Lehet több ugyanolyan pontszám, ezért csak az értékét adom meg.
print('{:68}'.format('Az első dolgozatban az átlagtól legmesszebb eső elem(ek) helye(i):'), maxindex1)
print(100*'-') #csak tagolás miatt
print('{:68}'.format('A második dolgozat pontszámai:'), dolgozat2)
print('{:68}'.format('A második dolgozat potjainak átlaga:'), atlag2)
print('{:68}'.format('A második dolgozatban az átlagtól legmesszebb eső elem(ek):'), maxelem2)  #Lehet több ugyanolyan pontszám, ezért csak az értékét adom meg.
print('{:68}'.format('A második dolgozatban az átlagtól legmesszebb eső elem(ek) helye(i):'), maxindex2)
