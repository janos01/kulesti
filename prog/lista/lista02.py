
print('Nevek vege végjelig')

nev = 'null'
nevek = []
while nev != 'vege':
    nev = input('Név: ')
    if nev != 'vege':
        nevek.append(nev)


for nevElem in nevek:
    print(nevElem)

print(nevek)