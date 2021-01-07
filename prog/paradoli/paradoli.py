
class Dolgozo:
	def __init__(self):
		self.nev = 'Névtlen'		
	def dolgozik(self):
		print('ás')
	def alszom(self):
		print('alszom')


mari = Dolgozo()
mari.nev = 'Nagy Mária'

print (mari.nev, ' ', end='')
mari.dolgozik()
mari.alszom()
