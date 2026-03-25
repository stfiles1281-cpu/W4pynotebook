#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[6]:


#Creating a Series
s = pd.Series( [10, 20, 30, 40], index=['a', 'b', 'c', 'd'] )
print("Series:")
print(s)
print(f"Value at index 'c': {s['c']}")


# In[95]:


#Creating a Dataframe
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Andrea', 'Jack', 'Julie', 'Paul', 'Rosie'],
    'Age': [25, 32, 19, 29, 22, 34, 34, 35, 32],
    'Salary': [5000, 68000, 75000, 62000, 12000, 34000, 234440, 237890, 12000],
    'Department': ['HR', 'IT', 'IT', 'Marketing', 'HR', 'IT', 'Marketing', 'IT', 'IT'],
    'City': ['NewYork', 'Paris', 'Tokyo', 'Florida', 'NewYork', 'Seoul', 'Sofia', 'Sydney', 'Toronto'],
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.head())
print(df.tail(3))
print(df.describe())


# In[96]:


#Select a single column ( returns a Series)
ages = df['Age']
print(ages)


# In[93]:


#Selct multuiple columns (returns a DataFrame)
subset= df[['Name', 'City']]
print(subset)


# In[94]:


df.iloc[6:10,[0,3]]


# In[ ]:


# Find all students older than 28
older_students = df [df ['Age' ] > 28]

# Multiple conditions (use & for AND, | for OR)
# Students older than 25 AND from London
filtered = df [(df ['Age'] > 25) & (df ['City' ] == 'London' )]

# Students younger than 30 OR from Paris
filtered = df[(df['Age'] < 30) | (df ['City'] == 'Paris')]

# Check for missing values
missing_ages = df [df ['Age' ]. isna() ]


# In[80]:


TASK = df[(df ['Age' ] 25) & (df['Department'] == 'IT')]
print(TASK)


# In[83]:


df ["Orgin_Country"] = ["China", "Nepal", "Bangladesh", "India", "France", "Turkey", "Canada", "Japan", "Russia"]


# In[87]:


df["Age_category"] = df["Age"].apply(
    lambda x: "Young" if x < 20 else "Middle"
)


# In[88]:


df


# In[ ]:


df.isna()
df.isna().sum()

# Drop missing values
df_clean = df.dropna()
df_clean = df.dropna(subset=['age'])

# Fill missing values
df_filled = df.fillna(0)
df_filled = df.fillna({'age': df['age'].mean()}) # Fill age with mean
df_filled = df ['age'].fillna(df ['age'].median()) # Fill series with median

