# This is my script for the wiki_tech_mini_coding_challenge
import re, random
infile = open('modifythis.txt', 'r')

def process(line):
    zero = '0'
    return re.sub('[^0\n]', zero, line)


for line in infile:
    # Strip any line endings from the line(\r, \n, or \r\n) then process the
    # line using the process_line function
    if (line[0] != "\n" and line[0] != '#'):
        data = process(line.rstrip("\r\n"))

        # Write the processed line to standard out.
        # print "{} {}".format(line, data)
        print (data + "->" + line)
    # print "%s -> %s" % (line, data)

# Close the file because we are done with it.
# infile.close()


outfile = open('jade.txt', 'w')
outfile.write("Jade Yen \n")

for index in range(5):
    outfile.write("I don't have one\n")

random_number = random.randint(1, 101)
outfile.write(str(random_number) + "\n")

# def identity(n):
#     for i in range(n):
#         id_row = [1 if i==j else 0 for j in range(n)]
#         return str(id_row)
        # outfile.write(str(id_row))
    # return [[1 if i==j else 0 for j in range(n)] for i in range(n)]

# identity(random_number)

for i in range(random_number):
    id_row = [1 if i==j else 0 for j in range(random_number)]
    outfile.write(str(id_row) + "\n")
# outfile.write(identity(random_number))

outfile.close()
