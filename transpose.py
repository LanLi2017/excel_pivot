from pprint import pprint

import pandas as pd

data = pd.read_excel('demo.xlsx')
data.to_csv('csv_demo.csv')
# set up pivot column
pivoted_col = data['Sales Reps']

# the rest of column names are allocated to a new column: 'location'
col_list = list(data.columns.values)
location_list = [col for col in col_list if col != 'Sales Reps']
# col_list.remove('Sales Reps')

# every value in pivoted column will need to repeat for how many times
repeat_iter = len(col_list) - 1

# Pivoted_table = pd.DataFrame(columns=['Sales Reps', 'Location', 'Amount'])

sales_reps = []
location = []
Amount = []
# first column with repeated values in the new dataframe
for i,v in enumerate(pivoted_col):
    sales_reps.extend([v]*repeat_iter)

# second column with repeated values of rest of columns
location.extend(location_list * repeat_iter)

# transpose rows into one column
df = data.drop('Sales Reps', 1)
for row in df.itertuples(index=False):
    rows = list(row)
    Amount.extend(rows)

Pivoted_table = pd.DataFrame({'Sales Reps':sales_reps, 'Location': location, 'Amount': Amount})
Pivoted_table.to_csv('pivoted_demo.csv')

