import matplotlib.pyplot as plt

# Data
days = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri']
drink_sales = [300, 450, 150, 400, 650]
food_sales = [400, 500, 350, 300, 500]

# Create subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 8))

# Plot drink sales
axs[0].plot(days, drink_sales, linestyle='--', color='cyan', marker='H', markersize=8, markerfacecolor='magenta', markeredgecolor='black')
axs[0].set_xlabel('Days of Week')
axs[0].set_ylabel('Sale of Drinks')
axs[0].set_title('Sales Data1', loc='right')
axs[0].set_title('PONNU AUGUSTINE\nMCA 2023-2025', loc='left')  # Multiple titles will only show the last one
axs[0].grid(True, color='blue', linestyle='dotted')

# Plot food sales
axs[1].plot(days, food_sales, linestyle='-', color='yellow', marker='D', markersize=8, markerfacecolor='green', markeredgecolor='red')
axs[1].set_xlabel('Days of Week')
axs[1].set_ylabel('Sale of Food')
axs[1].set_title('Sales Data2', loc='center')
axs[1].grid(True, color='blue', linestyle='dotted')

# Adjust layout and save
plt.tight_layout()
plt.savefig('prgrm2.png')  # Save as PNG file format
plt.show()  # Display the plot
