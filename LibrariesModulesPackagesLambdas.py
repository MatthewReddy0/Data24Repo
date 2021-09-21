import random
import math
import os
import requests
import pprint as pp


request_bbc = requests.get('https://www.bbc.co.uk/news')
# pp.pprint(request_bbc.content)
pp.pprint(request_bbc.headers)

# addition = lambda num1, num2: num1 + num2
# print(addition(3, 6))

savings = [234, 555, 674, 78]

bonus = list(map(lambda x: x*1.1, savings))
print(bonus)
