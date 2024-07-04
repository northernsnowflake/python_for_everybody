line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008' 

words = line.split() # rozdělí text na slova podle mezer
print(words)
email = words[1]
pieces = email.split('@') # když dáme argument do závorky, říkám tím čím rozdělit
print(pieces[0])
print(pieces[1])