# This is my script for the wiki_tech_mini_coding_challenge
import re, random
infile = open('modifythis.txt', 'r')

def process(line):
    zero = '0'
    return re.sub('[^0]*', zero, line)

# Processing text files by line is typical but processing binary files by line
# is not. When processing binary files use .read(), .seek(), and .tell()
for line in infile:
    # Strip any line endings from the line(\r, \n, or \r\n) then process the
    # line using the process_line function
    if (line[0] != '#'):
        data = process(line.rstrip('\r\n'))

        # Write the processed line to standard out.
        # print "{} {}".format(line, data)
        print (line + "->" + data)
    # print "%s -> %s" % (line, data)

# Close the file because we are done with it.
infile.close()


outfile = open('jade.txt', 'w')
outfile.write("Jade Yen")

for index in range(6):
    outfile.write("I don't have one")

random_number = random.randint(1, 101)
outfile.write(str(random_number))

def identity(n):
    for i in range(n):
        id_row = [1 if i==j else 0 for j in range(n)]
        outfile.write(id_row)
    # return [[1 if i==j else 0 for j in range(n)] for i in range(n)]

outfile.write(identity(random_number))

outfile.close()
