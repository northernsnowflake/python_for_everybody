c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items(): #seradim dle item
    tmp.append((v,k))
print(tmp)

tmp = sorted(tmp, reverse=True) # chci to v opacnem poradi
print(tmp)