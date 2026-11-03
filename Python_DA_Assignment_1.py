
# Python DA Assignment 1
# Section 1: NumPy Array Operations

import numpy as np

# Que 1: Create a 1D NumPy Array

temperatures_w1 = np.array([22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9])

print("Week 1 Temperatures:", temperatures_w1)


# Que 2: Inspection and Properties

print("Shape:", temperatures_w1.shape)
print("Data Type:", temperatures_w1.dtype)
print("Number of Elements:", temperatures_w1.size)

# Que 3: Array Operations

# Convert Celsius to Fahrenheit
temperatures_f = (temperatures_w1 * 9/5) + 32
print("Temperatures in Fahrenheit:", temperatures_f)

# Find maximum temperature
print("Maximum Temperature:", temperatures_w1.max())

# Find minimum temperature
print("Minimum Temperature:", temperatures_w1.min())

# Find mean temperature
print("Mean Temperature:", temperatures_w1.mean())

# Que 4: Array Slicing and Indexing

# a. First three days
print("First three days:", temperatures_w1[:3])

# b. Weekend temperatures
print("Weekend temperatures:", temperatures_w1[-2:])

# c. Middle three days
print("Middle three days:", temperatures_w1[2:5])

# Que 5: Create a 2D Array

temperatures = np.array([
    [22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9],
    [19.2, 22.5, 21.3, 24.0, 23.5, 22.8, 20.1]
])

print("Two Weeks Temperatures:")
print(temperatures)

# Que 6: Inspect and Slice the 2D Array

# a. Inspect array properties
print("Shape:", temperatures.shape)
print("Data Type:", temperatures.dtype)
print("Total Elements:", temperatures.size)

# b. Extract temperatures for each week
print("Week 1 Temperatures:", temperatures[0])
print("Week 2 Temperatures:", temperatures[1])

# c. Extract weekend temperatures for both weeks
print("Weekend Temperatures:", temperatures[:, -2:])


import pandas as pd

# Pandas Series

# Que 1: Creating Pandas Series

marks = pd.Series(
    [95, 92, 89, 85, 80],
    index=['Rank1', 'Rank2', 'Rank3', 'Rank4', 'Rank5']
)

print("Student Marks:")
print(marks)

# Que 2: Indexing and Slicing

# a. Access 1st rank using integer index position
print("1st Rank Mark:", marks.iloc[0])

# b. Retrieve top 3 ranks using loc
print("Top 3 Ranks:", marks.loc[['Rank1', 'Rank2', 'Rank3']])

# c. Access 3rd rank using iloc
print("3rd Rank Mark:", marks.iloc[2])

# d. Filter marks greater than 90
print("Marks greater than 90:", marks[marks > 90])

# Que 3: Manipulating Series

# a. Modify the 1st rank mark to 100
marks.loc['Rank1'] = 100
print("After updating Rank1:", marks)

# b. Remove the last rank
marks = marks.drop('Rank5')
print("After removing Rank5:", marks)

# c. Calculate CGPA
cgpa = marks / 10
print("CGPA:", cgpa)

# Pandas DataFrame

# Que 1: Creating Pandas DataFrame

transactions = pd.DataFrame({
    'TransactionID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],

    'ProductCategory': [
        'Electronics', 'Clothing', 'Electronics', 'Furniture',
        'Clothing', 'Electronics', 'Furniture', 'Clothing',
        'Furniture', 'Electronics'
    ],

    'Region': [
        'North', 'South', 'North', 'East', 'West',
        'North', 'East', 'West', 'South', 'North'
    ],

    'Amount': [200, 150, 300, 450, 200, 250, 300, 180, 350, 400]
})

print("Transactions DataFrame:")
print(transactions)

# Que 2: Data Exploration

# a. Display DataFrame and basic information
print("First 5 Rows:")
print(transactions.head())

print("Last 5 Rows:")
print(transactions.tail())

print("Shape:", transactions.shape)

print("Column Names:", transactions.columns)

print("Data Types:")
print(transactions.dtypes)

print("DataFrame Information:")
transactions.info()

# b. Display ProductCategory and Amount columns

print("Product Category and Amount:")
print(transactions[['ProductCategory', 'Amount']])

# c. Retrieve the last 3 columns using iloc

print("Last 3 Columns:")
print(transactions.iloc[:, -3:])

# d. Filter rows based on conditions

print("North Region Transactions with Amount greater than 200:")

filtered_data = transactions[
    (transactions['Region'] == 'North') &
    (transactions['Amount'] > 200)
]

print(filtered_data)

# e. Find value counts for ProductCategory

print("Product Category Counts:")
print(transactions['ProductCategory'].value_counts())

# f. Find unique values in Region

print("Unique Regions:")
print(transactions['Region'].unique())

# g. Group by Region and calculate mean Amount

print("Average Amount by Region:")

print(transactions.groupby('Region')['Amount'].mean())

# Q3. Manipulating the DataFrame

# a. Modify Amount for TransactionID 102 to 165

transactions.loc[transactions['TransactionID'] == 102, 'Amount'] = 165

print("After updating Transaction 102:")
print(transactions)

# b. Add Discount column (10% of Amount)

transactions['Discount'] = transactions['Amount'] * 0.10

print("After adding Discount column:")
print(transactions)

# c. Remove the row with TransactionID 109

transactions = transactions[transactions['TransactionID'] != 109]

print("After removing Transaction 109:")
print(transactions)

# d. Delete the Discount column

transactions = transactions.drop(columns=['Discount'])

print("After deleting Discount column:")
print(transactions)