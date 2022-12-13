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
	return [d.strip() for d in data]

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###

def contains(a,b,c,d):

	if a>=c and b<=d:
		return True

	if c>=a and d<=b:
		return True

	return False

def part1():
	data = read_data()


	counter = 0
	for ii in range(len(data)):
		d = data[ii]

		e = d.split(',')

		f = e[0].split('-')
		f.extend(e[1].split('-'))
		g = [int(i) for i in f]

		a,b,c,d = g

		counter += int(contains(a,b,c,d))

	return counter


###

def overlaps(a,b,c,d):

	A = set(range(a,b+1))
	B = set(range(c,d+1))


	return len(A.intersection(B))>0



def part2():
	data = read_data()

	counter = 0
	for ii in range(len(data)):
		d = data[ii]

		e = d.split(',')

		f = e[0].split('-')
		f.extend(e[1].split('-'))
		g = [int(i) for i in f]

		a,b,c,d = g

		counter += int(overlaps(a,b,c,d))

	return counter

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
