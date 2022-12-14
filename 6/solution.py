import numpy as np
import pandas as pd

test = False


if test:
	input_name = 'testinput.txt'

else:
	input_name = 'input.txt'

	
def read_data():
	with open (input_name) as f:
		data = f.readlines()
	return [d.strip() for d in data if d]

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###

def part1():
	data = read_data()
	data = data[0]
	

	for ii in range(len(data)-4):
		
		if len(set(data[ii:ii+4]))==4:
			return ii+4
	return -1


###



def part2():
	data = read_data()
	data = data[0]
	

	for ii in range(len(data)-14):
		
		if len(set(data[ii:ii+14]))==14:
			return ii+14
	return -1

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
