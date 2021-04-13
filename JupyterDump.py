# -*- coding: utf-8 -*-
"""

All of the code I have written so far for the TransactionVisualizationProject 
will be stored here , to be broken up into manageable chunks

"""


# importing the essential libraries and data

import pandas as pd
import datetime as dt

# Exporting the data from the spreadsheet into a pandas dataframe

df = pd.read_excel(r'C:\Users\daypa\Documents\git\Bank_Transaction_Project\TransactionVisualizationProject\Transactions_20-21.xlsx');
print(df.head(10));



# Creating the ValueToDate Function

    
def valueToDate(DataFrame ):
    '''
    (Pandas Data Frame) ---> (Pandas Data Frame)
    
    valueToDate converts Date Values in a pandas data frame into a readable format
    
    Restrictions:
    This function assumes that the column that contains the date values is in row position 0.
    
    
    '''
    rDate = dt.datetime(1899 , 12, 30); # The date at which the date values are referenced 12/30/1899

    for i in range(0 , len(DataFrame)): 
    
        dateValue = DataFrame.iloc[i , (0)]; # The ith date value in the dataset
    
        if type(dateValue) is int: # if a date value is passed then it will be converted into a readable format
        
            dateDays = dt.timedelta(days = dateValue); # Converts the date value into # of days
            realDate = rDate + dateDays;               # Adds the days to the reference to get to the date the value refers to
            DataFrame.iloc[i , (0)] = realDate;        # Replace the date value with the readable date
        
    
        else: # otherwise it will replace whatever its value was with the reference date.
        
            realDate = rDate;
            DataFrame.iloc[i , (0)] = realDate
    
    return DataFrame;



# Calling the valueToDate Function and storing it as a new dataframe object

df2 = valueToDate(df);



# Iterating over the SubClass column and collecting all of the unique values
     

SpecificClass = []; # defining a list to collect unique instances of subclasses
Count = 0;

for i in df2.iloc[: , (3)]: # iterating over the values in the "subclass" column of the dataset
    
    if i not in SpecificClass:
        
        SpecificClass.append(i); # append the SubClass list if the sub class value is not already in the list
        Count += 1; # icrement the count by one every time a new sub class is enocuntererd

print(SpecificClass);    



# Reclassifying the specific SubClass Values into a predetermined set of general ones

SubClasses = ['Utilities' , 'Rent' , 'Loans' , 'Grocery' , 'Car', 'Fast Food' , 'Fun' , 'Misc', 'Transfer'];
# The list of subclasses we want to reclassify other values into

import re # importing the re module


def ReClass(DataFrame): # defining the function
    
    
    UtilReg = re.compile(r'AT&T Internet|Insurance & Phone|SDGE'); # A regex for the utilities category
    LoansReg = re.compile(r'Parent Loans'); # Regex for the loans category
    CarReg = re.compile(r'Gas'); # Regex for the Car category
    MiscReg = re.compile(r'Gym'); # Regex for the Misc category
    MissReg = re.compile(r'Fast Fodd'); # A regex for the misspelling of Fast Food
    TransReg = re.compile(r'Savings 00|Checking 90|College 0867|From College 0867}Checkings 90|Venmo|Savings00|Tax Refund|Cash out');
    
    RegDic = {UtilReg: 'Utilities' , LoansReg: 'Loans' , CarReg: 'Car' , MiscReg: 'Misc' , MissReg: 'Fast Food' , TransReg: 'Transfer'};
    
    # The keys are pattern objects that need to be replaced by the value they refer to
    
    
    for RegX in RegDic.keys(): # iterating over the keys of RegDic
        for i in range(0 , len(DataFrame)): # iterating over the values in the iterable object
            
            if type(DataFrame.iloc[i , (3)]) == float: # Converts the nan into a string
                DataFrame.iloc[i, (3)] = str(DataFrame.iloc[i,(3)]);
            
            
                
            
            mo = RegX.search(DataFrame.iloc[i,(3)]); # Searching for match objects for the regexes
            
            if mo != None: # If a match is found then:
                DataFrame.iloc[i, (3)] = RegDic[RegX]; # Replace the ith item in the iterable object with the value the current key refers to.
            
        
    return DataFrame; # return the modified iterable object
            
        
# Storing the reclassified dataframe as a new one

df3 = ReClass(df2);






    
    
    
    
    