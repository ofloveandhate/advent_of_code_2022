import numpy as np
import pandas as pd

test = False


if test:
	input_name = 'testinput.txt'

else:
	input_name = 'input.txt'

	
def read_raw_data():
	with open (input_name) as f:
		data = f.readlines()
	return [d.strip() for d in data if d]





def read_data():
	raw = read_raw_data()

	return process(raw)


class Directory(object):
	"""docstring for Directory"""
	def __init__(self, name, depth):
		super(Directory, self).__init__()

		self.name = name
		self.contents = []
		self.depth = depth

	def size(self):
		return sum([s.size() for s in self.contents])

	def add_content(self, content):
		if content is self:
			raise ValueError(f'trying to add {content}, but is same as {self}')
		self.contents.append(content)

	def __repr__(self):
		return self.name
		# r = '\n'+' '*self.depth+f'- {self.name}\n'

		# for c in self.contents:
		# 	r = r+' '*(self.depth+1) + str(c)
		# return r

	def __str__(self):
		return repr(self)

	def subdirectories(self):

		subdirs = [c.subdirectories() for c in self.contents if isinstance(c,Directory)]

		ans = []
		for s in subdirs:
			ans.extend(s)
		ans.append(self)

		return ans


class File(object):

	def __init__(self,size, name):
		super(File, self).__init__()


		self._size = int(size)
		self.name = name


	def size(self):
		return self._size

	def __repr__(self):
		return f'File({self.name}, {self._size})'

	def __str__(self):
		return repr(self)


def process(raw):
	# expects a list of strings.

	raw.pop(0)
	root = Directory('/',0)

	dir_stack = [root]
	current_directory = root # should be a reference to the Directory

	while len(raw)>0:


		line = raw.pop(0)

		if line.startswith('$'):
			command = line.split()[1]

			if command == "cd":
				where = line.split()[2]

				if where == '..':
					dir_stack.pop(-1)
					current_directory = dir_stack[-1]

				else:
					found_dir = False
					for c in current_directory.contents:
						if c.name == where:
							dir_stack.append(c)
							current_directory = c
							found_dir = True
					if not found_dir:
						raise ValueError(f'failed to find an existing directory with name {where} in {current_directory.name} (contents {current_directory.contents}), processing line {line}')

			elif command == "ls":	
				contents = []
				while (len(raw)>0) and (not raw[0].startswith('$')):
					contents.append(raw.pop(0))

				for c in contents:


					if c.startswith('dir'):
						n = c.split()[1]

						current_directory.add_content(Directory(n, depth=len(dir_stack)))

					else:
						current_directory.add_content(File(*(c.split())))


	return root


def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###

def part1():
	data = read_data()
	sizes = [s.size() for s in data.subdirectories()]
	return sum([s for s in sizes if s <=100000])


###



def part2():
	data = read_data()
	sizes = [s.size() for s in data.subdirectories()]

	total_space = 70000000
	desired_free_space = 30000000

	size_root = data.size()

	current_free = total_space - size_root

	deficiency = desired_free_space - current_free



	df = pd.DataFrame({'sizes':[s.size() for s in data.subdirectories()]})

	return int(df[df>deficiency]['sizes'].min())




print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
