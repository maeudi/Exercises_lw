# pylint: disable=missing-docstring

# TODO: 1st exercise: Define the `forward_price` function
from math import e
interest_rate = 0.03 
spot_price = 0 
time = 1 
rt = time * interest_rate 
forward_price = spot_price * (e**rt)
print(forward_price) 

# TODO: 2nd exercise: Define the `short_pnl` function