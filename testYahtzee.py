# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:59:15 2023

@author: M.F.Weemeijer
"""

import random

throw = []

freq = []

conseq = []

for i in range(5):
     throw.append(random.randint(1, 6))
    
throw.sort()
res = [*set(throw)]

for i in range(len(res)-1):
    conseq.append(res[i+1]-res[i])
    
for i in range(1,7):
    freq.append(len([x for x in throw if x == i]))




    