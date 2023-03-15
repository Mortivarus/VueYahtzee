# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:59:15 2023

@author: M.F.Weemeijer
"""

import random

throw = []

for i in range(5):
     throw.append(random.randint(1, 6))
    
throw.sort()
res = [*set(throw)]

nonConsecCount = 0

# for i in range(0, len(res)-1):
#     if(res[i] + 1 != res[i+1]):
#         nonConsecCount += 1
#     else:


size = []

conseqCount = 0

for i in range(0, len(res)-1):
    if(res[i] + 1 == res[i+1]):
        conseqCount += 1
        print(f"{res[i]+1}, {res[i+1]} ")
    else:
        size.append(conseqCount + 1)
        print(f"{res[i]+1}, {res[i+1]} ")
        conseqCount = 0
        continue
    size.append(conseqCount + 1)
        


     