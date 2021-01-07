# Nyíri Adrienn beadandó, osztzat, szoft 1 esti, 2020-12-10
# A bekért két dolgozat pontszámát átlagolja, illetve meghatározza melyik tér el jobban az átlagtól.


print('Nyíri Adrienn beadandó, osztzat, szoft 1 esti, 2020-12-10')
print('A bekért két dolgozat pontszámát átlagolja, illetve meghatározza melyik tér el jobban az átlagtól.')
print('Mivel két dolgozat van, ugyanannyira tér el az átlagtól')

def átlag(Szám1, Szám2):
    összeg = Szám1 + Szám2
    átlag = összeg/2
    return átlag

Szám1 = int(input('Szám1:'))
Szám2 = int(input('Szám2:'))

print('Átlag:', átlag(Szám1, Szám2))
