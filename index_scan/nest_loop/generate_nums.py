import sys
import random

def generate_nums(inputfile, num_rows, shuffle):

	array = []

	orig_stdout = sys.stdout
	f = open(inputfile, 'w')
	sys.stdout = f

	for i in range(num_rows):
		for j in range(100):
			array.append(i)
	
	if shuffle:
		random.shuffle(array)

	for elem in array:
		print(elem)

	sys.stdout = orig_stdout
	f.close()

if __name__ == "__main__":
	generate_nums('nums.csv',1000000,1)
