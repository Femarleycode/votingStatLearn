import pandas as pd
import pyreadstat
import matplotlib.pyplot as plt
import seaborn as sns

# Read the SPSS file
df, meta = pyreadstat.read_sav('data/BrexitAttitudes_Data.sav')

print("start")

# # Print variable names
# print(meta.column_names)

# # Print variable labels
# print(meta.column_labels)

# # Print value labels (if any)
# print(meta.variable_value_labels)


# Print top 5 rows
print(df.head())

# Histograms
# df.hist(figsize=(15,15))
# plt.tight_layout()
# plt.show()



plt.figure(figsize=(14,6))
plt.subplot(1,2,1)
df['EURef2016'].value_counts().plot(kind='bar')
plt.title("Bar")

plt.subplot(1,2,2)  
df['EURef2016'].value_counts().plot(kind='pie',labels=["Yes", "No", "Skip", "Forgot"], autopct="%.2f%%")
plt.title("Pie")
plt.show()


# Check for age distribution for candidates backing out after Round 1 and 2
# 0 stands for Retained , 1 stands for Left

# Drop people who forgot or didn't vote
print(df['EURef2016'].value_counts())
# Assuming df is your DataFrame and values_to_drop is a list of values
values_to_drop = [3.0, 4.0]  # List of values to drop

# Drop rows where column 'age' contains any value from the list values_to_drop
df = df[~df['EURef2016'].isin(values_to_drop)]
print(df['EURef2016'].value_counts())





# Plot
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='age', hue='EURef2016')
plt.title('Distribution of EU Referendum Votes by Age')
plt.xlabel('Age')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='EU Referendum Vote')
plt.tight_layout()
plt.show()



