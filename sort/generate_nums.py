import sys
import random

def generate_nums(inputfile, num_rows, varchar_length, shuffle):

	array = []

	orig_stdout = sys.stdout
	f = open(inputfile, 'w')
	f.truncate()
	sys.stdout = f

	for i in range(num_rows):
		array.append(i)
	
	if shuffle:
		random.shuffle(array)

	varchar = ''

	for i in range(varchar_length):
		varchar = varchar + 'a'

	for elem in array:
		print(elem,varchar)

	sys.stdout = orig_stdout
	f.close()

if __name__ == "__main__":
	generate_nums('nums.csv',2528312,90,1)
