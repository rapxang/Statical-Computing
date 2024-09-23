import matplotlib.pyplot as plt
import numpy as np

months=[1,2,3,4,5]
facecream=[2500,2630,2140,3400,3600]
facewash=[1500,
1200,
1340,
1130,
1740,
]

toothpaste=[5200,
5100,4550,5870,4560]
bathingsoap=[9200,
6100,
9550,
8870,
7760
]
shampoo=[1200,2100,
3550,
1870,
1560
]


moisturizer=[1500,1200,1340,1130,1740]
plt.plot(months, facewash,color='red',marker='o',label='FaceWash')

plt.plot(months, facecream,color='green',marker='o',label='Face Cream')

plt.plot(months, toothpaste,color='blue',marker='o',label='Toothpaste')
plt.plot(months, bathingsoap,color='purple',marker='o',label='Bathing Soap')
plt.plot(months, shampoo,color='brown',marker='o',label='Shampoo')
plt.plot(months, moisturizer,color='hotpink',marker='o',label='Moisturizer')


# Set labels and title
plt.xlabel('Month Number')
plt.ylabel('Sales Units in Number')
plt.legend(loc='upper left')
# Show the plot
plt.title('Sales Data')
plt.show()
