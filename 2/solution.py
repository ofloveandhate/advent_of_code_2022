import numpy as np
import pandas as pd

def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
	return [d.strip() for d in data]

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')



winning_pairs = [('A','Y'),('B','Z'),('C','X')]
tying_pairs = [('A','X'),('B','Y'),('C','Z')]
value = {'X':1,'Y':2,'Z':3}


to_win = {'A':'Y','B':'Z','C':'X'}
to_tie = {'A':'X','B':'Y','C':'Z'}
to_lose = {'A':'Z','B':'X','C':'Y'}


def score(a,x):


	if (a,x) in winning_pairs:
		return 6 + value[x]
	elif (a,x) in tying_pairs:
		return 3 + value[x]
	else:
		return 0 + value[x]
###

def part1():
	data = read_data()
	q = []
	for ii in range(len(data)):
		d = data[ii]
		w = d.split()
		q.append(score(w[0],w[1]))

	
	return sum(q)


###

def strategy(a,x):
	if x=='X':
		return (a,to_lose[a])
	elif x=="Y":
		return (a,to_tie[a])
	else:
		return (a,to_win[a])


def part2():
	data = read_data()

	q = []
	for ii in range(len(data)):
		d = data[ii]
		w = d.split()
		q.append(score(*(strategy(w[0],w[1]))))

	return sum(q)

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
