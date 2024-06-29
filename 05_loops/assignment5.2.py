largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        inum = int(num)
    except:
        print('Invalid input')
        continue

    for value in [inum]:
        if smallest is None: # first time
            smallest = value
        elif value < smallest:
            smallest = value

    for value in [inum]:
        if largest is None:
            largest = value
        elif value > largest:
            largest = value


print("Maximum is ",largest)
print("Minimus is ",smallest)
