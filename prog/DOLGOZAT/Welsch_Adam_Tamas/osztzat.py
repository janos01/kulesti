#(Welsch Ádám Tamás, 2020.12.05, Külker Esti Szoftver,Két user input szám bekérése majd átlag számítása,írjuk ki azt is, ki tért el leginkább az átlagtól.)
print("Welsch Ádám Tamás, 2020.12.05, Külker Esti Szoftver, Két user input szám bekérése majd átlag számítása,írjuk ki azt is, ki tért el leginkább az átlagtól.")
num = 2
total_sum = 0
for n in range(num):
    numbers = float(input('Adja meg a dolgozata elért pontszámát  : '))
    total_sum += numbers
avg = total_sum/num
print(num,' db dolgozat átlaga:', avg)
print("Két szám átlaga mindig ugyanannyira tér el az átlagtól")
