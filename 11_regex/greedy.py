import re
x = 'From: Using the : character'
y = re.findall('^F.+?:' , x) # first character in the match, one or more characters, last match

print(y)