print('Langó Luca Judit, SZOFT 1/E') 
print('készítette: 2020.12.05.')

def isfloat(str):
    try: 
        float(str)
    except ValueError: 
        return False
    return True

myList = []

for n in range(3):
	my_Number = None
	my_NumberIsFloat = False
	while not my_NumberIsFloat:
		my_Number = input('Enter number: ')
		my_NumberIsFloat = isfloat(myNumber)
		if not my_NumberIsFloat:
			print("    Please enter a real number instead!")
	
	print(f"    Appended real number: {my_Number}")
	my_List.append(myNumber)
    

print("Largest element is:", max(my_List)) 
