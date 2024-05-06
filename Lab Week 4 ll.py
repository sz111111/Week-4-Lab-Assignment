# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 05:44:14 2024

@author: ChelseySSS
"""

#SHIHAN ZHAO

#For the following questions, load the iris.csv dataset into a Pandas
#DataFrame. Make sure you set up an absolute path as described in 
#lecture, and if you're working with others, you should each update
#it to work on your computer.

#1. Explore the data.  How many categories of flowers are there? What
#   are the mean and median values, and the standard deviation?  How 
#   would you find the mean values per type of flower?  Right now you
#   can implement this with subsetting; next week we will cover how to
#   do this using groupby.

import pandas as pd

# Load the dataset
iris = pd.read_csv('C:/Users/ChelseySSS/Desktop/iris.csv')

# Explore the data
# Number of flower categories
categories = iris['species'].unique()
num_categories = len(categories)

# Get the mean, median, and the standard deviation
numeric_columns = iris.select_dtypes(include=[float, int])  
mean_values = numeric_columns.mean()
median_values = numeric_columns.median()
std_dev_values = numeric_columns.std()

# Mean values per type of flower 
mean_setosa = iris[iris['species'] == 'setosa'][numeric_columns.columns].mean()
mean_versicolor = iris[iris['species'] == 'versicolor'][numeric_columns.columns].mean()
mean_virginica = iris[iris['species'] == 'virginica'][numeric_columns.columns].mean()

# Print results
print("Number of categories:", num_categories)
print("Categories:", categories)
print("Mean values:\n", mean_values)
print("Median values:\n", median_values)
print("Standard Deviation:\n", std_dev_values)
print("Mean values for Setosa:\n", mean_setosa)
print("Mean values for Versicolor:\n", mean_versicolor)
print("Mean values for Virginica:\n", mean_virginica)

#2. Locate the max value across all four measures.  Use loc to display
#   just the rows that contain those values.

# Find the maximum values 
max_sepal_length = iris['sepal_length'].max()
max_sepal_width = iris['sepal_width'].max()
max_petal_length = iris['petal_length'].max()
max_petal_width = iris['petal_width'].max()

# Display rows where each measurement is at its maximum
max_sepal_length_row = iris.loc[iris['sepal_length'] == max_sepal_length]
max_sepal_width_row = iris.loc[iris['sepal_width'] == max_sepal_width]
max_petal_length_row = iris.loc[iris['petal_length'] == max_petal_length]
max_petal_width_row = iris.loc[iris['petal_width'] == max_petal_width]

# Print results
print("Row(s) with maximum sepal length:\n", max_sepal_length_row)
print("Row(s) with maximum sepal width:\n", max_sepal_width_row)
print("Row(s) with maximum petal length:\n", max_petal_length_row)
print("Row(s) with maximum petal width:\n", max_petal_width_row)

#3. How many of observations for each species of iris is in the data?

# Count the number of observations for each species
species_counts = iris['species'].value_counts()

# Print the counts
print("Number of observations per species:\n", species_counts)

#4. Using one line of code for each column, divide each value by the mean 
#   for that measure, and assign the result to four new columns.  How is this 
#   different from a zscore?  How would you make this a zscore instead?  What's 
#   the problem with doing this without accounting for the values in the 
#   species column?

# Creating New Columns by Dividing by Mean
iris['sepal_length_norm'] = iris['sepal_length'] / iris['sepal_length'].mean()
iris['sepal_width_norm'] = iris['sepal_width'] / iris['sepal_width'].mean()
iris['petal_length_norm'] = iris['petal_length'] / iris['petal_length'].mean()
iris['petal_width_norm'] = iris['petal_width'] / iris['petal_width'].mean()

print(iris['sepal_length_norm'])
print(iris['sepal_width_norm'])
print(iris['petal_length_norm'])
print(iris['petal_width_norm'])

# Difference from Z-Score
# The above  transformation divides each value by the mean of that measure. This normalization tells you how each value compares to the average of its column but does not consider the dispersion or spread of the data (i.e., how tightly the data points are clustered around the mean). 
# In contrast, a Z-score also considers the standard deviation of the data, giving a more complete picture of how far away each data point is from the mean in terms of standard deviations.

# Converting to Z-Scores

iris['sepal_length_z'] = (iris['sepal_length'] - iris['sepal_length'].mean()) / iris['sepal_length'].std()
iris['sepal_width_z'] = (iris['sepal_width'] - iris['sepal_width'].mean()) / iris['sepal_width'].std()
iris['petal_length_z'] = (iris['petal_length'] - iris['petal_length'].mean()) / iris['petal_length'].std()
iris['petal_width_z'] = (iris['petal_width'] - iris['petal_width'].mean()) / iris['petal_width'].std()

print(iris['sepal_length_z'])
print(iris['sepal_width_z'])
print(iris['petal_length_z'])
print(iris['petal_width_z'])

# Issues with Ignoring Species Column
# When we normalize or standardize the entire dataset without considering the species column, we ignore the inherent differences between the species. For instance, one species might naturally have larger sepal lengths than others. If we standardize across the entire dataset,
# we might lose this between-group variability, which could be crucial for certain analyses like clustering or classification.

#5. Create a new column named "petal_area" which is equal to the length
#   times the width.  Note that this isn't really the area of the petal, since
#   petals presumably aren't rectangles.

iris['petal_area'] = iris['petal_length'] * iris['petal_width']
print(iris['petal_area'])

#6. Subset the data to a new variable that is a dataframe with only virginica 
#   flowers.  Now add a new column to this subset that is equal to 1 if the 
#   sepal_length is greater than the mean sepal_length, else 0.  Did you get a
#   SettingWithCopyWarning message?  Modify your copying to do away with the 
#   warning.  Hint: You can create this with apply, or with map if you also
#   create a global variable holding the mean.

# Create a copy of the subset for virginica species
virginica = iris[iris['species'] == 'virginica'].copy()
print(virginica)

# Define a global variable for the mean sepal length
global mean_sepal_length_virginica
mean_sepal_length_virginica = virginica['sepal_length'].mean()

# Function to compare with the global mean
def compare_mean(x):
    return 1 if x > mean_sepal_length_virginica else 0

# Create a new column using map
virginica['sepal_length_gt_mean'] = virginica['sepal_length'].map(compare_mean)
print(virginica['sepal_length_gt_mean'])





