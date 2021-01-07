#Frantal Attila, 2020.11.27. , Szoft I/1/E

print('Frantal Attila, 2020.11.27. ,  Szoft I/1/E\n')

feladat="""Feladat 0412:
Adott három valós szám. Határozzuk meg közölük a legnagyobbat! A három számot kérjük be a felhasználóktól!
-----------------------------------------------------------------------------------------------------------"""

print(feladat+'\n')

print('Adj meg három valós számot:')
valos1 = float(input('Szám1: '))
valos2 = float(input('Szám2: '))
valos3 = float(input('Szám3: '))

print('\nA megadott 3 szám közül a legnagyobb érték: ', end='')
#ez az "if"-es megoldás
if valos2 <= valos1 and valos3 <= valos1:
	print(valos1)
elif valos1 <= valos2 and valos3 <= valos2:
	print(valos2)
elif valos1 <= valos3 and valos2 <= valos3:
	print(valos3)

#print(max(valos1,valos2,valos3))  #ez is egy jó megoldás beépített függvénnyel
