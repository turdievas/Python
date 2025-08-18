import pandas as pd
#Homework 1
#1.
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} ;
df = pd.DataFrame(data)
def rename(column):
    return column.strip().lower().replace(' ', '_')
df.rename(columns=rename, inplace=True)

#2.
# df.head(3)

#3.
mean_age = df['age'].sum()/ df['age'].count()
mean_age

#4.
df[['first_name', 'city']]

#5. 
df['Salary'] = [1500, 2000,4500,1200]
df


#6.
df.describe()


#Homework 2
#1
money = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

mn = pd.DataFrame(money)
mn

#2.
max_sales = max(mn['Sales'])
max_expenses = max(mn['Expenses'])

f"Max sale is {max_sales} and max expense is {max_expenses}"

#3.
min_sales = min(mn['Sales'])
min_expenses = min(mn['Expenses'])

f"min sale is {min_sales} and min expense is {min_expenses}"

#4.
avg_sales = mn['Sales'].mean()
avg_expenses = mn['Expenses'].mean()

f"avg sale is {avg_sales} and avg expense is {avg_expenses}"


#Homework 3
#1
expense = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

expenses = pd.DataFrame(expense).set_index('Category')
expenses

#2.
max_expenses_per_category = expenses.max(axis=1)
max_expenses_per_category


#3.

min_expenses_per_category = expenses.min(axis=1)
min_expenses_per_category
#4.
avg_expenses_per_category = expenses.mean(axis=1)
avg_expenses_per_category
