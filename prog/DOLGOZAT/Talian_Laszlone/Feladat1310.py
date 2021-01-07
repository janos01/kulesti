#Írjon programot, amely bekéri két dolgozat elért pontszámait. A bekért pontszámokat a prog-ram átlagolja. Írjuk ki azt is, ki tért el leginkább az átlagtól. 

#Talián Lászlóné, 2020-11-28, esti szoftv

print('Talián Lászlóné, 2020-11-28, esti szoftv')
print('A 1310 feladat , Elért pontszámok')
print('Elért pontszámok bekérése, átlagolása, ki tér el leginkább az átlagtól')



Pontszam1 = int(input(' Pontszam1: '))
Pontszam2 = int(input(' Pontszam2: '))

Atlag = (Pontszam1 + Pontszam2) / 2

print('Atlag: ', Atlag)


if (Atlag - Pontszam1) >=  (Atlag - Pontszam2):
	print ("Pontszam1 eltér leginkább az átlagtól")

else:
	print ("Pontszam2 eltér leginkább az átlagtól")
	
