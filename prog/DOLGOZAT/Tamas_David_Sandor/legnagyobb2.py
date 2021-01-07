#Tamás Dávid Sándor
#SZOFT I/1/E
#2020-12-07

print( "A programot készítette: Tamás Dávid Sándor, SZOFT I/1/E, 2020. 12. 07." )

print( "A program három valós számot kér be, majd ezek közül meghatározza a legnagyobbat." )

number1 = None

number2 = None

number3 = None

number1 = int( input( "Első szám: " ) )

number2 = int( input( "Második szám: " ) )

number3 = int( input( "Harmadik szám: " ) )

if number1 > number2 and number1 > number3:
	
	print( "Az első szám a legnagyobb." )
	
elif number2 > number1 and number2 > number3:
	
	print( "A második szám a legnagyobb." )
	
elif number3 > number1 and number3 > number2:
	
	print( "A harmadik szám a legnagyobb." )
	
else:
	
	print( "Hiba! Kettő, vagy több szám is megfelel a feltételeknek." )
