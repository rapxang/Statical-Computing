
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("heart.csv")
print(df.head())
print(df.columns)




plt.scatter(df['age'], df['target'], label='Password Security', color='red')
plt.scatter(df['sex'], df['target'], label='Enable Security', color='Brown')
plt.scatter(df['cp'], df['target'], label='CSharing Location', color='Black')
plt.scatter(df['trestbps'], df['target'], label='Accept Unknown', color='Pink')
plt.scatter(df['chol'], df['target'], label='Number of Friends', color='Orange')
plt.scatter(df['fbs'], df['target'], label='Number of Groups', color='Purple')
plt.scatter(df['restecg'], df['target'], label='Click on Unknown Link', color='Green')



# Add labels and title
plt.xlabel('Behaviors')
plt.ylabel('target')
plt.title('Scatter plot of Correlation between Spam and Behaviors')
# Show legend
plt.legend(loc = 'lower right')
plt.grid(True)

# Display the plot
plt.show()






