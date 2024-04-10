# Data Analytics

## Pandas

When working with tabular data, such as data stored in spreadsheets or databases, pandas is the right tool for you. pandas will help you to explore, clean, and process your data. In pandas, a data table is called a DataFrame.

##### Setup DataFrame

###### Configure Row & Column Maxes

```python
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
```

###### Create DataFrame from CSV

```python
df = pd.read_csv('uk_universities.csv')
```

###### Create a DataFrame from List

```python
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    columns = ['student_id', 'age']
    df = pd.DataFrame.from_records(student_data, columns=columns)
```

#### Data Inspection

###### Get the Size of a DataFrame

```python
num_rows, num_columns = players.shape
```

###### Display first 5 rows

```python
print(df.head())
```

###### Display the First Three Rows

```python
employees.head(3)
```

###### Display column names & data types

```python
print(df.info())
```

###### Print column names

```python
print(df.columns.to_list())
```

###### Print as Markdown Table

```python
print(df.to_markdown())
```

#### Select Data

###### Select on value

- Select a row on a value
- return only specific fields of row

```python
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    row = students[students['student_id'] == 101]
    return row[['name', 'age']]
```

#### Data Cleaning

###### Replace/Fill null column values

```python
df['Motto'] = df['Motto'].fillna('')
```

###### Sort on a field

```python
sorted_df = df.sort_values(by="Starting Median Salary", ascending=False)
print(sorted_df.head().to_markdown(index = False, colalign='left'))
```

###### Drop duplicate records on a specific column

```python
def dropDuplicateEmails(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates(subset=['email'])
```

###### Drop rows where column has null value

```python
def dropMissingData(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna(subset=['name'])
```

###### Modify a column

```python
def modifySalaryColumn(df: pd.DataFrame) -> pd.DataFrame:
    df['salary'] = df['salary'] * 2
    return df
```

###### Parse Currency String to Perform Arithmetic

```python
def parse_salary(salary_string):
  return float(salary_string.replace('$', '').replace(',', ''))

sorted_df = df.sort_values(by="Starting Median Salary", ascending=False)
sorted_df['Starting Median Salary'] = sorted_df['Starting Median Salary'].apply(parse_salary)
sorted_df['Starting with 1'] = sorted_df['Starting Median Salary'] + 1
```

###### Rename Columns

```python
def renameColumns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns={
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    })
    return df
```

###### Cast Column Data Type

```python
def changeDatatype(df: pd.DataFrame) -> pd.DataFrame:
    df['grade'] = df['grade'].astype(int)
    return df
```

##### Reshape Data

###### Create New Column

- Create column bonus by doubling column salary

```python
def createBonusColumn(df: pd.DataFrame) -> pd.DataFrame:
    df['bonus'] = df['salary'] * 2
    return df
```

###### Concatenate Multiple DataFrames into One

```python
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    result = pd.concat([df1, df2], axis=0)
    return result
```

###### Pivot on a column

- Turn record values that repeat into it's columns.

```python
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(weather)
    pivot_df = df.pivot_table(index='month', columns='city', values='temperature', aggfunc='first')
    return pivot_df
```

###### Melt: Switching from

The DataFrame is reshaped from wide to long format. Each row represents the sales of a product in a quarter.

```python
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(report)
    reshaped_df = pd.melt(df, id_vars=['product'], var_name='quarter', value_name='sales')
    return reshaped_df
```

##### Charting

###### Title, X Label, Y Label

```python
plt.title('MPG vs Car Name')
plt.xlabel('MPG')
plt.ylabel('Car Name')
```

##### Advanced

- Filter DF on a field expression
- Sort on a field
- Parse only on field

```python
def findHeavyAnimals(data: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(data)
    filtered_df = df[df['weight'] > 100]
    sorted_df = filtered_df.sort_values(by='weight', ascending=False)
    return sorted_df[['name']]
```
