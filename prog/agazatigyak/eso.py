# Nagy János, 2021-01-07, SZOFT I/1/E
print('Nagy János, 2021-01-07, SZOFT I/1/E')
print('------------------------------------')
print('Ágazati 001 mintafeladat megoldása')

print('Csapadék mennyiség milliméterben:')
aktualis = int(input('Aktuális heti csapadék: '))
elozo = int(input('Előző heti csapadék: '))

# itt át lehet alakítani számmá

if aktualis > elozo:
    print('Több csapadék')
elif elozo > aktualis:
    print('Kevesebb csapadék')
else:
    print('Nem változott')
