# --------------
import numpy as np
import pandas as pd
# Read the data. Data is already loaded in the variable `path` use the `delimeter = ';'`.
data = pd.read_csv(path, delimiter=';')
print(data.shape)

# Replace the `unknown` values with the `Nan` and check the value count of missing values and drop the missing rows
print(data.isnull().sum())
data = data.replace(to_replace ='unknown', value =np.nan)
print(data.isnull().sum())

data = data.dropna()
print(data.shape)

# Replace the column name from `loan` to `previous_loan_status` and `y` to `loan_status` 
print(list(data.columns))
data.rename(columns={'loan':'previous_loan_status', 'y':'loan_status'}, inplace = True)
print(list(data.columns))

# Find out the information of the `job` column.
print(data.info())

# Check the `loan_status`  approval rate by `job`
print(data.groupby('job')['loan_status'].value_counts())

# Check the percentage of loan approved by `education`
print(data.groupby('education')['loan_status'].value_counts())

# Check the percentage of loan approved by `previous loan status`
print(data.groupby('previous_loan_status')['loan_status'].value_counts())

# Create a pivot table between `loan_status` and `marital ` with values form `age`
table = pd.pivot_table(data, index=['loan_status','marital'], values ='age')
print(table)

# Loan status based on marital status whose status is married

#Create a  Dataframes 

# Create a dataframe `df_branch_1` where keys are `'customer_id','first_name','last_name'` you can take any value 
data1 = {'customer_id':['1'], 'first_name':['S'],'last_name':['T']}
df_branch_1 = pd.DataFrame(data1)

# Create a dataframe `df_branch_2` where keys are `'customer_id','first_name','last_name'` you can take any value
data2 = {'customer_id':['2'], 'first_name':['A'],'last_name':['B']}
df_branch_2 = pd.DataFrame(data2)

# Create a dataframe `df_credit_score` where keys are `'customer_id','score'` you can take any value
data3 = {'customer_id':['2'], 'score':['20']}
df_credit_score = pd.DataFrame(data3)

# Concatenate the dataframe `df_branch_1` and `df_branch_2` along the rows
df_new = pd.concat([df_branch_1,df_branch_2])
print(df_new)

# Merge two dataframes `df_new` and `df_credit_score` with both the left and right dataframes using the `customer_id` key
new_table = pd.merge(df_new, df_credit_score, how ='left', on ='customer_id')
print(new_table)

new_table1 = pd.merge(df_new, df_credit_score, how ='right', on ='customer_id')
print(new_table1)



