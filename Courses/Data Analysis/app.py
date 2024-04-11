import os
import pandas as pd
current_dir = os.path.dirname(__file__)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)

file_path = os.path.join(current_dir, 'degrees-that-pay-back.csv')
df = pd.read_csv(file_path)

def parse_salary(salary_string):
    return float(salary_string.replace('$', '').replace(',', ''))

sorted_df = df.sort_values(by="Starting Median Salary", ascending=False)
sorted_df['Starting Median Salary'] = sorted_df['Starting Median Salary'].apply(parse_salary)
sorted_df['Starting with 1'] = sorted_df['Starting Median Salary'] + 1
print(sorted_df.head().to_markdown(index = False, colalign='left'))