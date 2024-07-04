count = dict()
names = ['csev','cwen','csev', 'zqian', 'cwen']

for name in names:
    count[name] = count.get(name,0) + 1
print(count)