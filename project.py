import matplotlib.pyplot as plt
import numpy as np
x_data = [0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90]
y_data = np.exp(x_data)
plt.plot(x_data, y_data)
plt.title('Temperature Rise')
plt.xlabel('X_data, Time')
plt.ylabel('Y_data, Temperature')
plt.show()
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [23, 45, 56, 78]

# Create the bar plot
plt.bar(categories, values, color='skyblue')

# Add titles and labels
plt.title('Bar Plot Example')
plt.xlabel('Categories')
plt.ylabel('Values')

# Display the plot
plt.show()

 #Data for the pie chart
labels = ['Tables', 'Charts', 'Graphs', 'Dashboards']
sizes = [25, 35, 20, 20]  # Hypothetical distribution of usage
colors = ['gold', 'lightblue', 'lightgreen', 'coral']
explode = (0, 0.1, 0, 0)  # Highlight 'Charts' for emphasis

# Create the pie chart
plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', startangle=140)

# Add title
plt.title('Distribution of Data Visualization Types')

# Display the plot
plt.show()
