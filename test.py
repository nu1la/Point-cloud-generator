import numpy as np
import random

p = random.uniform(0.01, 0.5)
n = random.randint(3, 25000)
pointLst = np.random.random((n, 3)) * 10
print(p)
print(n)
for i in range(len(pointLst)):
    print(str(pointLst[i][0]) + '\t' + str(pointLst[i][1])+ '\t' + str(pointLst[i][2]))
    
