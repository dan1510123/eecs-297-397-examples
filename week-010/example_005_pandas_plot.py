import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("numbers.csv")

# Can select individual columns
print("col x:", data['x'], sep='\n')
print("col y:", data['y'], sep='\n')


# Can get basic stats for columns with describe
print("data stats:", data.describe(), sep='\n')

# Can also target certain values (for entire dataframe or a single column)
print(data['x'].min())


# It's possible to combine data from multiple dataframes. This example
# creates a new dataframe by doubling each value in the original dataframe
data_2 = data * 2
print("doubled-data:", data_2.describe(), sep='\n')


# Can also concatenate data in multiple dataframes
data_3 = pd.concat([data, data_2])
print("concat data:", data_3.describe(), sep='\n')

# Dataframes are capable of generating different types of plots.
# Scatter plot example:
plt.figure()
data_3.plot.scatter('x', 'y')


# Pandas can bin data
data_3['x-bin'] = pd.cut(data_3['x'], bins=range(-10, 10, 1))
print("bins for x column:", data_3['x-bin'].value_counts(), sep='\n')


# Can also bin datas into buckets evenly
data_3['y-bin'] = pd.qcut(data_3['y'], 10)
print("y-bin:", data_3['y-bin'].head(10), sep='\n')


# Can plot out the bucket counts
plt.figure()
bar_data = data_3[['x-bin', 'x']].groupby('x-bin').count().plot()

plt.figure()
bar_data = data_3[['y-bin', 'y']].groupby('y-bin').count().plot(kind='bar')



# It's possible to select a subset of data.
# Let's find all rows with positive x and y values.
# Note that the conditional syntax is slightly different than what you would
# expect to see with plain old Python conditionals.

positive_vals = data_3[(data_3['x'] > 0) & (data_3['y'] > 0)]
print("positive stats:", positive_vals.describe(), sep='\n')

negative_vals = data_3[(data_3['x'] < 0) & (data_3['y'] < 0)]
print("negative stats:", negative_vals.describe(), sep='\n')


# Can capture the output of a plot call to get the axis object
# for the plot. Can set the ax argument to future plot calls
# in order to display other dataframes on the same plot
plt.figure()
plot_axis = positive_vals.plot.scatter(x='x', y='y', c='red')
negative_vals.plot.scatter(x='x', y='y', c='blue', ax=plot_axis)