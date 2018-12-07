import json

# people_string = {
#                 "people" : [ { 
#                                 "name" : "James Smith", 
#                                 "phone": "563-759-5294", 
#                                 "emails" : ['artnuit@kmail.com','regtron@yawpmail.com'],
#                                 "has_license" : True
#                                 },
#                                 { 
#                                 "name" : "Jane Smith", 
#                                 "phone" : "375-438-8364",
#                                 "emails" : None ,
#                                 "has_license" : False
#                                 } 
#                             ]
#                 }

# data = json.dumps(people_string, indent=2)

# # with open('record.txt','w') as f:
# #     f.write(data)
# print(data, type(data))


## opening a json file ## 

with open("states.json",'r') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'], state['abbreviation'])

for state in data['states']:
    del state['area_codes']

with open("new_states.json",'w') as f:
    json.dump(data,f, indent = 2)



