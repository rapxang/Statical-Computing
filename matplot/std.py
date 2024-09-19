#1. Calculate the standard deviation, for the following
#numpy method
import numpy as np
SampleDataSet = 20, 15, 24, 10, 8, 19, 24
arr=np.array(SampleDataSet)
sample_sd = np.std(arr,ddof=1)
popn_sd = np.std(arr)
print("Sample Standard deviation by numpy",sample_sd)
print("Population Standard deviation by numpy",popn_sd)

#pandas method
import pandas as pd
Population= 84, 82, 90, 77, 75, 77, 82, 86, 82
pop_arr=pd.array(Population)
sam_sd=pop_arr.std()
pop_sd=pop_arr.std(ddof=0)
print("Sample Standard deviation by pandas",sam_sd)
print("Population Standard deviation by pandas",pop_sd)


#statistics method
import statistics
DataSet= 36, 27, 50, 42, 27, 36, 25, 40
sample_std=statistics.stdev(DataSet)
popn_std=statistics.pstdev(DataSet)
print("Sample Standard deviation by statistics",sample_std)
print("Population Standard deviation by statistics",popn_std)

import math
Datas= 1,2,3,4,5,6,7,8,9
mean=sum(Datas)/len(Datas)
squarred_values=sum((X-mean)**2 for X in Datas)/(len(Datas))
SD=math.sqrt(squarred_values)
print("Sample Standard Deviation by scratch",SD)













