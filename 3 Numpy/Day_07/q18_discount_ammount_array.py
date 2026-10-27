'''
Calculate the discount amount for every product using broadcasting.
Then calculate the final prices.
'''

import numpy as np 

prices = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400]
])

discount = np.array([0.10, 0.20, 0.30]) 

print("Discount ammount:",prices - discount)

