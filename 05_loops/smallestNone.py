smallest = None #start Flog value

print('Before')

for value in [9,4,12,3,74,15]:
    if smallest is None: #first time
        smallest = value
    elif value < smallest:
        smallest = value 
    print(smallest,value)
print('After', smallest)