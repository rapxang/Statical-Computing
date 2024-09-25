#A teacher records the scores of her students on a math test. The scores
# are normally distributed with a mean (average) of 75 and a standard deviation of 10

#If a student scores 85 on the test, what is the z-score for that student's test score?


import numpy as np
#given
mean=75
std=10
score=85
scores = np.array([-3,-2,-1,0,1,2,3])

zscore=(score-mean)/std
print("Z-score of the student is ",zscore)
print("The Z-score of the student is ",zscore,"standard deviation above the mean")

