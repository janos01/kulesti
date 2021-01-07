#Nyíri Adrienn beadandó, legnagyobb2, szoft 1 esti, 2020-12-10
#A bekért három valósszámból meghatározom a legnagyobbat.
print('Nyíri Adrienn beadandó, legnagyobb2, szoft 1 esti, 2020-12-10')
print('A bekért három valósszámból meghatározom a legnagyobbat.')

számok = []

print('Első szám:')
szam1= float(input())
számok.append(szam1)

print('Második szám:')
szam2=float(input())
számok.append(szam2)

print('Harmadik szám:')
szam3=float(input())
számok.append(szam3)

ertek=int(számok[0])
for x in range (len(számok)):
    if float(számok[x])>ertek:
        ertek =számok[x]
print ('Legnagyobb érték:' , ertek)






