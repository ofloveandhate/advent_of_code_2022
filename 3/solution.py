import numpy as np
import pandas as pd


test = False


if test:
	input_name = 'testinput.txt'

else:
	input_name = 'input.txt'


def read_data():
	with open(input_name) as f:
		data = f.readlines()
	return [d.strip() for d in data]

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###

def priority(c):
	if c.islower():
		return ord(c)-ord('a')+1
	else:
		return ord(c)-ord('A')+1+26

def part1():
	data = read_data()

	common_elements = []
	for ii in range(len(data)):
		d = list(data[ii])

		L = len(d)

		a,b = d[:L//2], d[L//2:]
		a = set(a)
		b = set(b)

		common_this = list(a.intersection(b))

		assert len(common_this)==1

		common_elements.append(common_this[0])

	
	priorities = [priority(c) for c in common_elements]

	return sum(priorities)


###



def part2():
	data = read_data()

	badges = []
	for ii in range(0,len(data),3):
		A = list(data[ii])
		B = list(data[ii+1])
		C = list(data[ii+2])

		a = set(A)
		b = set(B)
		c = set(C)

		badge_this = list(a.intersection(b.intersection(c)))

		assert len(badge_this)==1

		badges.append(badge_this[0])

	
	priorities = [priority(c) for c in badges]

	return sum(priorities)

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
