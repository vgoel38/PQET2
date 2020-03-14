import sys
import random

def generate_nums(inputfile, num_rows, moderate_shuffle):

	array = []

	orig_stdout = sys.stdout
	f = open(inputfile, 'w')
	sys.stdout = f

	count = 0
	for i in range(int(num_rows/10)):
		array.append([])
		for j in range(10):
			array[i].append(count)
			count+=1
	
	if moderate_shuffle:
		random.shuffle(array)

	for elem1 in array:
		for elem2 in elem1:
			print(elem2)

	sys.stdout = orig_stdout
	f.close()

if __name__ == "__main__":
	generate_nums('nums.csv',1000000,1)
