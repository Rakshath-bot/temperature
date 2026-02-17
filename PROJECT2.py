import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# Load the Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target
iris_df['species'] = iris_df['species'].map({0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'})

# Calculate the average sepal length for each species
avg_sepal_length = iris_df.groupby('species')['sepal length (cm)'].mean().reset_index()

# Create the bar plot
sns.barplot(x='species', y='sepal length (cm)', data=avg_sepal_length, palette='viridis')

# Add titles and labels
plt.title('Average Sepal Length by Iris Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Length (cm)')

# Display the plot
plt.show()
