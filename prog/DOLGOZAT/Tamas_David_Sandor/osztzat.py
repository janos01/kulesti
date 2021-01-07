#Tamás Dávid Sándor
#SZOFT I/1/E
#2020-12-07

print( "A programot készítette: Tamás Dávid Sándor, SZOFT I/1/E, 2020. 12. 07." )

print( "A program, a megadott tanulók, két különálló dolgozatban elért pontszámmait kéri be, majd kiszámítja azok átlagát, valamint megállapítja melyik tanuló tért el legjobban az átlagtól." )

nevsor = [ ]

pontszamok1 = [ ] 

pontszamok2 = [ ]

letszam = int( input( "Adja meg, hány tanuló erdeményét szeretné rögzíteni: " ) ) 

if letszam > 1:

	print( "Adja meg a tanulók neveit:" )

elif letszam == 1:

	print( "Adja meg a tanuló nevét:" )

else:

	print( "Hiba! Legalább egy tanuló eredményét meg kell adnia!" )

for i in range( 0 , letszam ): 

	nevsor.append( str( input(  ) ) )

print( "Adja meg az első dolgozat pontszámait tanulónként." )

for i in range( 0 , letszam ):
	
	print( nevsor[i], "pontszáma: " )
	
	pontszamok1.append( int( input(  ) ) )
	
def Atlag( pontszamok1 ):
	
	return sum( pontszamok1 ) / len( pontszamok1 )

atlag1 = Atlag( pontszamok1 )

print( "Az első dolgozat pontszámainak átlaga: " , atlag1 )

kulonbseg1 = 0

kulonbseglist1 = [ ]

for i in range( 0 , letszam ):

	if pontszamok1[i] > atlag1:
		
		kulonbseg1 = pontszamok1[i] - atlag1
			
	else:
		
		kulonbseg1 = atlag1 - pontszamok1[i]
		
	kulonbseglist1.append(kulonbseg1)

print( nevsor[ kulonbseglist1.index( max( kulonbseglist1 ) ) ] , "tért el legjobban az első dolgozat átlagától." )
	
print( "Adja meg a második dolgozat pontszámait tanulónként." )

for i in range( 0 , letszam ):
	
	print( nevsor[i], "pontszáma: " )
	
	pontszamok2.append( int( input(  ) ) )

atlag2 = Atlag( pontszamok2 )

print( "A második dolgozat pontszámainak átlaga: " , atlag2 )

kulonbseg2 = 0

kulonbseglist2 = [ ]

for i in range( 0 , letszam ):

	if pontszamok2[i] > atlag2:
		
		kulonbseg2 = pontszamok2[i] - atlag2
			
	else:
		
		kulonbseg2 = atlag2 - pontszamok2[i]
		
	kulonbseglist2.append(kulonbseg1)

print( nevsor[ kulonbseglist2.index( max( kulonbseglist2 ) ) ] , "tért el legjobban a második dolgozat átlagától." )
