#1. Calculate the standard deviation, for the following
import pandas as pd
import numpy as np
SampleDataSet = 20, 15, 24, 10, 8, 19, 24
arr=np.array(SampleDataSet)
sample_sd = np.std(arr,ddof=1)
popn_sd = np.std(arr)
print("Sample Standard deviation by numpy",sample_sd)
print("Population Standard deviation by numpy",popn_sd)

sam_sd=arr.std()
pop_sd=arr.std(ddof=0)
print("Sample Standard deviation by pandas",sam_sd)
print("Population Standard deviation by pandas",pop_sd)






