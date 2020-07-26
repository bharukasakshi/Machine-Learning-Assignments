# -*- coding: utf-8 -*-
"""stack_overflow
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1XZT8iE0izxcYlc_0m0PgNAqZOf1UUQPB
"""

#import pandas
import pandas as pd 
from matplotlib import pyplot as plt

#download csv file from 
#https://drive.google.com/file/d/1mNePeYPIryqxkP0Y92ajiX7XD69dPV69/view?usp=sharing

#read dataset from Csv file
df = pd.read_csv("survey_results_public.csv")
df

#display  info about dataset
df.info()

#describe dataset
df.describe()

#display all columns
df.columns

#Which  is most used  programming langauge (use LanguageWorkedWith column)
df['LanguageWorkedWith'].value_counts()

#Display how many work remotely on pie chart  [use WorkRemote column]

#Display how many male and female programmers on pie chart  [use Gender column]
male=df[df.Gender=="Man"].shape[0]
female=df[df.Gender=="Woman"].shape[0]
a=[male,female]
b=['Man','Woman']
plt.title('Pie Chart For Male And Female')
plt.pie(a,labels=b,colors=['pink','cyan'],autopct='%.1f%%',shadow=True)
plt.show()

#which developer type is in demand [use DevType column]
df['DevType'].value_counts().idxmax

#which is langauge programmer is going to learn in next year[Display top 3] (use LanguageDesireNextYear column)
df['LanguageDesireNextYear'].value_counts().idxmax

#from which country programmer take part in survey[Display top 3] (use Country column)
df['Country'].value_counts()[0:3]
