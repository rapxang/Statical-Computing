import matplotlib.pyplot as plt
import numpy as np

months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
facecream = np.array([2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900])
facewash = np.array([1500, 1200, 1340, 1130, 1740, 1555,
                     1120,
                     1400,
                     1780,
                     1890,
                     2100,
                     1760
                     ])
toothpaste = np.array([5200, 5100, 4550, 5870, 4560, 4890,
                       4780,
                       5860,
                       6100,
                       8300,
                       7300,
                       7400
                       ])
bathingsoap = np.array([9200, 6100, 9550, 8870, 7760, 7490,
                        8980,
                        9960,
                        8100,
                        10300,
                        13300,
                        14400
                        ])
shampoo = np.array([1200, 2100, 3550, 1870, 1560, 1890,
                    1780,
                    2860,
                    2100,
                    2300,
                    2400,
                    1800
                    ])

moisturizer = [1500, 1200, 1340, 1130, 1740, 1555,
               1120,
               1400,
               1780,
               1890,
               2100,
               1760
               ]
plt.plot(months, facewash, color='red', marker='o', label='FaceWash')

plt.plot(months, facecream, color='green', marker='o', label='Face Cream')

plt.plot(months, toothpaste, color='blue', marker='o', label='Toothpaste')
plt.plot(months, bathingsoap, color='purple', marker='o', label='Bathing Soap')
plt.plot(months, shampoo, color='brown', marker='o', label='Shampoo')
plt.plot(months, moisturizer, color='hotpink', marker='o', label='Moisturizer')

# Set labels and title
plt.xlabel('Month Number')
plt.ylabel('Sales Units in Number')
plt.legend(loc='upper left')
# Show the plot
plt.title('Sales Data')
plt.show()
