import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load the BES data into a pandas DataFrame
bes_data = pd.read_csv('bes_data.csv')

# Define the features and target variable
features = ['age', 'gender', 'education', 'income', 'region', 'ethnicity']
target = 'brexit_vote'

X = bes_data[features]
y = bes_data[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the logistic regression model
logistic_model = LogisticRegression()

# Fit the model to the training data
logistic_model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = logistic_model.predict(X_test)

# Evaluate the model's performance
accuracy = logistic_model.score(X_test, y_test)
print(f'Accuracy: {accuracy:.2f}')

# Print the coefficients
coefficients = pd.DataFrame(zip(X.columns, logistic_model.coef_[0]), columns=['Feature', 'Coefficient'])
print('Coefficients:')
print(coefficients)