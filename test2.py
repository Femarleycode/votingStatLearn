import pandas as pd
import pyreadstat

# Read the SPSS file
df, meta = pyreadstat.read_sav('data/BrexitAttitudes_Data.sav')

print("start")

# Print variable names
print(meta.column_names)

# Print variable labels
print(meta.column_labels)

# Print value labels (if any)
print(meta.variable_value_labels)

# Get the number of rows and columns
num_rows, num_cols = df.shape

# Print the number of rows and columns
print("Number of rows:", num_rows)
print("Number of columns:", num_cols)

print("stop")

# # Print variable types (numeric or string)
# print(meta.column_types)

# # Now you can work with the DataFrame 'df'

