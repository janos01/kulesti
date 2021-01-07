#Bodanitz Bora 2020.11.27 esti szoft
print ("Bodanitz Bora, 2020.11.27, esti")

#ket dolgozat pontszamainak bekerese
doga1=int(input('elso dolgozat pontszama: '))
doga2=int(input('masodik dolgozat pontszama: '))

#dolgozat atlagai
atlag=(doga1+doga2)/2

#dolgozatok atlagtol valo eltérésenek kiiaratsa
#felesleges muvelet, mert ket dolgozat eseten ugyanakkora lesz az elteres
if abs(doga1-atlag)>abs(doga2-atlag):
	print("az elso dolgozat ter el jobban az atlagtol")
elif abs(doga1-atlag)<abs(doga2-atlag):
	print("a masodik dolgozat ter el jobban az atlagtol")
else:
	print("ugyanakkora az elteres.")


