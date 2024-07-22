import json
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "inst1",
        "number" : " +1 724 303 4456"
        },
        "email" : {
            "hide" : "yes"
        }
}'''

info = json.loads(data)
print('Name:', info['name']) #info is dictionary, name is key # chuck
print('Phone:', info['phone']['number']) #info is dictionary, name is key
print('Hide', info['email']['hide']) # yes