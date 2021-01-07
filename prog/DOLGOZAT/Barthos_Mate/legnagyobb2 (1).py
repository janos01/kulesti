#Barthos Máté 2020.12.07 esti szoftverfejlesztő
print ("Barthos Máté, 2020.12.07, esti")

#szamok lista
szamok=[]

#harom szám bekerese, majd listába rakása
while len(szamok)!=3:
	szam=int(input('adj egy szamot: '))
	szamok.append(szam)

#a harom szam kozul a legnagyobb kiiratasa
print('legnagyobb szam: ',str(max(szamok)))

	

