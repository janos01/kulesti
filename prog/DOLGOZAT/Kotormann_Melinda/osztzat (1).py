# Kotormann Melinda
# Esti szoft E/1
# Készült:2020.12.06, Mikulás napján:)
# Ez a program bekéri két dolgozat elért pontszámait és átlagolja, majd kiirja hogy ki tért el leginkább az átlagtól!

print('Kotormann Melinda')
print('Esti szoft')
print('Készült 2020. Mikulás napján')
print('Ez a program bekéri két dolgozat elért pontszámait és átlagolja, majd kiirja hogy ki tért el leginkább az átlagtól!')


dolgozat1pontszam = int(input('Írja be a pontszámát: '))
dolgozat2pontszam = int(input('Írja be a pontszámát: '))


def atlag(dolgozat1pontszam, dolgozat2pontszam):
	eredmeny = (dolgozat1pontszam + dolgozat2pontszam)/2
	return eredmeny

print('Dolgozatok átlaga: ',atlag(dolgozat1pontszam, dolgozat2pontszam))		 

print('Figyelembe véve, hogy két tagunk van, kijelenthetjük, hogy egyformán térnek el az átlagtól!')
