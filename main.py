name = "Arthur, King of the Britons"
dob = "3rd Jan, 838 AD"
age = "37"
address = "Camelot, a silly place"
print(f"{name} was born on {dob} and is {age} yrs old. They live at {address}.")

dict_data = {1: {"name": "Isaac", "age": "140"}, 2: {"name": "Joy", "age": "59"}}
for i in dict_data.values():
    print(i["name"])

age = 'h'
while age.isdigit() is False:
    print('WHAT is your age?')
    age = input()
    if 0 < age < 117:
        continue
    else:
        print('Unfinished')


print('WHAT is the capital of Assyria?')
print('WHAT is the air speed velocity of a swallow')
