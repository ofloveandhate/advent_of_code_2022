import numpy as np
import pandas as pd

test = False


if test:
	input_name = 'testinput.txt'

else:
	input_name = 'input.txt'

	
def read_data():
	with open(input_name) as f:
		data = f.read().rstrip()


	setup, instructions = data.split('\n\n')

	setup = setup.replace('    ',' [0] ').replace('[','').replace(']','').replace('\n','\n ').split('\n')
	
	setup = [ [c for c in s.split()] for s in setup[:-1]]

	
	setup = np.array(setup).T

	setup = [[c for c in list(setup[ii,:])[::-1] if c!='0'] for ii in range(setup.shape[0])]


	instructions = [ [int(c) for c in ell.split()] for ell in instructions.replace('move ','').replace('from ','').replace('to ','').split('\n')]


	return setup, instructions

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###




def part1():
	state, instructions = read_data()

	print(state)
	print(instructions)

	for num, source, dest in instructions:
		for ii in range(num):
			state[dest-1].append(state[source-1].pop(-1))

	print(state)
	return ''.join([stack[-1] for stack in state])


###



def part2():
	state, instructions = read_data()

	print(state)
	print(instructions)

	for num, source, dest in instructions:
		
		state[dest-1].extend(state[source-1][-num:])


		for ii in range(num):
			state[source-1].pop(-1)

	print(state)
	return ''.join([stack[-1] for stack in state])

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
