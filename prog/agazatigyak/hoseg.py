# Nagy János, 2021-01-07, SZOFT I/1/E
print('Nagy János, 2021-01-07, SZOFT I/1/E')
print('------------------------------------')
print('Ágazati 001 mintafeladat megoldása')

print('Hőmérsékletek')

def fagy(ho):
    if ho < 0:
        return True
    else: 
        return False

ho = ''
while ho != 'vege':
    ho = input('Hő: ')
    if ho != 'vege':
        if fagy(int(ho)):
            print('Fagy volt')
        else:
            print('Nem volt fagy')
        
