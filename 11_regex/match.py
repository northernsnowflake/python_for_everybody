import re
x = 'My 2 favourite numbers are 19 and 42'
y = re.findall('[0-9]+', x) # find all possible matches of 1 or more digits
print(y)