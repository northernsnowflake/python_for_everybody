import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

y = re.findall('^From.(\S+@\S+)' ,x) # not gready
print(y)