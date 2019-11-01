import pandas as pd
import numpy as np

# Basic read just takes in a filename.
# Types are inferred where possible.
dataframe = pd.read_csv("data.csv")

print(dataframe.dtypes)
print(dataframe.head(2))


# By default, tries to parse data based on ',' delims.
# As there are no commas in the file, all data is treated as a single column.
incorrect_dataframe = pd.read_csv("strangeData.csv")
print(incorrect_dataframe)


slightly_better_dataframe = pd.read_csv("strangeData.csv", sep='|')
# Table now has three columns!
print(slightly_better_dataframe)

# However, we really want age to be treated as an integer column.
print(slightly_better_dataframe.dtypes)

# This dataframe has 3 columns as expected, is treating ~ as a missing value, and is
# treating age as an integer.
best_dataframe = pd.read_csv("strangeData.csv", sep='|', na_values='~', dtype={"age": "Int64"})
print(best_dataframe)
print(best_dataframe.dtypes)



# Default writing adds the row index, rereading this file will make our
# new dataframe look strange
best_dataframe.to_csv("./meh-output.csv")
reread_dataframe = pd.read_csv("./meh-output.csv")
print(reread_dataframe)


# This will get rid of the index values and just print out
# the data.
best_dataframe.to_csv("myoutput.csv", index=False)
reread_best_dataframe = pd.read_csv("myoutput.csv")
print(reread_best_dataframe)