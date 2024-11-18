import matplotlib.pyplot as plt

# Example dataset
data = [65, 72, 78, 85, 90, 91, 92, 93, 95, 98, 100, 101, 102, 105, 110, 130, 150, 200]


# Create the box plot
plt.boxplot(data)

# Add titles and labels
plt.title("Box Plot Example")
plt.ylabel("Test Scores")

# Show the plot
plt.show()
