import matplotlib.pyplot as plt
# Sample data: replace this with your actual profit data for each month
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
total_profit = [200, 300, 250, 400, 350, 450, 500, 550, 600, 650, 700, 800]
# Create the line plot
plt.plot(months, total_profit, marker='o', color='blue')
# Set labels
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
# Add a title (optional)
plt.title('Total Profit Over Months')
# Show the plot
plt.grid(True)
plt.show()
