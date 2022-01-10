#Samuel Lockton 2021 ©

# Mathematical packages
import matplotlib
import numpy as np
from numpy.core.numeric import NaN
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import random
import math

# Utilities
import csv
import time
import collections
import copy
import talib as ta

import requests 
import json 
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import time



 
url = "http://api.isportsapi.com/sport/football/bookmaker?api_key=IsvK4UrjLX1moJg3"

# req_params = {"symbol" : symbol, 'interval' : interval, 'from' : startTime, 'to' : endTime}

response = json.loads(requests.get(url).text)
print(json.dumps(response["data"], indent = 4, sort_keys=True))
df = pd.DataFrame(response["data"])
df.to_csv('data.csv')
exit()
 
