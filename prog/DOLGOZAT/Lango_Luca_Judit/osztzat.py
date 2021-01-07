import math

NUMBER_OF_TESTS = 2

def standard_deviation(xs):
	mean = sum(xs) / len(xs)   # mean
	print(f"    Mean: {mean}")
	var  = sum(pow(x-mean,2) for x in xs) / len(xs)  # variance
	print(f"    Variance: {var}")
	std  = math.sqrt(var)  # standard deviation
	print(f"    Standard deviation: {std}")
	return std


def enter_scores_of_test(test_id, number_of_subtasks_in_test):
	print(f"Enter scores of test {test_id+1}: ")
	scores_of_test = []
	for subtask in range(number_of_subtasks_in_test):
		scores_of_test.append(float(input(f"    Enter score of subtask {subtask+1}: ")))
	return scores_of_test

def argmax(a):
    return max(range(len(a)), key=lambda x: a[x])

def main():
	print('Langó Luca Judit, SZOFT 1/E') 
	print('készítette: 2020.12.05.')
	
	number_of_subtasks_in_test = int(input("Number of subtasks in test: "))
	print()
	
	tests = [] # [[...], [...], ...]
	standard_deviations = [] # [num1, num2, ...]
	
	for test_id in range(NUMBER_OF_TESTS):
		scores_of_test = enter_scores_of_test(test_id, number_of_subtasks_in_test)
		tests.append(scores_of_test)
		standard_deviations.append(standard_deviation(scores_of_test))
		print()
	
	print(f"The highest deviation was found in test {argmax(standard_deviations)+1}")
	
if __name__ == '__main__':
	main()

# fav    13 12 25 14 8
# index  0  1  2  3  4
# max          25
# argmax       2         - index of max number
