import re
z = list()

count = 0
sum = 0
x = open('mbox-short.txt')
#x = open("regex_sum_160103.txt")

for line in x: # in every line
    words = line.strip('\n') # strip to the lines

    y = re.findall('([0-9]+)', words) #one or more numbers[0-9]+ in words
    z = z + y

for number in z:
    count = count+1 # add one per any of the list
    number = int(number) # transfotm str to the int
    sum = sum + number  # make a sum of all these extracted numebrs

print(count)
print(sum)