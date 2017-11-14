
import random

#ASSIGNMENT 1
def print_changes(old, new): 
	print(old + ' -> '+ new)

def remove_dirties():
	with open('wiki_tech_mini_coding_challenge-master/modifythis.txt', 'r+') as f:
		lines = f.readlines()
		for line_num in range(0, len(lines)):
			curr_line = lines[line_num].strip()
			if curr_line != '' and curr_line[0] != '#':
				old = curr_line
				new = ''
				for x in range(0,len(curr_line)):
					if curr_line[x] != '0':
						new += '0'
					else:
						new += curr_line[x]
				lines[line_num] = new + '\n'
				outfile = open('wiki_tech_mini_coding_challenge-master/modifythis.txt', 'w')
				outfile.writelines(lines)
				outfile.close
				print_changes(old, new)
		

#ASSIGNMENT 2
def generate_celena_file():
	outfile = open ('wiki_tech_mini_coding_challenge-master/celena.txt', 'w')
	rand_int = random.randrange(0, 100)

	#Creates identity matrix of rand_int size
	matrix=[['1' if x == y else '0' for y in range(rand_int)] for x in range(rand_int)]

	string_matrix = make_string_matrix(matrix)

	contents = ['Celena Chang\n', 
				['green\n' for x in range(0,5)],
				str(rand_int) + '\n',
				string_matrix]
	
	#Writing contents to celena.txt
	for x in range(len(contents)):
		#If element in contents is an array, separately write of the element's elements as its own line
		if isinstance(contents[x], list):
			for elem in contents[x]:
				outfile.write(elem)					
		else:
			outfile.write(contents[x])

	outfile.close()

#Transforms each row into its string representation
def make_string_matrix(matrix):
	string_matrix = []
	for r in matrix:
		row = ''
		for e in r:
			row += e
		string_matrix += [row + '\n']
	return string_matrix




