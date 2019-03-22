# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 21:18:46 2019

@author: Francisco.Verdejo
"""

# Empiezo a las 21:20
# Resultados correctos a las 22:00

import time

nn = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cases = 0
valid = 0
t = time.time()


# vaya tela fran 

for a in nn:
    nn.remove(a)
    for b in nn:
        nn.remove(b)
        for c in nn:
            nn.remove(c)
            for d in nn:
                nn.remove(d)
                for e in nn:
                    nn.remove(e)
                    for f in nn:
                        nn.remove(f)
                        for g in nn:
                            nn.remove(g)
                            for h in nn:
                                nn.remove(h)
                                for i in nn:
                                    r = a + 13 * b / c + d + 12 * e - f + g * h / i  # = 87
                                    if r == 87:
#                                        print(a, b, c, d, e, f, g, h, i)
                                        valid += 1
                                    cases += 1
                                nn.append(h)
                                nn.sort()
                            nn.append(g)
                            nn.sort()
                        nn.append(f)
                        nn.sort()
                    nn.append(e)
                    nn.sort()
                nn.append(d)
                nn.sort()
            nn.append(c)
            nn.sort()
        nn.append(b)
        nn.sort()
    nn.append(a)
    nn.sort()

elapsed = time.time() - t
print('This code took', round(elapsed, 2), 'seconds.')
