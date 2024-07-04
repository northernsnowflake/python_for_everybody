name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = 0
one = dict()
for line in handle:
    if line.startswith("From: "): # vyhledavani vsech line s "From: "
        splitted = line.split()
        for split in splitted:  # spocitej je, vzdy pripocitej jedna
            one[split] = one.get(split,0) + 1
        if "From: " in one:
            del one["From: "]

# Hledani nejvetsiho vyskytu
bigcount = None
bigword = None

for word, count in one.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount) 