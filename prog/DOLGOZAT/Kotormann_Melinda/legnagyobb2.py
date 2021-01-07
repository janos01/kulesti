# Kotormann Melinda
# Esti szoft E/1
# Készült:2020.12.06, Mikulás napján:)
# Ez a program bekér három valós számot és meghatározza közülük a legnagyobbat

print('Kotormann Melinda')
print('Esti szoft')
print('Készült 2020. Mikulás napján')
print('Ez a program bekér három valós számot és meghatározza közülük a legnagyobbat!')
print('Illetve nem írja ki, mert nem jöttem rá a megoldásra, sajnos')



szam = []

szam.append(int(input('Szám1: '))) 
szam.append(int(input('Szám2: ')))
szam.append(int(input('Szám3: '))) 


def legnagyobb(szamok):
	maximum = szamok[0]
	if maximum < szamok[1]:
		maximum = szamok[1]	
	if maximum < szamok[2]:	
		maximum = szamok[2]
	return maximum
	
	
print("A legnagyobb szám: ",legnagyobb(szam))



