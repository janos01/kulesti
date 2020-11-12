

hok = [7.5, 5.8, 3.6, 2.7]

print('Első: ', hok[0])

hok2 = [7.5, 5.8, 3.6, 2.7]

if hok == hok2:
    print("egyenlő")

print(len(hok2))

for ho in hok:
    print('Hőmérséklet: ', ho)

nevek = ['Béla', 'Lajos', 'Zoltán']
if 'Béla' in nevek:
    print('Vana Béla')

voltFagy = False
for ho in hok:
    if ho < 0:
        voltFagy = True

if voltFagy:
    print("Volt fagyás")
else:
    print("Nem volt fagy")