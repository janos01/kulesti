#Bodanitz Bora 2020.11.27 esti szoft
print ("Bodanitz Bora, 2020.11.27, esti")

#szamok lista
szamok=[]

#harom szamo bekerese, majd listaba rakasa
while len(szamok)!=3:
	szam=int(input('adj egy szamot: '))
	szamok.append(szam)

#a harom szam kozul a legnagyobb kiiratasa
print('legnagyobb szam: ',str(max(szamok)))

	

