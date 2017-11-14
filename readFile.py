
import fileinput
def main():
	# f1 = open('modifythis.txt', 'r')
	# print(f1.read())
	# f2 = open('modifythis.txt', 'w')
	# for line in f1:
	#     f2.write(line.replace(0, 7))
	# f1.close()
	# f2.close()
	#if the first char isn't a #, then look at it and replace numbers
	# f = open('modifythis.txt', r)
	# text = f.readline()
	# for i in text:
	# 	if i.char(0) != "#":		
	for line in fileinput.FileInput("modifythis.txt", inplace=True):
		if line[0] != '#':
			for char in line:
				if line in ['\n', '\r\n']:
					break
				if char != '0':
					line = line.replace(char, '0')
			print(line)
		else:
			print(line)
def new():
	file = open("jimmy.txt", "w+")
	r = 0
	for i in range(8):
		if i == 0:
			file.write("Jimmy Ti-Chieh Tsang \r\n")
		elif i == 6:
			from random import randint
			r = randint(0, 100)
			file.write(str(r) + "\r\n")
		elif i == 7:
			matrix =[[0 for x in range(r)] for y in range(r)]
			for a in range(0,r):
				matrix[a][a] = 1
			file.write(str(matrix))
		else:
			file.write("Maroon \r\n")
	file.close()
main()
new()