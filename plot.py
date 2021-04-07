from matplotlib import pyplot as plt
import pandas as pd
import math
import numpy as np
data1= pd.read_csv('test.csv')
data2=pd.read_csv('testcenter.csv')
co=[]
np1=np.array(data1)
np2=np.array(data2)
print(np1-np2)
print(len(np1))
for i in range (len(np1)):
    dist = np.linalg.norm(np1[i]-np2[i])
    co.append(dist)
sum_co=float((np.sum(co)))
avg_co=(sum_co/666.0)
print('avg_distance:',avg_co)

plt.plot(co)
plt.show()

