import json  #square brackets signalizes the list

input = '''[
    {"id" : "001",
    "x" : "2",
    "name" : "Chuck"
    },
    {"id" : "002",
    "x" : "7",
    "name" : "Berry"
    }
]'''
info = json.loads(input) #parse it
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])