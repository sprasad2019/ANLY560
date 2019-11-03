# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 21:24:18 2019

@author: swethap
"""

# IMPORTING PANDAS

# 1. Import pandas under the name pd 
import pandas as pd

# 2. Print the version of pandas that has been imported
pd.__version__

# 3. Print out all the version information of the libraries that are required by the pandas library
pd.show_versions()


# DATAFRAME BASICS 

# 4. Create a DataFrame df from this dictionary data which has the index labels
import numpy as np

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, index=labels)

# 5. Display a summary of the basic information about this DataFrame and its data
df.describe()

# 6. Return the first 3 rows of the DataFrame df
df.head(3)

# 7. Select just the 'animal' and 'age' columns from the DataFrame df
df[['animal', 'age']]

# 8. Select the data in rows [3, 4, 8] and in columns ['animal', 'age']
df.loc[df.index[[3, 4, 8]], ['animal', 'age']]

# 9. Select only the rows where the number of visits is greater than 3
df[df['visits'] > 3]

# 10. Select the rows where the age is missing, i.e. is NaN
df[df['age'].isnull()]

# 11. Select the rows where the animal is a cat and the age is less than 3
df[(df['animal'] == 'cat') & (df['age'] < 3)]

# 12. Select the rows the age is between 2 and 4 (inclusive)
df[df['age'].between(2, 4)]

# 13. Change the age in row 'f' to 1.5
df.loc['f', 'age'] = 1.5

# 14. Calculate the sum of all visits (the total number of visits)
df['visits'].sum()

# 15. Calculate the mean age for each different animal in df
df.groupby('animal')['age'].mean()

# 16. Append a new row 'k' to df with your choice of values for each column. Then delete that row to return the original DataFrame
df.loc['k'] = [5.5, 'dog', 'no', 2]
df = df.drop('k')

# 17. Count the number of each type of animal in df
df['animal'].value_counts()

# 18. Sort df first by the values in the 'age' in decending order, then by the value in the 'visit' column in ascending order
df.sort_values(by=['age', 'visits'], ascending=[False, True])

# 19. The 'priority' column contains the values 'yes' and 'no'. Replace this column with a column of boolean values: 'yes' should be True and 'no' should be False
df['priority'] = df['priority'].map({'yes': True, 'no': False})

# 20. In the 'animal' column, change the 'snake' entries to 'python'
df['animal'] = df['animal'].replace('snake', 'python')

# 21. For each animal type and each number of visits, find the mean age. In other words, each row is an animal, each column is a number of visits and the values are the mean ages (hint: use a pivot table)
df.pivot_table(index='animal', columns='visits', values='age', aggfunc='mean')


# DATAFRAMES: BEYOND THE BASICS

# 22. You have a DataFrame df with a column 'A' of integers. How do you filter out rows which contain the same integer as the row immediately above?
df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
df.drop_duplicates(subset='A')

# 23. Given a DataFrame of numeric values, say df = pd.DataFrame(np.random.random(size=(5, 3))) # a 5x3 frame of float values, how do you subtract the row mean from each element in the row?
df.sub(df.mean(axis=1), axis=0)

# 24. Suppose you have DataFrame with 10 columns of real numbers, for example: df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij')). Which column of numbers has the smallest sum? (Find that column's label.)
df.sum().idxmin()

# 25. How do you count how many unique rows a DataFrame has (i.e. ignore all rows that are duplicates)?
len(df.drop_duplicates(keep=False))

# 26. You have a DataFrame that consists of 10 columns of floating--point numbers. Suppose that exactly 5 entries in each row are NaN values. For each row of the DataFrame, find the column which contains the third NaN value
(df.isnull().cumsum(axis=1) == 3).idxmax(axis=1)

# 27. A DataFrame has a column of groups 'grps' and and column of numbers 'vals'. For each group, find the sum of the three greatest values.
df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 
                   'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})

df.groupby('grps')['vals'].nlargest(3).sum(level=0)

# 28. A DataFrame has two integer columns 'A' and 'B'. The values in 'A' are between 1 and 100 (inclusive). For each group of 10 consecutive integers in 'A' (i.e. (0, 10], (10, 20], ...), calculate the sum of the corresponding values in column 'B'
df.groupby(pd.cut(df['A'], np.arange(0, 101, 10)))['B'].sum()


# DATAFRAMES: HARDER PROBLEMS

# 29. Consider a DataFrame df where there is an integer column 'X'. For each value, count the difference back to the previous zero (or the start of the Series, whichever is closer). These values should therefore be [1, 2, 0, 1, 2, 3, 4, 0, 1, 2]. Make this a new column 'Y'
df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

x = (df['X'] != 0).cumsum()
y = x != x.shift()
df['Y'] = y.groupby((y != y.shift()).cumsum()).cumsum()

# 30. Consider a DataFrame containing rows and columns of purely numerical data. Create a list of the row-column index locations of the 3 largest values
df.unstack().sort_values()[-3:].index.tolist()

# 31. Given a DataFrame with a column of group IDs, 'grps', and a column of corresponding integer values, 'vals', replace any negative values in 'vals' with the group mean
df.groupby(['grps'])['vals'].transform(replace)

# 32. Implement a rolling mean over groups with window size 3, which ignores NaN value. For example consider the following DataFrame
df = pd.DataFrame({'group': list('aabbabbbabab'),
                       'value': [1, 2, 3, np.nan, 2, 3, 
                                 np.nan, 1, 7, 3, np.nan, 8]})

g1 = df.groupby(['group'])['value']              
g2 = df.fillna(0).groupby(['group'])['value']    

s = g2.rolling(3, min_periods=1).sum() / g1.rolling(3, min_periods=1).count() 
s.reset_index(level=0, drop=True).sort_index() 

# SERIES AND DATETIMEINDEX

# 33. Create a DatetimeIndex that contains each business day of 2015 and use it to index a Series of random numbers. Let's call this Series s
dti = pd.date_range(start='2015-01-01', end='2015-12-31', freq='B') 
s = pd.Series(np.random.rand(len(dti)), index=dti)

# 34. Find the sum of the values in s for every Wednesday
s[s.index.weekday == 2].sum()

# 35. For each calendar month in s, find the mean of values
s.resample('M').mean()

# 36. For each group of four consecutive calendar months in s, find the date on which the highest value occurred
s.groupby(pd.TimeGrouper('4M')).idxmax()

# 37. Create a DateTimeIndex consisting of the third Thursday in each month for the years 2015 and 2016
pd.date_range('2015-01-01', '2016-12-31', freq='WOM-3THU')

# CLEANING DATA

# 38. Some values in the the FlightNumber column are missing. These numbers are meant to increase by 10 with each row so 10055 and 10075 need to be put in place. Fill in these missing numbers and make the column an integer column (instead of a float column)
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 
                               'Budapest_PaRis', 'Brussels_londOn'],
              'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
              'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', 
                               '12. Air France', '"Swiss Air"']})

df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)

# 39. The From_To column would be better as two separate columns! Split each string on the underscore delimiter _ to give a new temporary DataFrame with the correct values. Assign the correct column names to this temporary DataFrame
temp = df.From_To.str.split('_', expand=True)
temp.columns = ['From', 'To']

# 40. Notice how the capitalisation of the city names is all mixed up in this temporary DataFrame. Standardise the strings so that only the first letter is uppercase (e.g. "londON" should become "London".)
temp['From'] = temp['From'].str.capitalize()
temp['To'] = temp['To'].str.capitalize()

# 41. Delete the From_To column from df and attach the temporary DataFrame from the previous questions
df = df.drop('From_To', axis=1)
df = df.join(temp)

# 42. In the Airline column, you can see some extra puctuation and symbols have appeared around the airline names. Pull out just the airline name. E.g. '(British Airways. )' should become 'British Airways'
df['Airline'] = df['Airline'].str.extract('([a-zA-Z\s]+)', expand=False).str.strip()

# 43. In the RecentDelays column, the values have been entered into the DataFrame as a list. We would like each first value in its own column, each second value in its own column, and so on. If there isn't an Nth value, the value should be NaN
delays = df['RecentDelays'].apply(pd.Series)
delays.columns = ['delay_{}'.format(n) for n in range(1, len(delays.columns)+1)]
df = df.drop('RecentDelays', axis=1).join(delays)

# USING MULTIINDEXES

# 44. Given the lists letters = ['A', 'B', 'C'] and numbers = list(range(10)), construct a MultiIndex object from the product of the two lists. Use it to index a Series of random numbers. Call this Series s
letters = ['A', 'B', 'C']
numbers = list(range(10))

mi = pd.MultiIndex.from_product([letters, numbers])
s = pd.Series(np.random.rand(30), index=mi)

# 45. Check the index of s is lexicographically sorted (this is a necessary proprty for indexing to work correctly with a MultiIndex)
s.index.is_lexsorted()
s.index.lexsort_depth == s.index.nlevels

# 46. Select the labels 1, 3 and 6 from the second level of the MultiIndexed Series
s.loc[:, [1, 3, 6]]

# 47. Slice the Series s; slice up to label 'B' for the first level and from label 5 onwards for the second level
s.loc[pd.IndexSlice[:'B', 5:]]
s.loc[slice(None, 'B'), slice(5, None)]

# 48. Sum the values in s for each label in the first level (you should have Series giving you a total for labels A, B and C)
s.sum(level=0)

# 49. Suppose that sum() (and other methods) did not accept a level keyword argument. How else could you perform the equivalent of s.sum(level=1)?
s.unstack().sum(axis=0)

# 50. Exchange the levels of the MultiIndex so we have an index of the form (letters, numbers). Is this new Series properly lexsorted? If not, sort it
new_s = s.swaplevel(0, 1)
new_s.index.is_lexsorted()
new_s = new_s.sort_index()


