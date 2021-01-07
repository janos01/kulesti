#(Welsch Ádám Tamás, 2020.12.05, Külker Esti Szoftver,Adott három valós szám. Határozzuk meg közölük a legynagyobbat! A három számot kérjük be a felhasználóktól!)
print("Welsch Ádám Tamás, 2020.12.05, Külker Esti Szoftver, Adott három valós szám. Határozzuk meg közölük a legynagyobbat! A három számot kérjük be a felhasználóktól!")
num1 = float(input("Adja meg az első számot: "))
num2 = float(input("Adja meg a második számot: "))
num3 = float(input("Adja meg a harmadik számot: "))
 
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3
 
print("A legnagyobb szám",largest)
