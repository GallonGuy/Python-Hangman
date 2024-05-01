import matplotlib.pyplot as plt

# Define your data (replace these with your actual data)
x_values = [1, 2, 3, 4, 5]  # Replace with your X-axis data
left_y_values = [10, 20, 15, 25, 30]  # Replace with your left Y-axis data
right_y_values = [100, 80, 90, 70, 60]  # Replace with your right Y-axis data

# Create a figure and axis
fig, ax1 = plt.subplots()

# Plot the left y-axis data
ax1.plot(x_values, left_y_values, 'b', label='Left Y-axis')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Left Y-axis', color='b')
ax1.tick_params('y', colors='b')

# Create a second y-axis
ax2 = ax1.twinx()

# Plot the right y-axis data
ax2.plot(x_values, right_y_values, 'r', label='Right Y-axis')
ax2.set_ylabel('Right Y-axis', color='r')
ax2.tick_params('y', colors='r')

# Add a legend
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Show the plot
plt.title('Dual Y-axis Plot')
plt.show()
