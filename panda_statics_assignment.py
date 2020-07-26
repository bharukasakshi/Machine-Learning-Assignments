# -*- coding: utf-8 -*-
"""pandas_statistics.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1SZo3VC_6XrE__ZTk5OhExIGvT1Y4fqHf
"""



# Import the necessary libraries
import pandas as pd

#load dataset from csv file
data=pd.read_csv("baby_names.csv")

#See the first 10 entries
data.head(10)

#display all columns from dataframe
data.info()

#Delete the column 'Unnamed: 0' and 'Id'
data.drop(columns=['Unnamed: 0', 'Id'])

#Is there more male or female names in the dataset?
data.Gender.value_counts()
print("females count is more")

#display the count of each name present in dataset
data.Name.value_counts()

#group by name and assign it name grouped_names like
# grouped_name=df.groupby("Name").sum()
#aapply following operations on grouped_names variable

#What is the name with most occurrences?
data['Count'].idxmax()



#How many different names have the least occurrences

#Get a summary with the mean, min, max, std 
data.describe()