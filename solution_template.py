import numpy as np
import pandas as pd

test = True


if test:
	input_name = 'testinput.txt'

else:
	input_name = 'input.txt'

	
def read_data():
	with open (input_name) as f:
		data = f.readlines()
	return [d.strip() for d in data]

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###

def part1():
	data = read_data()

	for ii in range(len(data)):
		d = data[ii]
		pass
	return


###



def part2():
	data = read_data()
	thing = []
	for a in thing:
		pass

	return

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
