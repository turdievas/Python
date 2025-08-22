import pandas as pd

#Homework 
#1
import pandas as pd

sales_data = pd.read_csv('sales_data.csv')

stats = sales_data.groupby('Category').agg(
    Total_Quantity_Sold=('Quantity', 'sum'),
    Average_Price_Per_Unit=('Price', 'mean'),
    max_qty =('Quantity', 'max') 
)
stats

#Homework 2. Examining Customer Orders
import pandas as pd

customer_orders = pd.read_csv('customer_orders.csv')
#tasks 
#1.
order_counts = customer_orders.groupby('CustomerID').size()
customers_20plus = order_counts[order_counts >= 20].index
filtered_orders = customer_orders[customer_orders['CustomerID'].isin(customers_20plus)]
filtered_orders
#2.
avg_price = customer_orders.groupby('CustomerID')['Price'].mean()
greater_than_120= avg_price[avg_price>120]
greater_than_120
#3.
tt_qty_tt_price = customer_orders.groupby('Product').agg(tt_qty =('Quantity','sum'),
tt_price = ('Price', 'sum'))
filtered_products = tt_qty_tt_price[tt_qty_tt_price['tt_qty'] < 5]

filtered_products


#Homework 3

import sqlite3
conn  = sqlite3.connect('population.db')

salary_analysis = pd.read_excel('population_salary_analysis.xlsx')
query  = 'select * from population'
df = pd.read_sql_query(query,conn)
conn.close()

import sqlite3
import pandas as pd
import numpy as np

# ---------------------------
# 1. Read population data from SQLite
# ---------------------------
conn = sqlite3.connect('population.db')
query = 'SELECT * FROM population'
df = pd.read_sql_query(query, conn)
conn.close()

# ---------------------------
# 2. Read salary band definitions from Excel
# ---------------------------
salary_analysis = pd.read_excel('population_salary_analysis.xlsx')

# Assume columns: Band, MinSalary, MaxSalary
# Sort by MinSalary to ensure correct order
salary_analysis = salary_analysis.sort_values(by='MinSalary')

# ---------------------------
# 3. Assign each person to a salary band
# ---------------------------
# Build bins and labels dynamically
bins = salary_analysis['MinSalary'].tolist() + [float('inf')]
labels = salary_analysis['Band'].tolist()

df['SalaryCategory'] = pd.cut(df['salary'],
                              bins=bins,
                              labels=labels,
                              right=True,
                              include_lowest=True)

# ---------------------------
# 4. Overall summary by salary category
# ---------------------------
group = df.groupby('SalaryCategory')

summary_overall = pd.DataFrame({
    'PopulationCount': group['salary'].count(),
    'AverageSalary': group['salary'].mean(),
    'MedianSalary': group['salary'].median()
})

total_population = len(df)
summary_overall['PopulationPercent'] = (summary_overall['PopulationCount'] / total_population) * 100
summary_overall = summary_overall.reset_index()

# ---------------------------
# 5. Summary by State and salary category
# ---------------------------
group_state = df.groupby(['state', 'SalaryCategory'])

summary_state = pd.DataFrame({
    'PopulationCount': group_state['salary'].count(),
    'AverageSalary': group_state['salary'].mean(),
    'MedianSalary': group_state['salary'].median()
}).reset_index()

# Add percentage of population within each state
state_totals = df.groupby('state')['salary'].count()
summary_state['PopulationPercent'] = summary_state.apply(
    lambda row: (row['PopulationCount'] / state_totals[row['state']]) * 100, axis=1
)

# ---------------------------
# 6. Display or save results
# ---------------------------
print("Overall Salary Category Summary:")
print(summary_overall)

print("\nSalary Category Summary by State:")
print(summary_state)

# Optional: export to Excel
with pd.ExcelWriter('population_salary_analysis_results.xlsx') as writer:
    summary_overall.to_excel(writer, sheet_name='Overall', index=False)
    summary_state.to_excel(writer, sheet_name='ByState', index=False)


