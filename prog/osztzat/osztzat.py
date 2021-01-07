# Nagy János, 2020-12-17, esti szoft1
print("Nagy János, 2020-12-17, esti szoft1")
print("Két dolgozat pontszámait kéri be")


dolgozat1 = []
dolgozat2 = []

def beker():
    dolgozat = []
    pontszam = -2 
    while pontszam != -1:
        pontszam = int(input('Pontszám: '))
        if pontszam != -1:
            dolgozat.append(pontszam)
    return dolgozat

def atlag(dolgozat):
    darab = len(dolgozat)
    osszeg = 0
    for pontszam in dolgozat:
        osszeg += pontszam
    atlag = osszeg / darab;
    return atlag

def legnagyobbElterok(dolgozat, atlag):
    legnagyobbElteres = 0
    for pontszam in dolgozat:
        aktualisElteres = abs(atlag - pontszam)
        if aktualisElteres > legnagyobbElteres:
           legnagyobbElteres = aktualisElteres
    legnagyobbElterok = []     
    for pontszam in dolgozat:
        aktualisElteres = abs(atlag - pontszam)
        if aktualisElteres == legnagyobbElteres:
            legnagyobbElterok.append(pontszam)
    return legnagyobbElterok

print("Első dolgozat jegyei")
dolgozat1 = beker()
atlag1 = atlag(dolgozat1)
print('Első dolgozat átlaga: ', atlag1)
elterok = legnagyobbElterok(dolgozat1, atlag1)
print('Legnagyobb eltérés: ', elterok)

print("Második dolgozat jegyei")
dolgozat2 = beker()
atlag2 = atlag(dolgozat2)
print('Második dolgozat átlaga: ', atlag2)
elterok2 = legnagyobbElterok(dolgozat2, atlag2)
print('Legnagyobb eltérés: ', elterok2)





    


