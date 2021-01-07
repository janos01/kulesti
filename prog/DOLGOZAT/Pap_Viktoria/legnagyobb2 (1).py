Név= 'Pap Viktória, '
Osztály= 'Szoftverfejlesztő-esti, '
Dátum= '2020.11.29, '
Feladat='0412- 3 szám bekérése közöttük a legnagyobb meghatározása'
print(Név, Osztály, Dátum)

db = 3

keresett = float(input("1. szám: "))
legnagyobb = keresett

for i in range(2, db+1):
    keresett = float(input(str(i) + ". szám: "))
    if keresett > legnagyobb:
        legnagyobb = keresett
 
print("Legnagyobb szám:", legnagyobb)
 



