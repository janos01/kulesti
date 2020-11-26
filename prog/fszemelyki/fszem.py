# Nagy János, 2020-11-26, esti szoft1

print('Nagy János, 2020-11-26, esti szoft1')
print('Feladat 1602 megoldása')
print('Személyek adatait kérjük és tároljuk')


fp = open('szemely.txt', 'w')
num = input('Sorszám: ')
while num != '0':
    nev = input('Név: ')
    telepules = input('Település: ')
    cim = input('Cím: ')
    jovedelem = input('Jövedelem: ')
    line = num + ":" + nev + ":" + telepules + ":" + cim + ":" + jovedelem + "\n"
    fp.write(line)
    num = input('Sorszám: ')

fp.close()
    
    
