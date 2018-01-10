# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 22:31:40 2016

@author: michaelchan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Loading csv file
titanic_file = pd.read_csv('titanic_data.csv')

print titanic_file.count()

total = titanic_file_survival.count()

'''
1) Numpy 1D array of males and females.  Average percentage of males survived.
Vs Percentage of females survived.  Indexes is male and female.
Data is survived or died.

Average number of people survived and died.
'''

def chances_of_survival():
    titanic_file_survival = titanic_file['Survived']    
    for i in range(0,1):
        survivors = titanic_file_survival[titanic_file_survival==i].count()
        if i == 0:
            print "Number of people who died:",survivors
        elif i == 1:
            print "Number of people who survived:",survivors
            print " "
            print "People on board had a" , float(i)/float(total) , "chance of surviving."
        print " "

def avg_age_survival():
    for i in range(0,1):
        Ages = titanic_file[titanic_file['Survived']==i]['Age'].dropna()
        if i == 0:
            print "Average Age of ones who survived:", Ages.mean()
        elif i == 1:
            print "Average Age of ones who died:", Ages.mean()
        print " "
        
def gender_survival():
    survived_males = titanic_file[titanic_file['Survived']==1][titanic_file['Sex']=='male']['Sex'].count()
    total_males= titanic_file[titanic_file['Sex']=='male']['Sex'].count()
    print float(survived_males)/float(total_males)


chances_of_survival()
    
avg_age_survival()
    
gender_survived()
    

'''
males_survived = titanic_file_sex[titanic_file_sex=='male'].count()
total_males = titanic_file['Sex'][titanic_file['Sex']=='male'].count()
print males_survived, total_males
print "Percentage of Males Survived:", males_survived/total_males
print " "
'''
'''
3) Dataframe exploration: Does Male/Female (Column) AND Age 
(Index grouped as (0-10, 10-20, 20-30, 30-40, 40-50, 50+) have an effect? 
Data is 'Survived'. Or use pd.qcut
'''

'''
4) Numpy Array (2D) of survival and deaths if they are part of a family.
1 array for SibSp
1 array for Parch
What is the survival amongst either they have only siblings?
Only Parents?
Both?
None
'''



'''
print titanic_died.Age.sum()

titanic_survived = titanic_data[titanic_data.Survived.isin([1])]

print titanic_survived.Age.mean()
print titanic_survived.Age.sum()

titanic_died = titanic_data[titanic_data.Survived.isin([0])]

print titanic_died.Age.mean()
print titanic_died.Age.sum()

Questions to Explore:








One Dataframe for survived and one for died.

'''