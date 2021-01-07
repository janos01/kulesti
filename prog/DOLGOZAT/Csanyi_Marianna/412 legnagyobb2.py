"""Feladat 0412
Adott három valós szám. Határozzuk meg közölük a legynagyobbat! 
A három számot kérjük be a felhasználóktól!
"""

#Csányi Marianna
#2020.12.01
#esti Szoft I.

print('Csányi Marianna, 2020.12.01, esti Szoft I')  
print('Feladat 0412 megoldása')        
print('Legnagyobb valós szám meghatározása')

szam1 = float(input('Szám1: ')) 
szam2 = float(input('Szám2: ')) 
szam3 = float(input('Szám3: '))

if szam2 < szam1 and szam3 < szam1:              
	print('Legnagyobb valós szám: ', szam1)
elif szam1 < szam2 and szam3 < szam2:
	print('Legnagyobb valós szám: ', szam2)
elif szam1 < szam3 and szam2 < szam3:
	print('Legnagyobb valós szám: ', szam3)
