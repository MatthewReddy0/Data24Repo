import json
import requests
from pprint import pprint

# json.dumps()   Serialises json to a formatted string
# json.dump()    Creates a stream object and expects a file object to write to
car_data = {'name': 'tesla', 'engine': 'electric'}
car_data_json_string = json.dumps(car_data)
print(type(car_data_json_string))

# with open('new_json_file.json', 'w') as json_file:
#     json.dump(car_data, json_file)

with open('new_json_file.json') as json_file:
    car = json.load(json_file)
    print(type(car))
    print(car['name'])
    print(car['engine'])

"""
Here lies the https stuff
"""

postcodes_req = requests.get('https://api.postcodes.io/postcodes/GL528JF')
# print(postcodes_req.status_code)
# print(postcodes_req.headers)
# print(postcodes_req.content)
# print(postcodes_req.json())

# Always follow the documentation. Do what it says
json_body = json.dumps({'postcodes': ['PR3 0SG', 'M45 6GN', 'EX16 5BL']})
headers = {'Content-Type': 'application/json'}

post_multi_req = requests.post('https://api.postcodes.io/postcodes', headers=headers, data=json_body)
# pprint(post_multi_req.json())

cat_fact = requests.get('https://catfact.ninja/fact')
print(cat_fact .json())
