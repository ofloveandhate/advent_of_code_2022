import numpy as np
import pandas as pd

def read_data():
	with open ('input.txt') as f:
		data = f.read()
	return data.split('\n\n')

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###

def part1():
	data = read_data()
	q = []
	for ii in range(len(data)):
		d = data[ii]
		q.append(sum([int(w) for w in d.split()]))
		
	return max(q)


###



def part2():
	data = read_data()
	q = []
	for ii in range(len(data)):
		d = data[ii]
		q.append(sum([int(w) for w in d.split()]))
	
	q.sort()
	return sum(q[-3:])

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
