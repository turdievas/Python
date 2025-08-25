import pandas as pd

#Homework 
#1st Dataframe : Student grades

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)
#1.
df1['avg_grade'] =df1[['Math', 'English', 'Science']].mean(axis=1)
#2
top_student = df1.loc[df1['avg_grade'].idxmax()]
#3.
df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)
#4.
subject_averages = df1[['Math','English','Science']].mean()
subject_averages




#DaqtaFrame2 : Sales Data

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)
#1.
total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
#2.
highest_sales_date =df2.loc[df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1).idxmax(), 'Date']
#3.
percent_change = df2[['Product_A', 'Product_B', 'Product_C']].pct_change().fillna(0)
#4.



#3.DataFrame 3: Employee Information

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)
import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)
#1.

df3['Average Salary'] = df3.groupby('Department')['Salary'].transform('mean')
#2
most_experienced_employee = df3.loc[df3['Experience (Years)'].idxmax()]
#3.
df3['Salary Increase'] = (df3['Salary'] - df3['Salary'].min()) / df3['Salary'].min() * 100

#DataFrame 4: Customer Orders
import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)
df4
#1
total_revenue = df4['Total_Price'].sum()
total_revenue

#2.
most_ordered_product = df4['Product'].mode()[0]
most_ordered_product

#3.

average_quantity = df4['Quantity'].mean()
average_quantity
