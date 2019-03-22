# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 22:51:25 2019

@author: Francisco.Verdejo
"""

from itertools import permutations
import time

valid = 0
p = permutations(range(1, 10))
t = time.time()

for i in p:
    x = i[0] + 13 * i[1] / i[2] + i[3] + 12 * i[4] - i[5] + i[6] * i[7] / i[8]
    if x == 87:
        print(i)
        valid += 1

elapsed = time.time() - t
print('This code took', round(elapsed, 2), 'seconds.')
