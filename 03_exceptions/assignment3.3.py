score = input("Enter score betweeen 0.0 and 1.0: ")

try:
    s = float(score)
except:
    print("Error")
    exit()

if s > 1.0:
    print("Error")
    exit()
if s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
elif s < 0.6:
    print("F")
else:
    print("Error")
    exit()
