#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#load dataset and store  
data = pd.read_csv('fuel_ferc1.csv')
data.head()


# DATA CLEANING

# In[3]:


#information on feul dataset
data.info()


# In[4]:


#checking for missing values
data.isnull().sum()


# In[5]:


#calculate median of missing column
mode = data['fuel_unit'].mode()
mode


# In[6]:


#replacing missing values
#ata['fuel_unit'].replace(mode,inplace =True)


# In[7]:


data.describe(include ='all')


# In[8]:


data.dtypes


# ANALYSIS

# In[9]:


data['fuel_type_code_pudl'].value_counts().plot(kind='bar')


# In[10]:


x = data['report_year']
y= data['fuel_qty_burned'] 
plt.bar(x,y)
plt.title('Barchat of year against burned fuel quantity')


# QUIZ SOLUTIONS

# 1.
# A = [1,2,3,4,5,6] B= [13,21,34]

# In[11]:


A =[1,2,3,4,5,6]
B= [13,21,34]

A.extend(B)
print("Extend gives: ",A)

A.append(B)
print("Append gives: ",A)


# Ans = A.extend(B)

# 2. Creating an index matrix:

# In[12]:


np.identity(3)


# In[13]:


np.array([1, 0, 0], [0, 1, 0], [0, 0, 1])


# In[14]:


np.array[(1, 0, 0), (0, 1, 0), (0, 0, 1)]


# In[15]:


eye(3)


# Ans = np.identity(3)

# 3.lowest fuel cost per unit burned by fuel type code 

# In[16]:


3. # group by 'fuel_type_code_pudl' and calculate the mean 'fuel_cost_per_unit_burned'
data.groupby('fuel_type_code_pudl').fuel_cost_per_unit_burned.mean().sort_values()


# Ans = gas

# 4. standard deviation and 75th percentile of fuel_mmbtu_per_unit

# In[17]:


standard_deviation= data.fuel_mmbtu_per_unit.std()
print("Standard deviation: ", round(standard_deviation,2))

percentile= data.fuel_mmbtu_per_unit.quantile(0.75)
print("75th percentile: ", round(percentile, 2))


# Ans = 10.6 and 17.01

# 5. Skewness and Kurtosis of the fuel quantity

# In[18]:


skewness= data.fuel_qty_burned.skew()
print("Skewness:", round(skewness, 2))

kurtosis= data.fuel_qty_burned.kurt()
print("Kurtosis:", round(kurtosis, 2))


# Ans= 15.85 and 651.37

# 6. Feature with missing values, total number of missing values and percentage

# In[19]:


#total number of missing values
data.isna().sum().sort_values(ascending=False)


# In[20]:


# percentage of missing values
missing = data.fuel_unit.isna().sum()
rows = data.shape[0]
percentage_missing = (missing / rows) * 100
print("Percentage of missing values: ", round(percentage_missing, 3))


# Ans= Feature: fuel_unit, Total: 180, Percent: 0.610

# 7. missing value type

# In[21]:


#since fuel_unit is the missing vale, we check for the data type 
data.fuel_unit.dtypes


# 'O' stands for the datatype 'object', which is a categorical variable
# 
# Ans= categorical and mode imputation

# 8. Second and third lowest correlation with the Fuel Cost Per Unit Burned?

# In[22]:


correlation = data.corr()
correlation.fuel_cost_per_unit_burned.sort_values().sort_values(ascending=False)


# Ans= fuel_qty_burned and fuel_mmbtu_per_unit

# In[23]:


#using the heatmap graph
f, ax = plt.subplots(figsize=(12,8))
sns.heatmap(data.corr(), annot=True, linewidths=0.5, fmt='.1f', ax=ax)


# 9. Percentage change of coal in the fuel cost per unit burned in 1998 compared to 1994?

# In[24]:


# select records with fuel type coal for 1994 and 1998
coal_1994 = data.loc[(data['fuel_type_code_pudl'] == 'coal') & ((data['report_year'] == 1994))]
coal_1998 = data.loc[(data['fuel_type_code_pudl'] == 'coal') & ((data['report_year'] == 1998))]

#calculate sum of both
coal_1994_sum = coal_1994.fuel_cost_per_unit_burned.sum()
coal_1998_sum = coal_1998.fuel_cost_per_unit_burned.sum()

#
percent_change = (coal_1998_sum - coal_1994_sum) / coal_1994_sum * 100
print("Percentage change of coal: ", round(percent_change))


# Ans= -21%

# 10. Year with the highest average fuel cost per unit delivered

# In[25]:


# group by 'report_year' and calculate mean of 'fuel_cost_per_unit_burned'
data.groupby('report_year').fuel_cost_per_unit_delivered.mean().sort_values(ascending = False)[:3]


# Ans= 1997

# In[ ]:




