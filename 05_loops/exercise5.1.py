num = 0
tot = 0.0

while True:
    sval = input('Enter number: ')
    if sval == "done": # exit mechanism
        break
    try: #checking of our input
        fval = float(sval)
    except:
        print("invalid input")
        continue # continue to the loop UP
    #print(fval)
    num = num + 1
    tot = tot + fval
print("All done")
print(tot, num, tot/num)