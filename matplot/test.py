from tracemalloc import Statistic

import numpy as np
import pandas as pd
import statistics


SampleDataSet = 20, 15, 24, 10, 8, 19, 24
# datas=np.array(SampleDataSet)
# sample_std=np.std(datas,ddof=1)
# popn_std=np.std(datas)
# print("standasrd deviation sample=",sample_std)
# print("popn stad = ",popn_std)
#
# data=pd.Series(SampleDataSet)
# sample_std=data.std()
# popn_std=data.std(ddof=0)
# print("standasrd deviation sample=",sample_std)
# print("popn stad = ",popn_std)
# sample_std=statistics.stdev(SampleDataSet)
# popn_std=statistics.pstdev(SampleDataSet)
# print("standasrd deviation sample=",sample_std)
# print("popn stad = ",popn_std)

# import statistics
# mean=7
# std= 1.3
# z_score=statistics.NormalDist(mean,std).zscore(5)
# print(z_score)

import scipy.stats as stats
data = np.array([6, 7, 7, 12, 13, 13, 15, 16, 19, 22])
z_score=stats.zscore(data)
print(z_score)


from scipy.stats import zscore
z=zscore(data)
print("z score direct import = ",z)


import  numpy as np

np.random.seed(4)
datas=np.random.randint(0,5,(3,3))
zz=zscore((datas))
print("Randomselection =", zz)