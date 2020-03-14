import sys
import random

def generate_nums(inputfile, num_rows, varchar_length, shuffle, multiplicity):

	array = []

	orig_stdout = sys.stdout
	f = open(inputfile, 'w')
	f.truncate()
	sys.stdout = f

	count = 0
	elem = 0
	while count < num_rows:
		temp = 0
		while temp < multiplicity:
			array.append(elem)
			count += 1
			temp+=1
		elem +=1
	
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
	generate_nums('/home/sahana/Documents/PQET/Prediction-of-Query-Execution-Time/merge_sort/nums.csv',1000000,20,0,1)
