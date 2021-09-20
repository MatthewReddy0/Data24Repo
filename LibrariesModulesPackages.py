import random
# import numpy as np
# import scipy as sp
import math
import os
import requests
import pprint as pp


request_bbc = requests.get('https://www.bbc.co.uk/news')
# pp.pprint(request_bbc.content)
pp.pprint(request_bbc.headers)
