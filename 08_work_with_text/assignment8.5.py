fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if line.startswith("From: "):
        count = count + 1
        line = line.strip('\n') # odděl to zalomení na nový řádek, jinak by to bylo vždy s mezerou mezy výsledky
        splitted = line.split('From: ')
        print(splitted[1])
print("There were", count, "lines in the file with From as the first word")