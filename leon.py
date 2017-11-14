import re, random

with open("modifythis.txt") as f:
    lines = f.readlines()

new_lines = []

for line in lines:
    if line[0] != "#" and line[0] != "\n":
        new_line = re.sub("[^0\n]", "0", line)
        new_lines.append(new_line)
        print(line.rstrip() + " -> " + new_line.rstrip())
    else:
        new_lines.append(line)

with open("modifythis.txt", "w") as f:
    f.writelines(new_lines)


with open("leon.txt", "w") as f:
    f.write("Leon Ming\n")

    for _ in range(5):
        f.write("Orange\n")

    n = random.randint(1, 100)
    f.write(str(n) + "\n")
    for i in range(n):
        for j in range(n):
            if i == j:
                f.write("1")
            else:
                f.write("0")
        f.write("\n")
