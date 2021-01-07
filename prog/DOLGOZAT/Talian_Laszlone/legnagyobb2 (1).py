
# Talián Milla
# 2020.11.28
# Esti szoftver
# Feladat 0412
# Legnagyobb valós szám

import math

print("Talián Milla, 2020.11.28, Esti szoftver")
print("Feladat 0412")
print("Legnagyobb valós szám")



valos1 = int(input(' valos1: '))
valos2 = int(input(' valos2: '))
valos3 = int(input(' valos3: '))

if valos2 < valos1 and valos3 < valos1:
	print (valos1)
 
elif valos1 < valos2 and valos3 < valos2:
	print (valos2)
			
elif valos1 < valos3 and valos2 < valos3:
	print (valos3)
	
else:
	print ("egyik sem teljesült")
	
