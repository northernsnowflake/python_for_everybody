smalest = 76

print('Before', smalest)
for num in [9,4,12,3,74,15]:
    if num < smalest:
        smalest = num
    print(smalest,num)
print('After', smalest)